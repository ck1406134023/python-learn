# Python 学习计划 - 前端开发程序员版

## 📋 学习目标
- 掌握 Python 基础语法和核心概念
- 理解 Python 的编程范式（面向对象、函数式编程）
- 能够独立开发 Python 项目
- 了解常用的 Python 库和框架

## 🎯 总体时间安排
- **总时长**: 8-10 周（工作日，每天 1-2 小时）
- **学习方式**: 阅读官方文档 + 编写代码实践
- **学习资源**: Python 官方文档、MDN 风格的教程、实际项目

---

## 📚 第一阶段：Python 基础语法（2周）

### 第1周：基础入门

#### Day 1: 环境搭建与第一个程序
**学习任务**:
- [ ] 安装 Python 开发环境（推荐 VS Code + Python 扩展）
- [ ] 阅读 [Python 官方文档 - 教程](https://docs.python.org/zh-cn/3/tutorial/index.html) 第1-2章
- [ ] 编写第一个 Python 程序：打印 "Hello, Python!"
- [ ] 练习：编写程序打印个人信息（姓名、年龄、职业）

**实践代码**:
```python
# hello_python.py
print("Hello, Python!")
print("我是一名前端开发程序员，正在学习 Python")
```

#### Day 2: 变量与数据类型
**学习任务**:
- [ ] 阅读文档：变量、数字、字符串
- [ ] 对比 JavaScript 和 Python 的数据类型差异
- [ ] 练习：创建不同类型的变量并打印其类型

**实践代码**:
```python
# variables.py
name = "张三"
age = 25
is_frontend_dev = True
skills = ["JavaScript", "React", "Vue"]

print(f"姓名: {name}, 类型: {type(name)}")
print(f"年龄: {age}, 类型: {type(age)}")
```

#### Day 3: 字符串操作
**学习任务**:
- [ ] 阅读文档：字符串格式化、常用方法
- [ ] 练习：字符串拼接、格式化、切片操作
- [ ] 对比：Python 的 f-string 和 JavaScript 的模板字符串

**实践代码**:
```python
# string_practice.py
name = "前端开发"
lang = "Python"
message = f"我是{name}，正在学习{lang}"
print(message.upper())
print(message.replace("学习", "掌握"))
```

#### Day 4: 列表与字典
**学习任务**:
- [ ] 阅读文档：列表（list）和字典（dict）
- [ ] 对比 JavaScript 数组和对象
- [ ] 练习：创建列表和字典，进行增删改查操作

**实践代码**:
```python
# data_structures.py
# 列表操作
fruits = ["苹果", "香蕉", "橙子"]
fruits.append("葡萄")
fruits.remove("香蕉")

# 字典操作
person = {
    "name": "张三",
    "age": 25,
    "skills": ["JavaScript", "Python"]
}
person["city"] = "北京"
print(person.get("name"))
```

#### Day 5: 控制流（if/for/while）
**学习任务**:
- [ ] 阅读文档：条件语句、循环语句
- [ ] 练习：编写判断和循环程序
- [ ] 对比：Python 的缩进语法和 JavaScript 的大括号

**实践代码**:
```python
# control_flow.py
# 条件判断
score = 85
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
else:
    grade = "需努力"

# 循环
for i in range(1, 6):
    print(f"第{i}天学习 Python")

# 列表推导式（类似 JavaScript 的 map）
numbers = [x * 2 for x in range(5)]
```

---

### 第2周：函数与模块

#### Day 6: 函数定义与调用
**学习任务**:
- [ ] 阅读文档：函数定义、参数、返回值
- [ ] 理解：位置参数、关键字参数、默认参数
- [ ] 对比：Python 函数和 JavaScript 函数

**实践代码**:
```python
# functions.py
def greet(name, title="工程师"):
    """问候函数"""
    return f"你好，{name}，你是一名{title}"

# 调用函数
print(greet("张三"))
print(greet("李四", "前端开发"))
```

#### Day 7: Lambda 与高阶函数
**学习任务**:
- [ ] 阅读文档：Lambda 表达式、map、filter、reduce
- [ ] 对比：Python 和 JavaScript 的函数式编程

**实践代码**:
```python
# lambda_functions.py
numbers = [1, 2, 3, 4, 5]
# map（类似 JavaScript 的 map）
squared = list(map(lambda x: x ** 2, numbers))
# filter（类似 JavaScript 的 filter）
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

#### Day 8: 模块与包
**学习任务**:
- [ ] 阅读文档：import 语句、模块创建
- [ ] 练习：创建自己的模块并导入使用
- [ ] 对比：Python 的模块系统和 JavaScript 的 ES6 模块

**实践代码**:
```python
# my_module.py
def calculate_area(length, width):
    return length * width

# main.py
from my_module import calculate_area
area = calculate_area(5, 3)
print(f"面积: {area}")
```

#### Day 9: 文件操作
**学习任务**:
- [ ] 阅读文档：文件读写操作
- [ ] 练习：读取和写入文件
- [ ] 实践：创建一个简单的日志系统

**实践代码**:
```python
# file_operations.py
# 写入文件
with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("今天学习了 Python 文件操作\n")

# 读取文件
with open("diary.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

#### Day 10: 第一阶段总结与项目
**学习任务**:
- [ ] 复习前9天的内容
- [ ] 完成小项目：个人任务管理器（命令行版）

**项目要求**:
- 可以添加、删除、查看任务
- 任务保存到文件
- 使用函数组织代码

---

## 🔧 第二阶段：面向对象编程（1.5周）

#### Day 11-12: 类与对象基础
**学习任务**:
- [ ] 阅读文档：类定义、对象创建、属性、方法
- [ ] 对比：Python 的类和 JavaScript 的类（ES6）
- [ ] 练习：创建简单的类

**实践代码**:
```python
# oop_basic.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我是{self.name}，今年{self.age}岁"

person = Person("张三", 25)
print(person.introduce())
```

#### Day 13-14: 继承与多态
**学习任务**:
- [ ] 阅读文档：继承、方法重写、super()
- [ ] 练习：创建继承关系的类

**实践代码**:
```python
# inheritance.py
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵"
```

#### Day 15: 特殊方法与属性
**学习任务**:
- [ ] 阅读文档：`__init__`、`__str__`、`__repr__` 等特殊方法
- [ ] 练习：实现字符串表示、比较等方法

---

## 📦 第三阶段：常用内置库（1.5周）

#### Day 16-17: 日期时间处理（datetime）
**学习任务**:
- [ ] 阅读文档：[datetime 模块](https://docs.python.org/zh-cn/3/library/datetime.html)
- [ ] 练习：日期格式化、计算时间差

**实践代码**:
```python
# datetime_practice.py
from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# 计算一周后的日期
future = now + timedelta(days=7)
```

#### Day 18-19: 正则表达式（re）
**学习任务**:
- [ ] 阅读文档：[re 模块](https://docs.python.org/zh-cn/3/library/re.html)
- [ ] 对比：Python 正则和 JavaScript 正则
- [ ] 练习：匹配、搜索、替换文本

#### Day 20-21: JSON 处理
**学习任务**:
- [ ] 阅读文档：[json 模块](https://docs.python.org/zh-cn/3/library/json.html)
- [ ] 练习：JSON 序列化和反序列化
- [ ] 实践：处理 API 数据格式

**实践代码**:
```python
# json_practice.py
import json

data = {
    "name": "张三",
    "skills": ["JavaScript", "Python"]
}

# 转换为 JSON 字符串
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

# 从 JSON 字符串解析
parsed = json.loads(json_str)
```

---

## 🛠️ 第四阶段：实用工具库（2周）

#### Day 22-24: 文件系统操作（os, pathlib）
**学习任务**:
- [ ] 阅读文档：os 模块、pathlib 模块
- [ ] 练习：文件路径操作、目录遍历
- [ ] 实践：批量重命名文件脚本

#### Day 25-26: HTTP 请求（requests）
**学习任务**:
- [ ] 阅读文档：[requests 库文档](https://requests.readthedocs.io/)
- [ ] 安装：`pip install requests`
- [ ] 练习：发送 GET/POST 请求、处理响应
- [ ] 对比：Python requests 和 JavaScript fetch

**实践代码**:
```python
# requests_practice.py
import requests

# GET 请求
response = requests.get("https://api.github.com/users/octocat")
data = response.json()
print(data)
```

#### Day 27-28: 数据处理（pandas 基础）
**学习任务**:
- [ ] 阅读文档：[pandas 入门教程](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [ ] 安装：`pip install pandas`
- [ ] 练习：读取 CSV、数据筛选、基本统计

#### Day 29-30: 环境与包管理
**学习任务**:
- [ ] 阅读文档：pip、venv、requirements.txt
- [ ] 练习：创建虚拟环境、安装依赖
- [ ] 实践：管理项目依赖

**实践代码**:
```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux

# 安装包
pip install requests pandas

# 生成依赖文件
pip freeze > requirements.txt
```

---

## 🎨 第五阶段：实战项目（2-3周）

### 项目1：命令行待办事项应用（Day 31-35）
**功能要求**:
- 添加、删除、完成任务
- 任务优先级
- 数据持久化（JSON 文件）
- 命令行界面

**技术栈**: 基础语法 + 文件操作 + JSON

### 项目2：API 数据抓取工具（Day 36-40）
**功能要求**:
- 从公开 API 获取数据（如 GitHub API、天气 API）
- 数据清洗和格式化
- 保存到文件或数据库

**技术栈**: requests + JSON + 文件操作

### 项目3：文件管理工具（Day 41-45）
**功能要求**:
- 批量重命名文件
- 文件分类整理
- 统计文件信息

**技术栈**: os + pathlib + 正则表达式

### 项目4：数据统计工具（Day 46-50）
**功能要求**:
- 读取 CSV/JSON 数据
- 数据分析和统计
- 生成简单的报告

**技术栈**: pandas + 文件操作

---

## 📖 推荐学习资源

### 官方文档（优先）
1. **Python 官方教程**（中文）: https://docs.python.org/zh-cn/3/tutorial/
2. **Python 标准库参考**: https://docs.python.org/zh-cn/3/library/index.html
3. **Python 语言参考**: https://docs.python.org/zh-cn/3/reference/

### 在线教程（文档形式）
1. **Real Python**: https://realpython.com/ （高质量文章，有代码示例）
2. **Python 进阶**: https://www.pythontab.com/html/pythonhexinbiancheng/
3. **廖雪峰 Python 教程**: https://www.liaoxuefeng.com/wiki/1016959663602400

### 实践平台
1. **LeetCode**: 刷题练习算法
2. **Python 挑战**: https://www.pythonchallenge.com/
3. **Codewars**: https://www.codewars.com/

---

## 💡 学习建议

### 每日学习流程
1. **早上（30分钟）**: 阅读文档，理解概念
2. **上班间隙（30-60分钟）**: 编写代码实践
3. **晚上（30分钟）**: 复习和总结

### 学习方法
1. **对比学习**: 利用前端经验，对比 JavaScript 和 Python 的差异
2. **实践为主**: 每学一个概念就立即写代码验证
3. **做笔记**: 记录 Python 特有的语法和概念
4. **项目驱动**: 通过实际项目巩固知识

### 注意事项
1. **缩进很重要**: Python 使用缩进而不是大括号
2. **类型动态**: Python 是动态类型语言（类似 JavaScript）
3. **Pythonic 风格**: 学习 Python 的惯用写法
4. **错误处理**: 学会阅读和理解 Python 的错误信息

---

## 📝 学习记录模板

### 每日学习记录
```markdown
## Day X: [主题]

### 学习内容
- [ ] 阅读文档：[章节名称]
- [ ] 理解概念：[概念名称]

### 代码实践
- [ ] 文件：xxx.py
- [ ] 功能：xxx

### 遇到的问题
1. 问题描述
2. 解决方案

### 明日计划
- [ ] 学习内容
```

---

## ✅ 检查清单

### 第一阶段检查
- [ ] 能熟练使用变量和数据类型
- [ ] 掌握列表和字典操作
- [ ] 能编写函数和模块
- [ ] 能进行文件读写

### 第二阶段检查
- [ ] 理解类和对象的概念
- [ ] 能创建和使用类
- [ ] 理解继承机制

### 第三阶段检查
- [ ] 能使用常用内置库
- [ ] 能处理 JSON 数据
- [ ] 能使用正则表达式

### 第四阶段检查
- [ ] 能使用 requests 发送 HTTP 请求
- [ ] 能使用 pandas 处理数据
- [ ] 能管理虚拟环境和依赖

### 第五阶段检查
- [ ] 完成至少 2 个实战项目
- [ ] 代码结构清晰，有注释
- [ ] 能独立解决遇到的问题

---

## 🎯 进阶方向（学完基础后）

1. **Web 开发**: Flask 或 Django
2. **数据分析**: pandas + matplotlib + jupyter
3. **自动化脚本**: 爬虫、文件处理、系统管理
4. **API 开发**: FastAPI 或 Flask RESTful

---

**开始日期**: _______________
**预计完成日期**: _______________

祝你学习顺利！🚀

