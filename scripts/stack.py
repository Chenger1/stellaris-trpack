from dataclasses import dataclass, field
from typing import List, Optional


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, value: str):
        self._stack.append(value)

    def pop(self) -> Optional[str]:
        return self._stack.pop() if self._stack else None

    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def clean(self):
        self._stack.clear()

    def get_last_elem(self) -> Optional[str]:
        return self._stack[-1] if self._stack else None


class LastParentStack(Stack):
    def get_full_path(self, new_key: str) -> str:
        parent_full_path = self._stack[-1].full_path.strip() if self._stack else None
        return f'{parent_full_path}/{new_key}' if parent_full_path else f'{new_key}'

    def get_parent_key(self) -> Optional[str]:
        return self._stack[-1].key if self._stack else None


@dataclass
class NameListElement:
    key: str
    index: int
    parent_key: 'NameListElement'
    full_path: str
    children: List['NameListElement'] = field(default_factory=list)
    value: str = None
