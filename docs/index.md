# Library Movies Top List

Creates a Library Movies Top List.

## Installation

Install using pip:

```bash
pip install lib_mov_top_list
```

Or using uv (recommended):

```bash
uv add lib_mov_top_list
```

## Quick Start

```python
import lib_mov_top_list

print(lib_mov_top_list.__version__)
```

## Development

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) for package management

### Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/heidenbloed/lib-mov-top-list.git
cd lib-mov-top-list
uv sync --group dev
```

### Running Tests

```bash
uv run pytest
```

### Code Quality

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run ty check
```

### Prek Hooks

Install prek hooks:

```bash
prek install
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/heidenbloed/lib-mov-top-list/blob/main/LICENSE) file for details.
