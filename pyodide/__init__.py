from typing import Any

__version__ = "0.20.0"


def eval_code(
        source: str,
        globals: dict[str, Any] | None = None,
        locals: dict[str, Any] | None = None,
        *,
        return_mode: str = "last_expr",
        quiet_trailing_semicolon: bool = True,
        filename: str = "<exec>",
        flags: int = 0x0,
) -> Any:
    pass


__all__ = [
    "http",
    "eval_code"
]
