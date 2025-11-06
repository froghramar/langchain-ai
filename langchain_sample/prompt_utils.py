"""Small pure-Python helpers for prompt construction.

These are intentionally network-free so they can be unit-tested quickly.
"""

from typing import List


def build_translate_prompt(text: str, target_language: str = "French") -> str:
    """Return a simple prompt asking to translate `text` to `target_language`."""
    if text is None:
        raise ValueError("text must not be None")
    return f"Translate to {target_language}: {text}"


def bullet_points_prompt(items: List[str]) -> str:
    """Return a prompt that asks the model to turn a list into bullet points."""
    if items is None:
        raise ValueError("items must not be None")
    joined = "\n".join(f"- {i}" for i in items)
    return f"Turn the following into a clean bullet list:\n{joined}"
