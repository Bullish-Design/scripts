"""Scripts package.

Copier template structure to quickly generate uv scripts
"""

from __future__ import annotations

from scripts._internal.cli import get_parser, main

__all__: list[str] = ["get_parser", "main"]
