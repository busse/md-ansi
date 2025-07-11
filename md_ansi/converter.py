"""
Core markdown to ANSI converter
"""

import re
from typing import List, Tuple
from .styles import ANSIColors, get_theme


class MarkdownToANSIConverter:
    """Convert markdown to ANSI-formatted text"""
    
    def __init__(self, style_name='beach'):
        self.theme = get_theme(style_name)
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
    
    def _format_blockquote(self, line: str) -> str:
        """Format blockquote lines"""
        content = line.strip()[1:].strip()
        formatted_content = self._format_inline_elements(content)
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
            bullet = '•' if indent == 0 else '◦'
            return f"{' ' * indent}{self.theme.list_color}{bullet} {formatted_content}{self.reset}"
        
        return line
    
    def _format_horizontal_rule(self) -> str:
        """Format horizontal rule"""
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
        return f"{self.theme.border_color}┌─ CODE{lang_display} ─{'─' * (50 - len(lang_display))}{self.reset}"
    
    def _format_code_block_end(self) -> str:
        """Format end of code block"""
        return f"{self.theme.border_color}└─{'─' * 58}{self.reset}"
    
    def _format_code_line(self, line: str) -> str:
        """Format a line inside a code block"""
        return f"{self.theme.border_color}│{self.reset} {self.theme.code_color}{line}{self.reset}"