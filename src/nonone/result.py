from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Callable, Any, TypeAlias, NoReturn, ParamSpec
import functools

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")
F = TypeVar("F")
P = ParamSpec("P")  # 用于保留装饰器参数签名


class UnwrapError(RuntimeError):
    """统一抛出的解包异常。"""


# -------------------- 成功分支 --------------------
@dataclass(frozen=True, slots=True)
class Ok(Generic[T, E]):
    value: T

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False

    def unwrap(self) -> T:
        return self.value

    def unwrap_err(self) -> NoReturn:
        raise UnwrapError(f"Called unwrap_err() on an Ok: {self.value!r}")

    def unwrap_or(self, default: T) -> T:
        return self.value

    def unwrap_or_else(self, op: Callable[[E], T]) -> T:
        return self.value

    def expect(self, msg: str) -> T:
        return self.value

    def map(self, f: Callable[[T], U]) -> Ok[U, E]:
        return Ok(f(self.value))

    def map_err(self, f: Callable[[E], F]) -> Ok[T, F]:
        return Ok(self.value)

    def and_then(self, f: Callable[[T], Result[U, E]]) -> Result[U, E]:
        return f(self.value)
    
    def try_and_then(self, f: Callable[[T], U]) -> Result[U, Exception]:
        return try_catch(f, self.value)  # 用于处理不是返回 Result 的函数

    def inspect(self, func: Callable[[T], Any]) -> Ok[T, E]:
        """对 Ok 值执行副作用函数（如打印），返回自身。类似 Rust 的 inspect()。"""
        func(self.value)
        return self
    
    def or_else(self, f: Callable[[E], Result[T, F]]) -> Result[T, F]:
        return Ok(self.value)


# -------------------- 失败分支 --------------------
@dataclass(frozen=True, slots=True)
class Err(Generic[T, E]):
    error: E

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True

    def unwrap(self) -> T:
        raise UnwrapError(f"Called unwrap() on an Err: {self.error!r}")

    def unwrap_err(self) -> E:
        return self.error

    def unwrap_or(self, default: T) -> T:
        return default

    def unwrap_or_else(self, op: Callable[[E], T]) -> T:
        return op(self.error)

    def expect(self, msg: str) -> NoReturn:
        raise UnwrapError(f"{msg}: {self.error!r}")

    def map(self, f: Callable[[T], U]) -> Err[U, E]:
        return Err(self.error)

    def map_err(self, f: Callable[[E], F]) -> Err[T, F]:
        return Err(f(self.error))

    def and_then(self, f: Callable[[T], Result[U, E]]) -> Result[U, E]:
        return Err(self.error)
    
    def try_and_then(self, f: Callable[[T], U]) -> Result[U, Exception | E]:
        return Err(self.error)
        # return cast(Any, self)  # 强制将当前实例视为目标返回类型

    def or_else(self, f: Callable[[E], Result[T, F]]) -> Result[T, F]:
        return f(self.error)
    
    def inspect(self, func: Callable[[E], Any]) -> Err[T, E]:
        """对 Err 错误执行副作用函数（如打印），返回自身。类似 Rust 的 inspect_err()。"""
        func(self.error)
        return self

# -------------------- 联合类型别名 --------------------
Result: TypeAlias = Ok[T, E] | Err[T, E]


# -------------------- 辅助构造器 --------------------
def ok(value: T) -> Ok[T, Any]:
    """小写构造器，返回 Ok[T, Any]（错误类型留作 Any）。"""
    return Ok(value)


def err(error: E) -> Err[Any, E]:
    """小写构造器，返回 Err[Any, E]（成功类型留作 Any）。"""
    return Err(error)


# -------------------- 装饰器：将普通函数变为返回 Result 的函数 --------------------
def catch(func: Callable[P, T]) -> Callable[P, Result[T, Exception]]:
    """
    装饰器。自动捕获异常并返回 Result。
    利用 ParamSpec 完美保留了原函数的参数类型提示。
    """
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Result[T, Exception]:
        try:
            return Ok(func(*args, **kwargs))
        except Exception as e:
            return Err(e)
    return wrapper


# -------------------- 函数式调用：立即执行函数并返回 Result --------------------
def try_catch(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> Result[T, Exception]:
    """手动调用：立即执行函数并返回 Result。"""
    try:
        return Ok(func(*args, **kwargs))
    except Exception as e:
        return Err(e)