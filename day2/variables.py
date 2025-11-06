# Day 2: 变量与数据类型
# 目标：理解 Python 的数据类型，并与 JavaScript 对比

# 字符串（类似 JavaScript 的 string）
name = "张三"
greeting = "你好"

# 数字（类似 JavaScript 的 number）
age = 25
height = 175.5  # 浮点数

# 布尔值（类似 JavaScript 的 boolean）
is_frontend_dev = True
is_learning = False

# 列表（类似 JavaScript 的 array）
skills = ["JavaScript", "React", "Vue", "Python"]
numbers = [1, 2, 3, 4, 5]

# 字典（类似 JavaScript 的 object）
person = {
    "name": "李四",
    "age": 28,
    "city": "北京"
}

# None（类似 JavaScript 的 null）
data = None

# 打印类型
print("=== 数据类型 ===")
print(f"name: {name}, 类型: {type(name)}")
print(f"age: {age}, 类型: {type(age)}")
print(f"height: {height}, 类型: {type(height)}")
print(f"is_frontend_dev: {is_frontend_dev}, 类型: {type(is_frontend_dev)}")
print(f"skills: {skills}, 类型: {type(skills)}")
print(f"person: {person}, 类型: {type(person)}")
print(f"data: {data}, 类型: {type(data)}")

# 对比 JavaScript
# JavaScript          Python
# ---------------------------
# let name = "张三"   name = "张三"
# const age = 25      age = 25
# let arr = [1,2,3]   arr = [1,2,3]
# let obj = {}        obj = {}

