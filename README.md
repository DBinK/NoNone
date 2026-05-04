
<div align="center">

# NoNone

**拒绝隐式 None，拥抱 Rust 风格的显式错误处理**

[![zread](https://img.shields.io/badge/Ask_Zread-_.svg?style=flat&color=00b0aa&labelColor=000000&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQuOTYxNTYgMS42MDAxSDIuMjQxNTZDMS44ODgxIDEuNjAwMSAxLjYwMTU2IDEuODg2NjQgMS42MDE1NiAyLjI0MDFWNC45NjAxQzEuNjAxNTYgNS4zMTM1NiAxLjg4ODEgNS42MDAxIDIuMjQxNTYgNS42MDAxSDQuOTYxNTZDNS4zMTUwMiA1LjYwMDEgNS42MDE1NiA1LjMxMzU2IDUuNjAxNTYgNC45NjAxVjIuMjQwMUM1LjYwMTU2IDEuODg2NjQgNS4zMTUwMiAxLjYwMDEgNC45NjE1NiAxLjYwMDFaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00Ljk2MTU2IDEwLjM5OTlIMi4yNDE1NkMxLjg4ODEgMTAuMzk5OSAxLjYwMTU2IDEwLjY4NjQgMS42MDE1NiAxMS4wMzk5VjEzLjc1OTlDMS42MDE1NiAxNC4xMTM0IDEuODg4MSAxNC4zOTk5IDIuMjQxNTYgMTQuMzk5OUg0Ljk2MTU2QzUuMzE1MDIgMTQuMzk5OSA1LjYwMTU2IDE0LjExMzQgNS42MDE1NiAxMy43NTk5VjExLjAzOTlDNS42MDE1NiAxMC42ODY0IDUuMzE1MDIgMTAuMzk5OSA0Ljk2MTU2IDEwLjM5OTlaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik0xMy43NTg0IDEuNjAwMUgxMS4wMzg0QzEwLjY4NSAxLjYwMDEgMTAuMzk4NCAxLjg4NjY0IDEwLjM5ODQgMi4yNDAxVjQuOTYwMUMxMC4zOTg0IDUuMzEzNTYgMTAuNjg1IDUuNjAwMSAxMS4wMzg0IDUuNjAwMUgxMy43NTg0QzE0LjExMTkgNS42MDAxIDE0LjM5ODQgNS4zMTM1NiAxNC4zOTg0IDQuOTYwMVYyLjI0MDFDMTQuMzk4NCAxLjg4NjY0IDE0LjExMTkgMS42MDAxIDEzLjc1ODQgMS42MDAxWiIgZmlsbD0iI2ZmZiIvPgo8cGF0aCBkPSJNNCAxMkwxMiA0TDQgMTJaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00IDEyTDEyIDQiIHN0cm9rZT0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8L3N2Zz4K&logoColor=ffffff)](https://zread.ai/DBinK/rose)
[![CI](https://img.shields.io/github/actions/workflow/status/DBinK/nonone/publish_to_pypi.yml?branch=main&logo=githubactions&logoColor=white)](https://github.com/DBinK/nonone/actions)
[![PyPI version](https://img.shields.io/pypi/v/nonone.svg)](https://pypi.org/project/nonone/)
[![Python versions](https://img.shields.io/pypi/pyversions/nonone.svg)](https://pypi.org/project/nonone/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- [安装](#安装) • [快速上手](#快速上手) • [API参考](#进阶用法) -->

</div>
<div align="center">
  <!-- Keep these links. Translations will automatically update with the README. -->
  <a href="https://www.zdoc.app/DBinK/nonone?lang=en">English</a> | 
  <a href="https://www.zdoc.app/DBinK/nonone?lang=ja">日本語</a> | 
  <a href="https://www.zdoc.app/DBinK/nonone?lang=de">Deutsch</a> | 
  <a href="https://www.zdoc.app/DBinK/nonone?lang=es">Español</a> | 
  <a href="https://www.zdoc.app/DBinK/nonone?lang=fr">français</a> | 
  <a href="https://www.zdoc.app/DBinK/nonone?lang=ko">한국어</a> | 
  <a href="https://www.zdoc.app/DBinK/nonone?lang=pt">Português</a> | 
  <a href="https://www.zdoc.app/DBinK/nonone?lang=ru">Русский</a>
</div>

---

### 核心特性

* 🦀 **Rust 体验**: 将成熟的 `Result[T, E]` 模式带入 Python
* ⚡ **开发体验**: 提供 `@catch` 和 `try_catch` 无缝迁移旧代码
* 🛡️ **类型安全**: 深度集成类型注解，支持 `mypy` 和 `pyright`
* 🪶 **轻量高效**: 零依赖，使用 `dataclass` 和 `__slots__` 优化内存占用
* 🧩 **模式匹配**: 专为 Python 3.10+ `match-case` 优化

---


### 为什么选择 NoNone？告别 Python 错误处理的三大痛点

在传统的 Python 开发中，我们经常面临以下痛点：

#### 痛点 1：错误处理的缺失与运行时崩溃

> 💡 **完整示例代码：** [`examples/01_painpoint1_error_handling.py`](examples/01_painpoint1_error_handling.py)

**❌ 传统写法 - 无显式错误处理**
```python
def divide(a: float, b: float) -> float:
    return a / b
    # ✅ 极简，零开销
    # ❌ 除零时程序崩溃
    # 🎯 适用：确信 b!=0、快速原型、脚本

result = divide(10, 0)  # 💥 程序直接崩溃, 抛出 ZeroDivisionError
print(f"结果: {result}")
```

**❌ 传统写法 - 出错提前返回 None**
```python
def divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b

result = divide(10, 0)
print(result * 2)  # 💥 如果 result 是 None，这里会抛出 TypeError！
```

**✅ NoNone 写法 - 类型安全**
```python
from nonone import Result, ok, err, Ok, Err

def divide_safe(a: float, b: float) -> Result[float, str]:
    if b == 0:
        return err("除数不能为零")
    return ok(a / b)

result = divide_safe(10, 0)

# Python 解释器和 IDE 会强制你处理两种情况，无法忽略错误
match result:
    case Ok(value):
        print(f"结果: {value * 2}")  # ✅ 安全，value 一定存在
    case Err(msg):
        print(f"错误: {msg}")
```

---

#### 痛点 2：异常处理冗长且容易遗漏

> 💡 **完整示例代码：** [`examples/02_painpoint2_exception_handling.py`](examples/02_painpoint2_exception_handling.py)

**❌ 传统写法 - 异常处理复杂且容易遗漏**
```python
def parse_and_calculate(input_str: str) -> float:
    try:
        num = float(input_str)
        if num <= 0:
            raise ValueError("数字必须大于0")
        return 100 / num
    except ValueError as e:
        # 需要手动处理每种异常类型
        print(f"解析失败: {e}")
        raise  # 或者返回默认值，但会丢失异常信息

def another_operation(data: str) -> float:
    try:
        # 一些复杂操作
        return float(data) * 2
    except ValueError as e:
        print(f"操作失败: {e}")
        raise

# 调用方需要嵌套 try-catch，代码冗长
try:
    result1 = parse_and_calculate("abc")
    result2 = another_operation("xyz")
    print(f"结果1: {result1}, 结果2: {result2}")
except ValueError as e:
    print(f"值错误: {e}")
except ZeroDivisionError as e:
    print(f"除零错误: {e}")
except Exception as e:
    print(f"未知错误: {e}")

# 问题：
# 1. 异常处理代码冗长，需要多层嵌套
# 2. 容易遗漏某些异常类型
# 3. 错误处理逻辑分散，难以统一管理
```

**✅ NoNone 写法 - 统一错误处理**
```python
from nonone import catch, try_catch

# 方式 A: 使用装饰器 - 一键转换现有函数
@catch
def dangerous_divide(a: float, b: float) -> float:
    return a / b  # 可能抛出 ZeroDivisionError

result = dangerous_divide(10, 0)
# 自动包装为: Err(ZeroDivisionError(...))

# 方式 B: 临时调用 - 无需修改原函数定义
def parse_and_calculate_unsafe(input_str: str) -> float:
    num = float(input_str)
    if num <= 0:
        raise ValueError("数字必须大于0")
    return 100 / num

# 直接包装调用，立即获得 Result
result = try_catch(parse_and_calculate_unsafe, "abc")

match result:
    case Ok(value):
        print(f"计算成功: {value}")
    case Err(e):
        print(f"处理失败: {type(e).__name__}: {e}")
# ✅ 所有异常都被统一捕获并转换为 Err，不会遗漏
```


---

#### 痛点 3：繁琐的嵌套 None 判断

> 💡 **完整示例代码：** [`examples/03_painpoint3_nested_none.py`](examples/03_painpoint3_nested_none.py)

**❌ 传统写法 - 嵌套地狱**
```python
def get_user(user_id: int) -> User | None:...

def get_score_record(user: User) -> ScoreRecord | None:...

def extract_score(record: ScoreRecord) -> float | None:...

def get_user_score_traditional(user_id: int) -> float | None:
    """获取用户分数，需要三层检查"""
    # 第1层: 检查用户是否存在
    user = get_user(user_id)
    if user is None:
        return None
    
    # 第2层: 检查用户是否有分数记录
    score_record = get_score_record(user)
    if score_record is None:
        return None
    
    # 第3层: 检查分数是否有效
    score = extract_score(score_record)
    if score is None:
        return None
    
    return score

# 使用时的嵌套判断
score = get_user_score_traditional(123)
if score is not None:
    print(f"用户分数: {score}")
else:
    print("无法获取用户分数")
```

**✅ NoNone 写法 - 扁平化链式调用**
```python
from nonone import ok, err, Result, Ok, Err

def get_user_safe(user_id: int) -> Result[User, str]:...

def get_score_record_safe(user: User) -> Result[ScoreRecord, str]:...

def extract_score_safe(record: ScoreRecord) -> Result[float, str]:...

def get_user_score_nonone(user_id: int) -> Result[float, str]:
    """使用链式调用获取用户分数"""
    return (
        get_user_safe(user_id)            # 获取用户
        .and_then(get_score_record_safe)  # 获取分数记录
        .and_then(extract_score_safe)     # 提取分数
    )

# 使用时只需要一次 match
match get_user_score_nonone(123):
    case Ok(score):
        print(f"用户分数: {score}")          # ✅ 输出: 用户分数: 95.5
    case Err(msg):
        print(f"获取失败: {msg}")            # 任何一步出错都会到这里

```

---

### 安装

使用 `uv`（推荐）或 `pip` 安装 **NoNone**：

```bash
uv pip install nonone
# 或者
pip install nonone
```

---

### 快速上手

#### 💡 重要提示：大写 vs 小写

NoNone 提供了两套 API，用途不同但很简单：

| 场景 | 使用 | 示例 |
|------|------|------|
| **构造实例** | 小写 `ok()` / `err()` | `return ok(42)` |
| **模式匹配** | 大写 `Ok` / `Err` | `case Ok(value):` |
| **类型注解** | 大写 `Result` | `-> Result[int, str]` |

**简单记忆**：🏗️ **建造时用小写的**（函数），🔍 **检查时用大的**（类）

---

### 快速上手：5分钟体验 NoNone

> 💡 **完整示例代码：** [`examples/04_quick_start.py`](examples/04_quick_start.py)

```python
# quick_start.py
from nonone import ok, err, Result, Ok, Err

# 1. 基本构造
result = ok(42)           # Ok(42)
error = err("出错了")     # Err("出错了")

# 2. 链式调用
def parse_number(s: str) -> Result[float, str]:
    try:
        return ok(float(s))
    except ValueError:
        return err(f"'{s}' 不是有效数字")

def validate_positive(num: float) -> Result[float, str]:
    if num <= 0:
        return err("数字必须大于0")
    return ok(num)

def calculate(num: float) -> Result[float, str]:
    return ok(num * 2)

# 组合多个操作
def process_input(input_str: str) -> Result[float, str]:
    return (
        parse_number(input_str)      # 解析字符串
        .and_then(validate_positive) # 验证正数
        .and_then(calculate)         # 计算
    )

# 3. 模式匹配处理结果
result = process_input("10")
match result:
    case Ok(value):
        print(f"✅ 结果: {value}")
    case Err(error):
        print(f"❌ 错误: {error}")
```

这就是 NoNone 的核心用法：**构造 → 链式调用 → 模式匹配**。

---

### 进阶用法：强大的 match-case

> 💡 **完整示例代码：** [`examples/05_advanced_pattern_matching.py`](examples/05_advanced_pattern_matching.py)

NoNone 基于 `dataclass` 构建，可以充分利用 Python 模式匹配的强大功能。

#### 🎯 使用 Guard（条件过滤）

在 `case` 中添加 `if` 条件，实现更精细的控制：

```python
from nonone import ok, err, Ok, Err

def divide(a: float, b: float):
    if b == 0:
        return err("除数不能为零")
    return ok(a / b)

result = divide(100, 2)

match result:
    case Ok(val) if val > 10:
        print(f"得到一个较大的数: {val}")     # ✅ 输出: 得到一个较大的数: 50.0
    case Ok(val):
        print(f"得到一个较小的数: {val}")
    case Err(msg):
        print(f"计算失败: {msg}")
```

#### 📦 嵌套对象解构

如果 `Ok` 里面包裹的是 `dataclass`，可以直接在 `case` 中解构其属性：

```python
from dataclasses import dataclass
from nonone import ok, err, Ok, Err, Result

@dataclass
class CalculationResult:
    value: float
    operation: str
    success: bool

def divide_with_info(a: float, b: float) -> Result[CalculationResult, str]:
    if b == 0:
        return err("除数不能为零")
    return ok(CalculationResult(
        value=a / b,
        operation="division",
        success=True
    ))

match divide_with_info(10, 2):
    # 直接解构内部对象的特定属性
    case Ok(CalculationResult(operation="division", value=result_value)):
        print(f"结果: {result_value}")           # ✅ 输出: 除法结果: 5.0
    case Ok(CalculationResult(value=result_value)):
        print(f"其他运算结果: {result_value}")
    case Err(error):
        print(f"计算失败: {error}")
```

这种深度解构让你可以在一行代码中完成**类型检查 + 属性提取 + 条件判断**，非常优雅！

---

## API 参考

### 类型定义

```python
Result: TypeAlias = Ok[T, E] | Err[T, E]
```

### 构造器

#### `ok(value: T) -> Ok[T, Any]`
创建成功的 Result 实例。

**参数**
- `value`: 成功时返回的值

**返回值**
- `Ok[T, Any]` - 成功的 Result，错误类型为 `Any`

**示例**
```python
result = ok(42)        # Ok(42)
result = ok("success") # Ok("success")
```

#### `err(error: E) -> Err[Any, E]`
创建失败的 Result 实例。

**参数**
- `error`: 错误信息或异常对象

**返回值**
- `Err[Any, E]` - 失败的 Result，成功类型为 `Any`

**示例**
```python
result = err("出错了")     # Err("出错了")
result = err(ValueError("无效值")) # Err(ValueError("无效值"))
```

### 装饰器和工具函数

#### `@catch`
装饰器，自动捕获函数中的异常并返回 Result。

**适用场景**
- 将现有函数一键转换为返回 Result 的函数
- 统一异常处理，避免遗漏异常类型

**示例**
```python
@catch
def divide(a: float, b: float) -> float:
    return a / b

result = divide(10, 0)  # Err(ZeroDivisionError(...))
```

#### `try_catch(func: Callable[P, T], *args, **kwargs) -> Result[T, Exception]`
立即执行函数并返回 Result，无需修改原函数定义。

**参数**
- `func`: 要执行的函数
- `*args`, `**kwargs`: 传递给函数的参数

**返回值**
- `Result[T, Exception]` - 执行结果

**示例**
```python
def parse_number(s: str) -> float:
    return float(s)

result = try_catch(parse_number, "abc")  # Err(ValueError(...))
```

### 状态检查方法

#### `is_ok() -> bool`
检查是否为成功状态。

**返回值**
- `True` - 如果是 `Ok`
- `False` - 如果是 `Err`

**示例**
```python
ok(42).is_ok()      # True
err("error").is_ok() # False
```

#### `is_err() -> bool`
检查是否为错误状态。

**返回值**
- `True` - 如果是 `Err`
- `False` - 如果是 `Ok`

**示例**
```python
ok(42).is_err()      # False
err("error").is_err() # True
```

### 值提取方法（谨慎使用）

#### `unwrap() -> T`
提取成功值，如果是 `Err` 则抛出 `UnwrapError` 异常。

**警告**
- 仅在确定结果是 `Ok` 时使用
- 生产代码建议使用模式匹配或链式调用

**示例**
```python
ok(42).unwrap()        # 42
err("error").unwrap()  # 抛出 UnwrapError
```

#### `unwrap_err() -> E`
提取错误值，如果是 `Ok` 则抛出 `UnwrapError` 异常。

**示例**
```python
err("error").unwrap_err() # "error"
ok(42).unwrap_err()      # 抛出 UnwrapError
```

#### `unwrap_or(default: T) -> T`
返回成功值或默认值。

**参数**
- `default`: 当结果是 `Err` 时返回的默认值

**示例**
```python
ok(42).unwrap_or(0)        # 42
err("error").unwrap_or(0)   # 0
```

#### `unwrap_or_else(op: Callable[[E], T]) -> T`
返回成功值或用错误值调用函数的结果。

**参数**
- `op`: 接收错误值并返回默认值的函数

**示例**
```python
ok(42).unwrap_or_else(str)           # 42
err("error").unwrap_or_else(len)      # 5 (字符串长度)
```

#### `expect(msg: str) -> T`
返回成功值，如果是 `Err` 则抛出带自定义消息的 `UnwrapError`。

**参数**
- `msg`: 自定义错误消息

**示例**
```python
ok(42).expect("应该成功")        # 42
err("error").expect("应该成功")  # 抛出 UnwrapError("应该成功: error")
```

### 链式操作方法

#### `map(f: Callable[[T], U]) -> Result[U, E]`
对成功值应用函数，保持错误类型不变。

**参数**
- `f`: 接收成功值并返回新值的函数

**返回值**
- `Ok(f(value))` - 如果是 `Ok`
- `Err(error)` - 如果是 `Err`（无操作）

**示例**
```python
ok(42).map(str)         # Ok("42")
err("error").map(str)   # Err("error")
```

#### `map_err(f: Callable[[E], F]) -> Result[T, F]`
对错误值应用函数，保持成功类型不变。

**参数**
- `f`: 接收错误值并返回新错误值的函数

**返回值**
- `Ok(value)` - 如果是 `Ok`（无操作）
- `Err(f(error))` - 如果是 `Err`

**示例**
```python
ok(42).map_err(str.upper)      # Ok(42)
err("error").map_err(str.upper) # Err("ERROR")
```

#### `and_then(f: Callable[[T], Result[U, E]]) -> Result[U, E]`
链式调用，用成功值调用返回 Result 的函数。

**参数**
- `f`: 接收成功值并返回新 Result 的函数

**返回值**
- `f(value)` - 如果是 `Ok`
- `Err(error)` - 如果是 `Err`（短路，不调用 `f`）

**示例**
```python
def double(x: int) -> Result[int, str]:
    return ok(x * 2)

ok(42).and_then(double)        # Ok(84)
err("error").and_then(double)  # Err("error")
```

#### `try_and_then(f: Callable[[T], U]) -> Result[U, Exception | E]`
安全链式调用，将不返回 Result 的函数包装为 Result。

**参数**
- `f`: 接收成功值并可能抛出异常的函数

**返回值**
- `Ok(f(value))` - 如果是 `Ok` 且函数成功
- `Err(exception)` - 如果是 `Ok` 且函数抛出异常
- `Err(error)` - 如果是 `Err`（无操作）

**示例**
```python
def risky_divide(x: int) -> float:
    return 100 / x

ok(2).try_and_then(risky_divide)      # Ok(50.0)
ok(0).try_and_then(risky_divide)      # Err(ZeroDivisionError(...))
err("error").try_and_then(risky_divide) # Err("error")
```

#### `or_else(f: Callable[[E], Result[T, F]]) -> Result[T, F]`
错误恢复，用错误值调用函数尝试恢复。

**参数**
- `f`: 接收错误值并返回新 Result 的函数

**返回值**
- `Ok(value)` - 如果是 `Ok`（无操作）
- `f(error)` - 如果是 `Err`

**示例**
```python
def recover(error: str) -> Result[int, str]:
    return ok(0)

ok(42).or_else(recover)        # Ok(42)
err("error").or_else(recover)  # Ok(0)
```

#### `inspect(func: Callable[[T | E], Any]) -> Result[T, E]`
执行副作用函数后返回自身，用于调试和日志。

**参数**
- `func`: 对值执行副作用的函数

**返回值**
- 原始的 Result 实例

**示例**
```python
# 对成功值执行副作用
ok(42).inspect(print)  # 打印 42，返回 Ok(42)

# 对错误值执行副作用  
err("error").inspect(print)  # 打印 "error"，返回 Err("error")
```

### 异常类

#### `UnwrapError`
当在错误状态下调用 `unwrap()` 或 `unwrap_err()` 时抛出的异常。

**继承关系**
- `RuntimeError`

---

### 许可协议

本项目基于 MIT License 开源.