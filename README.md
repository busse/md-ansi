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

### Command Line Options

```
usage: md-ansi [-h] [--style {beach,vaporwave,edgelord,rainbow,helvetica,codc}] 
               [--output OUTPUT] [--list-styles] [--version] [input]

Convert Markdown files to BBS-style ANSI documents

positional arguments:
  input                 Input markdown file (use "-" for stdin)

options:
  -h, --help            show this help message and exit
  --style STYLE         Style theme to use (default: beach)
  --output OUTPUT, -o OUTPUT
                        Output file (default: stdout)
  --list-styles         List available styles and exit
  --version             show program's version number and exit
```

## Features

- **Headers** - Styled with decorative borders
- **Text formatting** - Bold, italic, inline code
- **Links** - Underlined and colored
- **Lists** - Bullet points and numbered lists with nesting
- **Code blocks** - Syntax-highlighted with language labels
- **Blockquotes** - Formatted with side borders
- **Horizontal rules** - Decorative separators
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

## License

MIT License
