"""
Core markdown to ANSI converter
"""

import re
from typing import List, Tuple
from .styles import ANSIColors, get_theme


# ASCII art font definitions for max mode
ASCII_FONT_SMALL = {
    'A': ['▄▀█', '█▄▄'],
    'B': ['█▄▄', '█▄█'],
    'C': ['▄▀█', '█▄▄'],
    'D': ['█▀▄', '█▄▀'],
    'E': ['█▀▀', '█▄▄'],
    'F': ['█▀▀', '█▀▀'],
    'G': ['▄▀█', '█▄█'],
    'H': ['█▄█', '█▀█'],
    'I': ['█', '█'],
    'J': ['  █', '█▄█'],
    'K': ['█▄▀', '█▀▄'],
    'L': ['█  ', '█▄▄'],
    'M': ['█▄█', '█▀█'],
    'N': ['█▄█', '█▀█'],
    'O': ['▄▀█', '█▄█'],
    'P': ['█▀▄', '█▀▀'],
    'Q': ['▄▀█', '█▄█'],
    'R': ['█▀▄', '█▀▄'],
    'S': ['▄▀▀', '▄▄█'],
    'T': ['▀█▀', ' █ '],
    'U': ['█▄█', '█▄█'],
    'V': ['█▄█', ' █ '],
    'W': ['█▄█', '█▄█'],
    'X': ['█▄█', '█▀█'],
    'Y': ['█▄█', ' █ '],
    'Z': ['▀▀█', '█▄▄'],
    ' ': [' ', ' '],
    '1': ['█', '█'],
    '2': ['▀▀█', '█▄▄'],
    '3': ['▀▀█', '▄▄█'],
    '4': ['█▄█', '  █'],
    '5': ['█▀▀', '▄▄█'],
    '6': ['█▀▀', '█▄█'],
    '7': ['▀▀█', '  █'],
    '8': ['█▄█', '█▄█'],
    '9': ['█▄█', '▄▄█'],
    '0': ['█▄█', '█▄█'],
}

ASCII_FONT_LARGE = {
    'A': ['  ▄▀█  ', ' █▄▄█ ', '█▀   ▀█'],
    'B': ['█▀▀▀▀▄', '█▄▄▄▄▀', '█▄▄▄▄▀'],
    'C': [' ▄▀▀▀▀▄', '█▀     ', '█▄▄▄▄▄▀'],
    'D': ['█▀▀▀▀▄ ', '█     █', '█▄▄▄▄▀ '],
    'E': ['█▀▀▀▀▀▀', '█▄▄▄▄▄ ', '█▄▄▄▄▄▄'],
    'F': ['█▀▀▀▀▀▀', '█▄▄▄▄▄ ', '█      '],
    'G': [' ▄▀▀▀▀▄ ', '█▀   ▄▄', '█▄▄▄▄▀█'],
    'H': ['█▄   ▄█', '█▀▀▀▀▀█', '█     █'],
    'I': ['█', '█', '█'],
    'J': ['     █', '     █', '█▄▄▄▄▀'],
    'K': ['█▄  ▄▀', '█▀▀▀▄ ', '█   ▀▄'],
    'L': ['█      ', '█      ', '█▄▄▄▄▄▄'],
    'M': ['█▄   ▄█', '█▀▀▀▀▀█', '█     █'],
    'N': ['█▄   ▄█', '█▀▀▀▀▀█', '█     █'],
    'O': [' ▄▀▀▀▀▄ ', '█▀   ▀█', '█▄▄▄▄▄▀'],
    'P': ['█▀▀▀▀▄ ', '█▄▄▄▄▀ ', '█      '],
    'Q': [' ▄▀▀▀▀▄ ', '█▀   ▀█', '█▄▄▄▄▄▀'],
    'R': ['█▀▀▀▀▄ ', '█▄▄▄▄▀ ', '█   ▀▄ '],
    'S': [' ▄▀▀▀▀▄', '█▄▄▄▄▄ ', '▄▄▄▄▄▀█'],
    'T': ['▀▀▀█▀▀▀', '   █   ', '   █   '],
    'U': ['█▄   ▄█', '█▀   ▀█', '█▄▄▄▄▄▀'],
    'V': ['█▄   ▄█', '█▀▄ ▄▀█', '  ▀█▀  '],
    'W': ['█▄   ▄█', '█▀▀▀▀▀█', '█▄   ▄█'],
    'X': ['█▄   ▄█', ' ▀▄▄▄▀ ', '█▀   ▀█'],
    'Y': ['█▄   ▄█', ' ▀▄▄▄▀ ', '   █   '],
    'Z': ['▀▀▀▀▀▀█', '  ▄▄▄▀ ', '█▄▄▄▄▄▄'],
    ' ': ['   ', '   ', '   '],
    '1': [' █', ' █', ' █'],
    '2': [' ▄▀▀▀▄', '▄▄▄▄▄▀', '█▄▄▄▄▄'],
    '3': [' ▄▀▀▀▄', '▄▄▄▄▄▀', '▄▄▄▄▄▀'],
    '4': ['█▄   █', '▀▀▀▀▀█', '     █'],
    '5': ['█▀▀▀▀▀', '█▄▄▄▄▄', '▄▄▄▄▄▀'],
    '6': ['█▀▀▀▀▀', '█▄▄▄▄▄', '█▄▄▄▄▄'],
    '7': ['▀▀▀▀▀█', '     █', '     █'],
    '8': ['█▄▄▄▄█', '█▄▄▄▄█', '█▄▄▄▄█'],
    '9': ['█▄▄▄▄█', '▀▀▀▀▀█', '▄▄▄▄▄▀'],
    '0': ['█▄▄▄▄█', '█▄▄▄▄█', '█▄▄▄▄█'],
}


