# Day 4: 列表与字典
# 目标：掌握 Python 的核心数据结构

print("=" * 50)
print("列表（List）操作")
print("=" * 50)

# 列表（类似 JavaScript 的数组）
fruits = ["苹果", "香蕉", "橙子"]
print(f"初始列表: {fruits}")

# 添加元素
fruits.append("葡萄")  # 末尾添加
print(f"添加葡萄: {fruits}")

fruits.insert(1, "草莓")  # 指定位置插入
print(f"插入草莓: {fruits}")

# 删除元素
fruits.remove("香蕉")  # 删除指定值
print(f"删除香蕉: {fruits}")

popped = fruits.pop()  # 删除并返回最后一个元素
print(f"弹出最后一个: {popped}, 剩余: {fruits}")

# 列表切片
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\n原列表: {numbers}")
print(f"前三个: {numbers[:3]}")
print(f"后三个: {numbers[-3:]}")
print(f"中间三个: {numbers[3:6]}")

# 列表推导式（类似 JavaScript 的 map）
squared = [x ** 2 for x in range(1, 6)]
print(f"\n列表推导式（平方）: {squared}")

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"列表推导式（偶数）: {even_numbers}")

# JavaScript 对比
# const squared = [1,2,3,4,5].map(x => x ** 2)
# const even = [1,2,3,4,5,6,7,8,9,10].filter(x => x % 2 === 0)

print("\n" + "=" * 50)
print("字典（Dict）操作")
print("=" * 50)

# 字典（类似 JavaScript 的对象）
person = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "skills": ["JavaScript", "Python"]
}
print(f"初始字典: {person}")

# 访问值
print(f"\n姓名: {person['name']}")
print(f"年龄: {person.get('age')}")

# 添加/修改
person["email"] = "zhangsan@example.com"
person["age"] = 26
print(f"添加邮箱: {person}")

# 删除
del person["city"]
print(f"删除 city: {person}")

# 遍历字典
print("\n遍历字典:")
for key, value in person.items():
    print(f"  {key}: {value}")

# 只遍历键
print("\n所有键:", list(person.keys()))
# 只遍历值
print("所有值:", list(person.values()))

# 嵌套字典
programmer = {
    "info": {
        "name": "李四",
        "age": 28
    },
    "skills": {
        "frontend": ["React", "Vue"],
        "backend": ["Python"]
    }
}
print(f"\n嵌套字典: {programmer}")
print(f"前端技能: {programmer['skills']['frontend']}")

