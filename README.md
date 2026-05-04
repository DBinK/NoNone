# NoNone

> 拒绝隐式 `None`，拥抱现代 Python 的 Rust 风格 [Result](https://doc.rust-lang.org/std/result/) 类型。

**NoNone** 是一个轻量、纯粹且类型安全的 Python 库。它引入了 Rust 语言中著名的 [Result（](https://doc.rust-lang.org/std/result/)`Ok` / `Err`）模式，并专为 **Python 3.10+** 的 `match-case`（结构化模式匹配）语法量身定制。

---

### 为什么选择 NoNone？告别错误处理的三大痛点

在传统的 Python 开发中，我们经常面临以下痛点：

#### 痛点 1：错误处理的缺失与运行时崩溃

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
# 编译器和 IDE 会强制你处理两种情况，无法忽略错误
match result:
    case Ok(value):
        print(f"结果: {value * 2}")  # ✅ 安全，value 一定存在
    case Err(msg):
        print(f"错误: {msg}")
```

---

#### 痛点 2：异常处理冗长且容易遗漏

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


💡 **理解链式调用中的关键方法**：

- **`.and_then(func)`** - 当前一步成功时，执行下一个返回 `Result` 的操作
  - 如果前一步是 `Err`，则跳过后续所有步骤
  - 用于串联多个可能失败的操作

- **`.map(func)`** - 对成功的值进行转换（不改变 Result 结构）
  - 只在 `Ok` 时执行，将 `Ok(value)` 转换为 `Ok(func(value))`
  - 用于最后的格式化、计算等纯函数操作

**对比理解**：
```python
# 假设 get_address_safe 返回 Ok(Address(street="长安街"))

# 使用 .map() 转换结果
result = get_address_safe(123).map(lambda addr: addr.street)
# 结果: Ok("长安街")  ← 仍然是 Ok，但内部值从 Address 变成了 str

# 如果不使用 .map()
result = get_address_safe(123)
# 结果: Ok(Address(street="长安街"))  ← 内部还是 Address 对象
```


---

#### 痛点 3：繁琐的嵌套 None 判断

**❌ 传统写法 - 嵌套地狱**
```python
def get_user(user_id: int) -> User | None:...

def get_score_record(user: User) -> ScoreRecord | None:...

def extract_score(record: ScoreRecord) -> float | None:...

def get_user_score(user_id: int) -> float | None:
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
score = get_user_score(123)
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

def get_user_score_result(user_id: int) -> Result[float, str]:
    """使用链式调用获取用户分数"""
    return (
        get_user_safe(user_id)            # 获取用户
        .and_then(get_score_record_safe)  # 获取分数记录
        .and_then(extract_score_safe)     # 提取分数
    )

# 使用时只需要一次 match
match get_user_score_result(123):
    case Ok(score):
        print(f"用户分数: {score}")          # ✅ 输出: 用户分数: 95.5
    case Err(msg):
        print(f"获取失败: {msg}")            # 任何一步出错都会到这里
```

---

### NoNone 的核心优势

- ✅ **编译时类型安全**：基于双泛型 Result[T, E] 设计，静态类型检查器能提前发现潜在错误
- ✅ **强制错误处理**：无法忽略错误情况，必须显式处理所有分支
- ✅ **消除 None 隐患**：再也不用担心 `AttributeError: 'NoneType' object has no attribute...`
- ✅ **扁平化代码结构**：通过 `.map()`、`.and_then()` 等链式调用将多层嵌套变为线性流程
- ✅ **统一的错误模型**：所有错误都是 `Err`，无需记忆各种异常类型
- ✅ **无缝迁移**：使用 `@catch` 或 `try_catch` 零成本改造现有代码
- ✅ **现代语法支持**：专为 Python 3.10+ 的 `match-case` 结构化模式匹配量身定制
- ✅ **极简无包袱**：零第三方依赖，基于 `slots=True` 的数据类构建，极致轻量且高效

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

NoNone 基于 `dataclass` 构建，可以充分利用 Python 模式匹配的强大功能。

#### 🎯 使用 Guard（条件过滤）

在 `case` 中添加 `if` 条件，实现更精细的控制：

```python
from nonone import ok, Ok, Err

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
from nonone import ok, Ok, Err

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
    case Ok(CalculationResult(operation="division", value=value)):
        print(f"除法结果: {value}")           # ✅ 输出: 除法结果: 5.0
    case Ok(CalculationResult(value=value)):
        print(f"其他运算结果: {value}")
    case Err(error):
        print(f"计算失败: {error}")
```

这种深度解构让你可以在一行代码中完成**类型检查 + 属性提取 + 条件判断**，非常优雅！

---

### API 使用指南

根据你的需求选择合适的 API：

#### 🏗️ 构造 Result
```python
from nonone import ok, err

ok(42)           # 成功结果
err("出错了")     # 失败结果
```

#### 🔍 检查结果状态
```python
result.is_ok()   # True/False
result.is_err()  # True/False
```

#### 📦 提取值（谨慎使用）
```python
result.unwrap()          # 成功返回值，失败抛出 UnwrapError
result.unwrap_or(0)      # 成功返回值，失败返回默认值 0
result.expect("错误提示") # 成功返回值，失败抛出带自定义消息的异常
```

#### ⛓️ 链式操作（推荐）
```python
# map: 转换成功的值
ok(5).map(lambda x: x * 2)        # Ok(10)

# and_then: 串联多个可能失败的操作
ok(5).and_then(lambda x: ok(x * 2))  # Ok(10)

# or_else: 失败时尝试恢复
err("错").or_else(lambda e: ok(0))   # Ok(0)
```

#### 🎯 模式匹配（最安全）
```python
from nonone import Ok, Err

match result:
    case Ok(value):
        print(f"成功: {value}")
    case Err(error):
        print(f"失败: {error}")
```

#### 🛡️ 捕获异常
```python
from nonone import catch, try_catch

# 装饰器方式
@catch
def risky_func():
    return 1 / 0

# 函数方式
result = try_catch(risky_func)
```

---

### 许可协议

本项目基于 MIT License 开源。