"""
ANSI Style definitions for different themes
"""

class ANSIColors:
    """ANSI color codes"""
    # Reset
    RESET = '\033[0m'
    
    # Regular colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Text styles
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'


class StyleTheme:
    """Base class for style themes"""
    def __init__(self, name):
        self.name = name
        self.header_color = ANSIColors.WHITE
        self.text_color = ANSIColors.WHITE
        self.emphasis_color = ANSIColors.YELLOW
        self.strong_color = ANSIColors.RED
        self.code_color = ANSIColors.GREEN
        self.link_color = ANSIColors.BLUE
        self.list_color = ANSIColors.CYAN
        self.quote_color = ANSIColors.MAGENTA
        self.border_color = ANSIColors.WHITE
        self.background_color = ''


class BeachTheme(StyleTheme):
    """Beach theme - ocean blues, sandy yellows, tropical colors"""
    def __init__(self):
        super().__init__("beach")
        self.header_color = ANSIColors.BRIGHT_CYAN + ANSIColors.BOLD
        self.text_color = ANSIColors.BLUE
        self.emphasis_color = ANSIColors.BRIGHT_YELLOW
        self.strong_color = ANSIColors.BRIGHT_BLUE + ANSIColors.BOLD
        self.code_color = ANSIColors.CYAN
        self.link_color = ANSIColors.BRIGHT_BLUE + ANSIColors.UNDERLINE
        self.list_color = ANSIColors.YELLOW
        self.quote_color = ANSIColors.BRIGHT_CYAN
        self.border_color = ANSIColors.BRIGHT_YELLOW


class VaporwaveTheme(StyleTheme):
    """Vaporwave theme - pink, purple, cyan, retro aesthetic"""
    def __init__(self):
        super().__init__("vaporwave")
        self.header_color = ANSIColors.BRIGHT_MAGENTA + ANSIColors.BOLD
        self.text_color = ANSIColors.BRIGHT_CYAN
        self.emphasis_color = ANSIColors.BRIGHT_MAGENTA + ANSIColors.ITALIC
        self.strong_color = ANSIColors.MAGENTA + ANSIColors.BOLD
        self.code_color = ANSIColors.CYAN + ANSIColors.BG_MAGENTA
        self.link_color = ANSIColors.BRIGHT_MAGENTA + ANSIColors.UNDERLINE
        self.list_color = ANSIColors.BRIGHT_CYAN
        self.quote_color = ANSIColors.MAGENTA + ANSIColors.ITALIC
        self.border_color = ANSIColors.BRIGHT_MAGENTA


class EdgelordTheme(StyleTheme):
    """Edgelord theme - black, red, dark colors, gothic feel"""
    def __init__(self):
        super().__init__("edgelord")
        self.header_color = ANSIColors.BRIGHT_RED + ANSIColors.BOLD
        self.text_color = ANSIColors.WHITE
        self.emphasis_color = ANSIColors.RED + ANSIColors.ITALIC
        self.strong_color = ANSIColors.BRIGHT_RED + ANSIColors.BOLD
        self.code_color = ANSIColors.BRIGHT_BLACK + ANSIColors.BG_RED
        self.link_color = ANSIColors.RED + ANSIColors.UNDERLINE
        self.list_color = ANSIColors.BRIGHT_BLACK
        self.quote_color = ANSIColors.RED + ANSIColors.ITALIC
        self.border_color = ANSIColors.BRIGHT_RED


class RainbowTheme(StyleTheme):
    """Rainbow theme - full spectrum colors"""
    def __init__(self):
        super().__init__("rainbow")
        self.header_color = ANSIColors.BRIGHT_RED + ANSIColors.BOLD
        self.text_color = ANSIColors.WHITE
        self.emphasis_color = ANSIColors.BRIGHT_YELLOW + ANSIColors.ITALIC
        self.strong_color = ANSIColors.BRIGHT_GREEN + ANSIColors.BOLD
        self.code_color = ANSIColors.BRIGHT_BLUE
        self.link_color = ANSIColors.BRIGHT_MAGENTA + ANSIColors.UNDERLINE
        self.list_color = ANSIColors.BRIGHT_CYAN
        self.quote_color = ANSIColors.YELLOW + ANSIColors.ITALIC
        self.border_color = ANSIColors.BRIGHT_WHITE


class HelveticaTheme(StyleTheme):
    """Helvetica theme - clean, minimal, black/white/gray"""
    def __init__(self):
        super().__init__("helvetica")
        self.header_color = ANSIColors.BRIGHT_WHITE + ANSIColors.BOLD
        self.text_color = ANSIColors.WHITE
        self.emphasis_color = ANSIColors.BRIGHT_WHITE + ANSIColors.ITALIC
        self.strong_color = ANSIColors.BRIGHT_WHITE + ANSIColors.BOLD
        self.code_color = ANSIColors.BRIGHT_BLACK + ANSIColors.BG_WHITE
        self.link_color = ANSIColors.BRIGHT_WHITE + ANSIColors.UNDERLINE
        self.list_color = ANSIColors.BRIGHT_BLACK
        self.quote_color = ANSIColors.BRIGHT_BLACK + ANSIColors.ITALIC
        self.border_color = ANSIColors.BRIGHT_WHITE


class CODCTheme(StyleTheme):
    """Cult of the Dead Cow theme - hacker aesthetic, green on black"""
    def __init__(self):
        super().__init__("codc")
        self.header_color = ANSIColors.BRIGHT_GREEN + ANSIColors.BOLD
        self.text_color = ANSIColors.GREEN
        self.emphasis_color = ANSIColors.BRIGHT_GREEN + ANSIColors.ITALIC
        self.strong_color = ANSIColors.BRIGHT_GREEN + ANSIColors.BOLD
        self.code_color = ANSIColors.BRIGHT_GREEN + ANSIColors.BG_BLACK
        self.link_color = ANSIColors.GREEN + ANSIColors.UNDERLINE
        self.list_color = ANSIColors.BRIGHT_GREEN
        self.quote_color = ANSIColors.GREEN + ANSIColors.ITALIC
        self.border_color = ANSIColors.BRIGHT_GREEN


# Theme registry
THEMES = {
    'beach': BeachTheme(),
    'vaporwave': VaporwaveTheme(),
    'edgelord': EdgelordTheme(),
    'rainbow': RainbowTheme(),
    'helvetica': HelveticaTheme(),
    'codc': CODCTheme()
}


def get_theme(name):
    """Get a theme by name"""
    return THEMES.get(name.lower(), THEMES['beach'])  # Default to beach theme