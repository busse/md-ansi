# md-ansi

Convert Markdown files to BBS-style ANSI documents with colorful formatting reminiscent of classic bulletin board systems.

## Installation

```bash
pip install -e .
```

Or use directly:

```bash
./md-ansi input.md
```

## Usage

### Basic Usage

```bash
# Convert a markdown file with default beach style
md-ansi README.md

# Use a specific style
md-ansi --style vaporwave document.md

# Use max mode for enhanced formatting with ASCII art headers
md-ansi --max --style edgelord document.md

# Save to file
md-ansi --style codc --output output.ans input.md

# Read from stdin
cat input.md | md-ansi --style edgelord -
```

### Available Styles

- **beach** - Ocean blues, sandy yellows, tropical colors
- **vaporwave** - Pink, purple, cyan, retro aesthetic
- **edgelord** - Black, red, dark colors, gothic feel
- **rainbow** - Full spectrum colors
- **helvetica** - Clean, minimal, black/white/gray
- **codc** - Cult of the Dead Cow hacker aesthetic
- **topgun** - Military/aviation BBS aesthetic, bright contrasting colors

### Command Line Options

```
usage: md-ansi [-h] [--style {beach,vaporwave,edgelord,rainbow,helvetica,codc,topgun}] 
               [--output OUTPUT] [--max] [--list-styles] [--version] [input]

Convert Markdown files to BBS-style ANSI documents

positional arguments:
  input                 Input markdown file (use "-" for stdin)

options:
  -h, --help            show this help message and exit
  --style STYLE         Style theme to use (default: beach)
  --output OUTPUT, -o OUTPUT
                        Output file (default: stdout)
  --max                 Enhanced formatting with ASCII art headers and wilder colors
  --list-styles         List available styles and exit
  --version             show program's version number and exit
```

## Features

- **Headers** - Styled with decorative borders, ASCII art in max mode
- **Text formatting** - Bold, italic, inline code with enhanced effects in max mode
- **Links** - Underlined and colored, with blinking effects in max mode
- **Lists** - Bullet points and numbered lists with nesting, enhanced bullets in max mode
- **Code blocks** - Syntax-highlighted with language labels, enhanced borders in max mode
- **Blockquotes** - Formatted with side borders, variable characters in max mode
- **Horizontal rules** - Decorative separators, rainbow gradients in max mode
- **Max mode** - Enhanced formatting with ASCII art headers and wilder colors
- **Minimal dependencies** - Uses only Python standard library

## Examples

### Beach Style
Perfect for that tropical, laid-back documentation vibe.

### Vaporwave Style
Embrace the retro-futuristic aesthetic with pink and cyan colors.

### Edgelord Style
Dark and dramatic formatting for that gothic documentation feel.

### Rainbow Style
Full spectrum of colors for maximum visual impact.

### Helvetica Style
Clean, minimal black and white styling for professional documents.

### CODC Style
Green-on-black hacker aesthetic inspired by the Cult of the Dead Cow.

### Top Gun Style
Military/aviation BBS aesthetic with bright contrasting colors reminiscent of 1990s Top Gun themed bulletin board systems.

## License

MIT License
