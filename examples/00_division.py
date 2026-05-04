from nonone import ok, err, Err, Ok, Result


# 0️⃣ 直接处理（最最常用）
def div_direct(a: float, b: float) -> float:
    return a / b
    # ✅ 极简，零开销
    # ❌ 除零时程序崩溃
    # 🎯 适用：确信 b!=0、快速原型、脚本


print("=== div_direct ===")
print(f"成功: {div_direct(10, 2)}")    # 5.0
# print(div_direct(10, 0))            # 抛出 ZeroDivisionError，程序崩溃



# 1️⃣ 抛自定义异常（常用）
def div_raise(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b
    # ✅ 错误信息明确，语义清晰
    # ❌ 调用方必须 try-except
    # 🎯 适用：库函数、需要明确错误类型


print("\n=== div_raise ===")
print(f"成功: {div_raise(10, 2)}")           # 5.0
# print(div_raise(10, 0))                   # 抛出 ValueError


# 2️⃣ 返回 None（常用）
def div_none(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b
    # ✅ 不会崩溃，调用方需检查 None
    # ❌ 丢失错误原因
    # 🎯 适用：简单场景，只需知道成功/失败


print("\n=== div_none ===")
print(f"成功: {div_none(10, 2)}")            # 5.0
print(f"失败: {div_none(10, 0)}")            # None


# 3️⃣ Result 类型（工程推荐）
def div_result(a: float, b: float) -> Result[float, str]:
    if b == 0:
        return err("除数不能为零")
    return ok(a / b)
    # ✅ 安全 + 带错误信息 + 强制处理
    # ✅ 支持链式调用
    # 🎯 适用：中大型项目，需要可靠错误传播


print("\n=== div_result ===")
match div_result(10, 2):
    case Ok(v): 
        print(f"成功: {v}")           # 5.0
    case Err(e): 
        print(f"失败: {e}")

match div_result(10, 0):
    case Ok(v): 
        print(f"成功: {v}")
    case Err(e): 
        print(f"失败: {e}")          # 除数不能为零
    

