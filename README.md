# Library Movies Top List

[![CI](https://github.com/heidenbloed/lib-mov-top-list/actions/workflows/ci.yml/badge.svg)](https://github.com/heidenbloed/lib-mov-top-list/actions/workflows/ci.yml)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/badge/type--checked-ty-blue?labelColor=orange)](https://github.com/astral-sh/ty)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/heidenbloed/lib-mov-top-list/blob/main/LICENSE)

Creates a Library Movies Top List.

## Features

- Fast and modern Python toolchain using Astral's tools (uv, ruff, ty)
- Type-safe with full type annotations

## Installation

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

```bash
git clone https://github.com/heidenbloed/lib-mov-top-list.git
cd lib-mov-top-list
make install
```

### Running Tests

```bash
make test

# With coverage
make test-cov

# Across all Python versions
make test-matrix
```

### Code Quality

```bash
# Run all checks (lint, format, type-check)
make verify

# Auto-fix lint and format issues
make fix
```

### Prek

```bash
prek install
prek run --all-files
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
