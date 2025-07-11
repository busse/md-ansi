#!/usr/bin/env python3
"""
Command-line interface for md-ansi
"""

import argparse
import sys
from pathlib import Path
from .converter import MarkdownToANSIConverter
from .styles import THEMES


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Convert Markdown files to BBS-style ANSI documents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Available styles:
  beach      - Ocean blues, sandy yellows, tropical colors
  vaporwave  - Pink, purple, cyan, retro aesthetic  
  edgelord   - Black, red, dark colors, gothic feel
  rainbow    - Full spectrum colors
  helvetica  - Clean, minimal, black/white/gray
  codc       - Cult of the Dead Cow hacker aesthetic

Examples:
  %(prog)s README.md
  %(prog)s --style vaporwave document.md
  %(prog)s --style codc --output output.ans input.md
        '''
    )
    
    parser.add_argument(
        'input',
        nargs='?',
        help='Input markdown file (use "-" for stdin)'
    )
    
    parser.add_argument(
        '--style',
        choices=list(THEMES.keys()),
        default='beach',
        help='Style theme to use (default: beach)'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output file (default: stdout)'
    )
    
    parser.add_argument(
        '--list-styles',
        action='store_true',
        help='List available styles and exit'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 0.1.0'
    )
    
    args = parser.parse_args()
    
    if args.list_styles:
        print("Available styles:")
        for name, theme in THEMES.items():
            print(f"  {name:12} - {get_style_description(name)}")
        return
    
    if not args.input:
        parser.error("input is required unless using --list-styles")
    
    # Read input
    try:
        if args.input == '-':
            content = sys.stdin.read()
        else:
            input_path = Path(args.input)
            if not input_path.exists():
                print(f"Error: File '{args.input}' not found", file=sys.stderr)
                sys.exit(1)
            content = input_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Convert
    try:
        converter = MarkdownToANSIConverter(args.style)
        result = converter.convert(content)
    except Exception as e:
        print(f"Error converting content: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Output
    try:
        if args.output:
            output_path = Path(args.output)
            output_path.write_text(result, encoding='utf-8')
            print(f"Output written to {args.output}")
        else:
            print(result)
    except Exception as e:
        print(f"Error writing output: {e}", file=sys.stderr)
        sys.exit(1)


def get_style_description(style_name):
    """Get description for a style"""
    descriptions = {
        'beach': 'Ocean blues, sandy yellows, tropical colors',
        'vaporwave': 'Pink, purple, cyan, retro aesthetic',
        'edgelord': 'Black, red, dark colors, gothic feel',
        'rainbow': 'Full spectrum colors',
        'helvetica': 'Clean, minimal, black/white/gray',
        'codc': 'Cult of the Dead Cow hacker aesthetic'
    }
    return descriptions.get(style_name, 'Unknown style')


if __name__ == '__main__':
    main()