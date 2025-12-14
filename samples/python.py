from __future__ import annotations

# --- Imports (добавлены, чтобы твой пример был самодостаточным) ---
from dataclasses import dataclass, field
from enum import Enum, IntEnum
from typing import (
    Any,
    Callable,
    ClassVar,
    Final,
    Generic,
    Iterable,
    Iterator,
    List,
    Literal,
    Optional,
    Protocol,
    TypeAlias,
    TypeVar,
    runtime_checkable,
)

import abc
import functools
import pathlib

# --- Compatibility helper for @override (Python 3.12+) ---
try:
    from typing import override
except ImportError:  # pragma: no cover
    def override(fn):  # type: ignore[misc]
        return fn


# --- Type parameters / type alias (PEP 695 coverage) ---
T = TypeVar("T")
P = TypeVar("P")

type JsonScalar = str | int | float | bool | None
type JsonValue = JsonScalar | list["JsonValue"] | dict[str, "JsonValue"]

# typeHintComment coverage:
legacy_hint = 123  # type: int


# --- Constants / readonly modifier coverage ---
DEBUG: Final[bool] = True
MAX_RETRIES: Final[int] = 3
APP_NAME: Final[str] = "semantic-tokens-demo"

# A module symbol to exercise "module" token references:
HERE = pathlib.Path(__file__).resolve()


# --- Decorator coverage (your sample uses @decorator(param=1)) ---
def decorator(*, param: int = 0) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Simple decorator factory. Used by the JetBrains sample below."""
    def _wrap(fn: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(fn)
        def inner(*args: Any, **kwargs: Any) -> Any:
            if DEBUG and param:
                _ = len(args) + len(kwargs)  # builtin modifier likely on len
            return fn(*args, **kwargs)
        return inner
    return _wrap


# --- Enum / enumMember tokens ---
class Status(Enum):
    OK = "ok"
    NOT_FOUND = "not_found"
    ERROR = "error"


class HttpCode(IntEnum):
    OK = 200
    NOT_FOUND = 404


# --- Protocol / abstract / overridden modifiers ---
@runtime_checkable
class Closable(Protocol):
    def close(self) -> None: ...


class Base(abc.ABC):
    kind: ClassVar[str] = "base"  # static modifier may apply to ClassVar

    @abc.abstractmethod
    def run(self, value: int) -> str:  # abstract + typeHint on annotations
        """Must be implemented."""


class Child(Base):
    @override
    def run(self, value: int) -> str:  # overridden modifier target
        return f"Child({value})"


# --- property / member / magicFunction / callable coverage ---
@dataclass
class Widget(Generic[T]):
    name: str
    items: list[T] = field(default_factory=list)

    @property
    def size(self) -> int:  # property token on "size"
        return len(self.items)

    @functools.cached_property
    def slug(self) -> str:
        return self.name.lower().replace(" ", "-")

    @staticmethod
    def parse(raw: str) -> "Widget[str]":  # static modifier target
        w = Widget[str](name=raw)
        w.items.append(raw)
        return w

    @classmethod
    def empty(cls) -> "Widget[Any]":  # clsParameter token on "cls"
        return cls(name="")

    def __len__(self) -> int:  # magicFunction (dunder)
        return self.size

    def __iter__(self) -> Iterator[T]:  # magicFunction
        return iter(self.items)

    def __call__(self, x: T) -> None:  # magicFunction + callable instances
        self.items.append(x)


# callable modifier on variables (function + callable instance):
def plus_one(x: int) -> int:
    return x + 1

callable_fn = plus_one
callable_obj = Widget[int]("callable-widget")


# async modifier coverage
async def fetch(value: int) -> int:
    await _sleep0()
    return value + 1

async def _sleep0() -> None:
    return None


# -------------------- YOUR ORIGINAL JETBRAINS SAMPLE (kept as-is) --------------------
@decorator(param=1)
def f(x):
    """
    Syntax Highlighting Demo
    @param x Parameter

    Semantic highlighting:
    Generated spectrum to pick colors for local variables and parameters:
     Color#1 SC1.1 SC1.2 SC1.3 SC1.4 Color#2 SC2.1 SC2.2 SC2.3 SC2.4 Color#3
     Color#3 SC3.1 SC3.2 SC3.3 SC3.4 Color#4 SC4.1 SC4.2 SC4.3 SC4.4 Color#5
    """

    def nested_func(y):
        print(y + 1)

    s = ("Test", 2+3, {'a': 'b'}, f'{x!s:{"^10"}}')   # Comment
    f(s[0].lower())
    nested_func(42)

class Foo:
    tags: List[str]

    def __init__(self: Foo):
        byte_string: bytes = b'newline:\n also newline:\x0a'
        text_string = u"Cyrillic Я is \u042f. Oops: \u042g"
        self.make_sense(whatever=1)
    
    def make_sense[T](self, whatever: T):
        self.sense = whatever

x = len('abc')

# Original line had a syntax typo that breaks parsing and semantic tokens:
# type my_int< = int
type my_int = int

print(f.__doc__)
# -------------------------------------------------------------------------------


# Extra: module usage + intrinsic/builtin references in one place
def use_everything() -> JsonValue:
    w = Widget.parse("Hello World")
    w(123)
    _ = Status.OK
    _ = HttpCode.NOT_FOUND
    _ = x.__class__

    _ = callable_fn(41)
    _ = callable_obj.size
    _ = HERE.name
    return {"ok": True, "name": APP_NAME, "n": 1, "s": "x"}

if __name__ == "__main__":
    print("hello")

# --- Dunder attribute / "special runtime attribute" probe block ---
# (Use "Developer: Inspect Editor Tokens and Scopes" on each identifier)

# Function/object dunder attributes (likely similar behavior to __doc__)
_doc = f.__doc__
_name = f.__name__
_qual = f.__qualname__
_mod = f.__module__
_ann = f.__annotations__
_defaults = f.__defaults__
_kwdefaults = f.__kwdefaults__
_code = f.__code__
_dict = f.__dict__
_class = f.__class__

# Module-level special names (often treated differently by analyzers)
_this_name = __name__
_this_file = __file__
_this_pkg = __package__
_this_debug = __debug__
_this_builtins = __builtins__

# Common object dunders to compare
_widget = Widget[int]("probe")
_widget_class = _widget.__class__
_widget_dict = _widget.__dict__
_widget_module = _widget.__module__

# Some module-ish dunders that exist in many contexts (may be None / absent)
_spec = getattr(pathlib, "__spec__", None)
_loader = getattr(pathlib, "__loader__", None)
_package = getattr(pathlib, "__package__", None)
_all = getattr(pathlib, "__all__", None)

print(_doc, _name, _qual, _mod, _ann, _defaults, _kwdefaults, _code)
print(_this_name, _this_file, _this_pkg, _this_debug, type(_this_builtins))
print(_widget_class, _widget_dict, _widget_module, _spec, _loader, _package, _all)
