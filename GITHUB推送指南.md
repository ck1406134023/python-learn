# GitHub 推送指南

## 📋 当前状态

✅ Git 仓库已初始化  
✅ 文件已提交到本地仓库  
⏳ 等待连接到 GitHub 远程仓库

---

## 🚀 步骤 1: 在 GitHub 上创建仓库

1. 访问 [GitHub](https://github.com)
2. 点击右上角的 **"+"** → **"New repository"**
3. 填写仓库信息：
   - **Repository name**: `python-learn` (或你喜欢的名字)
   - **Description**: `Python学习计划 - 前端开发程序员的学习之路`
   - **Visibility**: 选择 Public 或 Private
   - ⚠️ **不要**勾选 "Initialize this repository with a README"（因为我们已经有了）
4. 点击 **"Create repository"**

---

## 🔗 步骤 2: 连接本地仓库到 GitHub

创建仓库后，GitHub 会显示推送命令。选择 **"push an existing repository from the command line"**，然后运行：

```bash
# 添加远程仓库（将 YOUR_USERNAME 替换为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/python-learn.git

# 或者使用 SSH（如果你配置了 SSH key）
git remote add origin git@github.com:YOUR_USERNAME/python-learn.git
```

---

## 📤 步骤 3: 推送到 GitHub

```bash
# 推送代码到 GitHub
git push -u origin main
```

如果遇到认证问题，可能需要：
- 使用 Personal Access Token（HTTPS）
- 或配置 SSH key（SSH）

---

## 🔄 后续更新代码

以后每次修改代码后，使用以下命令：

```bash
# 查看修改
git status

# 添加修改的文件
git add .

# 提交修改
git commit -m "描述你的修改"

# 推送到 GitHub
git push
```

---

## 💡 快速命令（一键执行）

如果你已经创建了 GitHub 仓库，可以直接运行：

```bash
# 替换 YOUR_USERNAME 和 REPO_NAME
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

---

## ❓ 常见问题

### 1. 认证失败
- **HTTPS**: 使用 Personal Access Token 代替密码
- **SSH**: 确保已配置 SSH key

### 2. 分支名称不同
如果 GitHub 默认分支是 `master`，使用：
```bash
git push -u origin main:master
```

### 3. 查看远程仓库
```bash
git remote -v
```

---

**提示**: 如果遇到问题，可以随时查看 Git 状态：
```bash
git status
```

