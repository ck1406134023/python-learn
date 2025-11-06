# Day 3: 字符串操作
# 目标：掌握 Python 字符串的各种操作方法

# 1. 字符串格式化
name = "前端开发"
lang = "Python"

# f-string（类似 JavaScript 的模板字符串）
message = f"我是{name}，正在学习{lang}"
print("f-string:", message)

# JavaScript 对比
# const message = `我是${name}，正在学习${lang}`

# 2. 字符串方法
text = "Hello Python World"

print("\n=== 字符串方法 ===")
print(f"原字符串: {text}")
print(f"大写: {text.upper()}")
print(f"小写: {text.lower()}")
print(f"首字母大写: {text.capitalize()}")
print(f"标题格式: {text.title()}")

# 3. 字符串查找和替换
text2 = "JavaScript 是前端语言"
print(f"\n查找 '前端': {text2.find('前端')}")
print(f"替换: {text2.replace('JavaScript', 'Python')}")

# 4. 字符串切片（类似 JavaScript 的 slice）
text3 = "Hello Python"
print(f"\n切片 [0:5]: {text3[0:5]}")  # Hello
print(f"切片 [6:]: {text3[6:]}")      # Python
print(f"切片 [-6:]: {text3[-6:]}")    # Python（从后往前）

# 5. 字符串分割和连接
tags = "Python,JavaScript,React"
tag_list = tags.split(",")
print(f"\n分割: {tag_list}")

joined = " | ".join(tag_list)
print(f"连接: {joined}")

# 6. 字符串格式化（旧方法）
name = "张三"
age = 25
# .format() 方法
info = "姓名：{}，年龄：{}".format(name, age)
print(f"\n.format(): {info}")

# % 格式化（类似 C 语言）
info2 = "姓名：%s，年龄：%d" % (name, age)
print(f"% 格式化: {info2}")

