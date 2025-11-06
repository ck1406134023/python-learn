# Day 5: 控制流
# 目标：掌握条件语句和循环语句

print("=" * 50)
print("条件语句（if/elif/else）")
print("=" * 50)

# 1. 基本条件判断
score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"分数: {score}, 等级: {grade}")

# 2. 多条件判断
age = 25
has_experience = True

if age >= 18 and has_experience:
    print("可以申请工作")
else:
    print("不符合条件")

# 3. 三元运算符（类似 JavaScript 的 ? :）
status = "学习" if age < 30 else "工作"
print(f"状态: {status}")

# JavaScript 对比
# const status = age < 30 ? "学习" : "工作"

print("\n" + "=" * 50)
print("循环语句（for/while）")
print("=" * 50)

# 1. for 循环（类似 JavaScript 的 for...of）
fruits = ["苹果", "香蕉", "橙子"]
print("for 循环遍历列表:")
for fruit in fruits:
    print(f"  - {fruit}")

# 2. range 函数（类似 JavaScript 的 for (let i = 0; i < 5; i++)）
print("\n使用 range:")
for i in range(1, 6):
    print(f"  第{i}天学习 Python")

# 3. 带索引的遍历（类似 JavaScript 的 forEach with index）
print("\n带索引遍历:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# 4. while 循环
print("\nwhile 循环:")
count = 0
while count < 3:
    print(f"  计数: {count}")
    count += 1

# 5. 循环控制：break 和 continue
print("\nbreak 和 continue:")
for i in range(1, 11):
    if i == 5:
        continue  # 跳过当前迭代
    if i == 8:
        break    # 退出循环
    print(f"  {i}")

# 6. 列表推导式（循环的简洁写法）
print("\n列表推导式:")
squares = [x ** 2 for x in range(1, 6)]
print(f"  平方数: {squares}")

# 带条件的列表推导式
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"  偶数的平方: {even_squares}")

# 7. 嵌套循环
print("\n嵌套循环（打印乘法表片段）:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i * j}", end="  ")
    print()  # 换行

# JavaScript 对比
# Python 使用缩进，JavaScript 使用大括号
# Python:                    JavaScript:
# if condition:              if (condition) {
#     do_something()             doSomething();
#                            }