def generate_ascii_art(text: str, font_size: str = 'small') -> List[str]:
    """Generate ASCII art from text using the specified font size"""
    text = text.upper()
    font = ASCII_FONT_SMALL if font_size == 'small' else ASCII_FONT_LARGE
    
    # Get the height of the font
    height = len(font.get('A', [' ']))
    
    # Create lines for the ASCII art
    lines = [''] * height
    
    for char in text:
        char_art = font.get(char, font.get(' ', [' '] * height))
        for i, line in enumerate(char_art):
            if i < len(lines):
                lines[i] += line + ' '
    
    return lines


class MarkdownToANSIConverter:
    """Convert markdown to ANSI-formatted text"""
    
    def __init__(self, style_name='beach', max_mode=False):
        self.theme = get_theme(style_name)
        self.max_mode = max_mode
        self.reset = ANSIColors.RESET
        
    def convert(self, markdown_text: str) -> str:
        """Convert markdown text to ANSI-formatted text"""
        lines = markdown_text.split('\n')
        result = []
        
        in_code_block = False
        code_block_lang = None
        
        for line in lines:
            if line.strip().startswith('```'):
                # Code block toggle
                if in_code_block:
                    in_code_block = False
                    code_block_lang = None
                    result.append(self._format_code_block_end())
                else:
                    in_code_block = True
                    code_block_lang = line.strip()[3:].strip()
                    result.append(self._format_code_block_start(code_block_lang))
                continue
            
            if in_code_block:
                result.append(self._format_code_line(line))
                continue
                
            # Process line based on markdown syntax
            formatted_line = self._format_line(line)
            result.append(formatted_line)
        
        return '\n'.join(result) + self.reset
    
    def _format_line(self, line: str) -> str:
        """Format a single line of markdown"""
        stripped = line.strip()
        
        # Headers
        if stripped.startswith('#'):
            return self._format_header(line)
        
        # Blockquotes
        if stripped.startswith('>'):
            return self._format_blockquote(line)
        
        # Lists
        if re.match(r'^[\s]*[-*+]\s', line) or re.match(r'^[\s]*\d+\.\s', line):
            return self._format_list_item(line)
        
        # Horizontal rules
        if re.match(r'^[\s]*-{3,}[\s]*$', stripped) or re.match(r'^[\s]*\*{3,}[\s]*$', stripped):
            return self._format_horizontal_rule()
        
        # Regular paragraph
        return self._format_paragraph(line)
    
    def _format_header(self, line: str) -> str:
        """Format header lines"""
        stripped = line.strip()
        level = 0
        while level < len(stripped) and stripped[level] == '#':
            level += 1
        
        header_text = stripped[level:].strip()
        
        if self.max_mode:
            return self._format_header_max(header_text, level)
        else:
            return self._format_header_normal(header_text, level)
    
    def _format_header_normal(self, header_text: str, level: int) -> str:
        """Format header lines in normal mode"""
        formatted_text = self._format_inline_elements(header_text)
        
        # Add decorative elements based on header level
        if level == 1:
            border = '═' * (len(header_text) + 4)
            return f"{self.theme.border_color}{border}{self.reset}\n{self.theme.header_color}  {formatted_text}  {self.reset}\n{self.theme.border_color}{border}{self.reset}"
        elif level == 2:
            border = '─' * (len(header_text) + 2)
            return f"{self.theme.border_color}{border}{self.reset}\n{self.theme.header_color} {formatted_text} {self.reset}\n{self.theme.border_color}{border}{self.reset}"
        else:
            prefix = '▶' if level == 3 else '•'
            return f"{self.theme.header_color}{prefix} {formatted_text}{self.reset}"
    
    def _format_header_max(self, header_text: str, level: int) -> str:
        """Format header lines in max mode with ASCII art"""
        # Use different ASCII art based on header level
        if level == 1:
            # Large ASCII art for H1
            ascii_lines = generate_ascii_art(header_text, 'large')
            # Add multiple color layers for extra flair
            colors = [
                ANSIColors.BRIGHT_YELLOW + ANSIColors.BOLD,
                ANSIColors.BRIGHT_MAGENTA + ANSIColors.BOLD,
                ANSIColors.BRIGHT_CYAN + ANSIColors.BOLD,
            ]
            
            # Create border with gradient effect
            border_width = max(len(line) for line in ascii_lines) + 4
            top_border = f"{ANSIColors.BRIGHT_YELLOW}╔{'═' * border_width}╗{self.reset}"
            bottom_border = f"{ANSIColors.BRIGHT_YELLOW}╚{'═' * border_width}╝{self.reset}"
            
            result = [top_border]
            for i, line in enumerate(ascii_lines):
                color = colors[i % len(colors)]
                padded_line = line.ljust(border_width)
                result.append(f"{ANSIColors.BRIGHT_YELLOW}║{color}{padded_line}{ANSIColors.BRIGHT_YELLOW}║{self.reset}")
            result.append(bottom_border)
            
            return '\n'.join(result)
            
        elif level == 2:
            # Medium ASCII art for H2
            ascii_lines = generate_ascii_art(header_text, 'small')
            colors = [
                ANSIColors.BRIGHT_CYAN + ANSIColors.BOLD,
                ANSIColors.BRIGHT_BLUE + ANSIColors.BOLD,
            ]
            
            border_width = max(len(line) for line in ascii_lines) + 2
            top_border = f"{ANSIColors.BRIGHT_CYAN}┌{'─' * border_width}┐{self.reset}"
            bottom_border = f"{ANSIColors.BRIGHT_CYAN}└{'─' * border_width}┘{self.reset}"
            
            result = [top_border]
            for i, line in enumerate(ascii_lines):
                color = colors[i % len(colors)]
                padded_line = line.ljust(border_width)
                result.append(f"{ANSIColors.BRIGHT_CYAN}│{color}{padded_line}{ANSIColors.BRIGHT_CYAN}│{self.reset}")
            result.append(bottom_border)
            
            return '\n'.join(result)
            
        else:
            # Enhanced regular headers for H3+
            decorative_chars = ['◆', '◇', '◈', '◉', '◎']
            char = decorative_chars[level % len(decorative_chars)]
            enhanced_colors = [
                ANSIColors.BRIGHT_GREEN + ANSIColors.BOLD,
                ANSIColors.BRIGHT_YELLOW + ANSIColors.BOLD,
                ANSIColors.BRIGHT_MAGENTA + ANSIColors.BOLD,
                ANSIColors.BRIGHT_RED + ANSIColors.BOLD,
            ]
            color = enhanced_colors[level % len(enhanced_colors)]
            
            # Add some decorative elements
            decoration = '▸' * (level - 2)
            formatted_text = self._format_inline_elements(header_text)
            
            return f"{color}{decoration}{char} {formatted_text} {char}{decoration}{self.reset}"
    
    def _format_blockquote(self, line: str) -> str:
        """Format blockquote lines"""
        content = line.strip()[1:].strip()
        formatted_content = self._format_inline_elements(content)
        
        if self.max_mode:
            # Enhanced blockquote with more decorative elements
            decorative_chars = ['┃', '┋', '┊', '│', '║']
            colors = [
                ANSIColors.BRIGHT_MAGENTA + ANSIColors.BOLD,
                ANSIColors.BRIGHT_CYAN + ANSIColors.BOLD,
                ANSIColors.BRIGHT_YELLOW + ANSIColors.BOLD,
            ]
            char = decorative_chars[hash(content) % len(decorative_chars)]
            color = colors[hash(content) % len(colors)]
            return f"{color}{char} {formatted_content}{self.reset}"
        else:
            return f"{self.theme.quote_color}┃ {formatted_content}{self.reset}"
    
    def _format_list_item(self, line: str) -> str:
        """Format list item lines"""
        # Determine indentation level
        indent_match = re.match(r'^(\s*)', line)
        indent = len(indent_match.group(1)) if indent_match else 0
        
        # Get list marker and content
        content_match = re.match(r'^[\s]*[-*+]\s(.*)$', line)
        if not content_match:
            content_match = re.match(r'^[\s]*\d+\.\s(.*)$', line)
        
        if content_match:
            content = content_match.group(1)
            formatted_content = self._format_inline_elements(content)
            
            if self.max_mode:
                # Enhanced list items with more decorative bullets
                decorative_bullets = ['◆', '◇', '◈', '◉', '◎', '●', '○', '◐', '◑', '◒', '◓']
                colors = [
                    ANSIColors.BRIGHT_RED + ANSIColors.BOLD,
                    ANSIColors.BRIGHT_GREEN + ANSIColors.BOLD,
                    ANSIColors.BRIGHT_BLUE + ANSIColors.BOLD,
                    ANSIColors.BRIGHT_YELLOW + ANSIColors.BOLD,
                    ANSIColors.BRIGHT_MAGENTA + ANSIColors.BOLD,
                    ANSIColors.BRIGHT_CYAN + ANSIColors.BOLD,
                ]
                
                bullet_index = (indent // 2) % len(decorative_bullets)
                color_index = (indent // 2) % len(colors)
                bullet = decorative_bullets[bullet_index]
                color = colors[color_index]
                
                return f"{' ' * indent}{color}{bullet} {formatted_content}{self.reset}"
            else:
                bullet = '•' if indent == 0 else '◦'
                return f"{' ' * indent}{self.theme.list_color}{bullet} {formatted_content}{self.reset}"
        
        return line
    
    def _format_horizontal_rule(self) -> str:
        """Format horizontal rule"""
        if self.max_mode:
            # Enhanced horizontal rule with gradient effect
            chars = ['▀', '▄', '█', '▌', '▐', '░', '▒', '▓']
            colors = [
                ANSIColors.BRIGHT_RED,
                ANSIColors.BRIGHT_YELLOW,
                ANSIColors.BRIGHT_GREEN,
                ANSIColors.BRIGHT_CYAN,
                ANSIColors.BRIGHT_BLUE,
                ANSIColors.BRIGHT_MAGENTA,
            ]
            
            rule_parts = []
            for i in range(80):
                char = chars[i % len(chars)]
                color = colors[i % len(colors)]
                rule_parts.append(f"{color}{char}")
            
            return ''.join(rule_parts) + self.reset
        else:
            return f"{self.theme.border_color}{'─' * 60}{self.reset}"
    
    def _format_paragraph(self, line: str) -> str:
        """Format regular paragraph text"""
        if not line.strip():
            return ''
        
        formatted_line = self._format_inline_elements(line)
        return f"{self.theme.text_color}{formatted_line}{self.reset}"
    
    def _format_inline_elements(self, text: str) -> str:
        """Format inline markdown elements (bold, italic, code, links)"""
        if not text:
            return ''
        
        if self.max_mode:
            # Enhanced inline formatting with more colors and effects
            # Bold text (**text** or __text__)
            text = re.sub(r'\*\*([^*]+)\*\*', f'{ANSIColors.BRIGHT_YELLOW + ANSIColors.BOLD + ANSIColors.BLINK}\\1{self.theme.text_color}', text)
            text = re.sub(r'__([^_]+)__', f'{ANSIColors.BRIGHT_YELLOW + ANSIColors.BOLD + ANSIColors.BLINK}\\1{self.theme.text_color}', text)
            
            # Italic text (*text* or _text_)
            text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', f'{ANSIColors.BRIGHT_MAGENTA + ANSIColors.ITALIC + ANSIColors.UNDERLINE}\\1{self.theme.text_color}', text)
            text = re.sub(r'(?<!_)_([^_]+)_(?!_)', f'{ANSIColors.BRIGHT_MAGENTA + ANSIColors.ITALIC + ANSIColors.UNDERLINE}\\1{self.theme.text_color}', text)
            
            # Inline code (`code`)
            text = re.sub(r'`([^`]+)`', f'{ANSIColors.BRIGHT_GREEN + ANSIColors.BOLD + ANSIColors.BG_BLACK}\\1{self.theme.text_color}', text)
            
            # Links [text](url)
            text = re.sub(r'\[([^\]]+)\]\([^)]+\)', f'{ANSIColors.BRIGHT_CYAN + ANSIColors.UNDERLINE + ANSIColors.BLINK}\\1{self.theme.text_color}', text)
        else:
            # Normal formatting
            # Bold text (**text** or __text__)
            text = re.sub(r'\*\*([^*]+)\*\*', f'{self.theme.strong_color}\\1{self.theme.text_color}', text)
            text = re.sub(r'__([^_]+)__', f'{self.theme.strong_color}\\1{self.theme.text_color}', text)
            
            # Italic text (*text* or _text_)
            text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', f'{self.theme.emphasis_color}\\1{self.theme.text_color}', text)
            text = re.sub(r'(?<!_)_([^_]+)_(?!_)', f'{self.theme.emphasis_color}\\1{self.theme.text_color}', text)
            
            # Inline code (`code`)
            text = re.sub(r'`([^`]+)`', f'{self.theme.code_color}\\1{self.theme.text_color}', text)
            
            # Links [text](url)
            text = re.sub(r'\[([^\]]+)\]\([^)]+\)', f'{self.theme.link_color}\\1{self.theme.text_color}', text)
        
        return text
    
    def _format_code_block_start(self, lang: str) -> str:
        """Format start of code block"""
        lang_display = f" ({lang})" if lang else ""
        
        if self.max_mode:
            # Enhanced code block borders
            border_chars = ['╔', '╗', '╠', '╣', '╚', '╝', '═', '║']
            colors = [
                ANSIColors.BRIGHT_GREEN + ANSIColors.BOLD,
                ANSIColors.BRIGHT_CYAN + ANSIColors.BOLD,
                ANSIColors.BRIGHT_YELLOW + ANSIColors.BOLD,
            ]
            
            color = colors[hash(lang) % len(colors)]
            border = '═' * (50 - len(lang_display))
            return f"{color}╔─ CODE{lang_display} ─{border}╗{self.reset}"
        else:
            return f"{self.theme.border_color}┌─ CODE{lang_display} ─{'─' * (50 - len(lang_display))}{self.reset}"
    
    def _format_code_block_end(self) -> str:
        """Format end of code block"""
        if self.max_mode:
            colors = [
                ANSIColors.BRIGHT_GREEN + ANSIColors.BOLD,
                ANSIColors.BRIGHT_CYAN + ANSIColors.BOLD,
                ANSIColors.BRIGHT_YELLOW + ANSIColors.BOLD,
            ]
            color = colors[0]  # Use consistent color
            return f"{color}╚{'═' * 60}╝{self.reset}"
        else:
            return f"{self.theme.border_color}└─{'─' * 58}{self.reset}"
    
    def _format_code_line(self, line: str) -> str:
        """Format a line inside a code block"""
        if self.max_mode:
            colors = [
                ANSIColors.BRIGHT_GREEN + ANSIColors.BOLD,
                ANSIColors.BRIGHT_CYAN + ANSIColors.BOLD,
                ANSIColors.BRIGHT_YELLOW + ANSIColors.BOLD,
            ]
            border_color = colors[0]
            return f"{border_color}║{self.reset} {self.theme.code_color}{line}{self.reset}"
        else:
            return f"{self.theme.border_color}│{self.reset} {self.theme.code_color}{line}{self.reset}"