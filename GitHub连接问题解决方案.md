# GitHub 连接问题解决方案

## 🔍 问题诊断

- ✅ Ping 可以通（基本网络正常）
- ❌ HTTPS (443端口) 连接超时
- ❌ 未配置 SSH key

---

## 🚀 解决方案

### 方案 1: 使用 SSH 方式（推荐）

#### 步骤 1: 生成 SSH Key

```bash
# 生成 SSH key（将邮箱替换为你的 GitHub 邮箱）
ssh-keygen -t ed25519 -C "1406134023@qq.com"

# 按 Enter 使用默认路径
# 可以设置密码或直接按 Enter（不设置密码）
```

#### 步骤 2: 添加 SSH Key 到 GitHub

```bash
# 复制公钥内容
cat ~/.ssh/id_ed25519.pub

# 或者使用 pbcopy（macOS）
pbcopy < ~/.ssh/id_ed25519.pub
```

然后：
1. 访问 https://github.com/settings/keys
2. 点击 "New SSH key"
3. 粘贴公钥内容
4. 点击 "Add SSH key"

#### 步骤 3: 更改远程仓库地址为 SSH

```bash
# 删除现有的 HTTPS 远程地址
git remote remove origin

# 添加 SSH 远程地址
git remote add origin git@github.com:ck1406134023/python-learn.git

# 测试连接
ssh -T git@github.com

# 推送代码
git push -u origin main
```

---

### 方案 2: 配置 Git 代理（如果你有代理）

#### 如果你有 HTTP/HTTPS 代理

```bash
# 设置 Git HTTP 代理（替换为你的代理地址和端口）
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

# 或者只对 GitHub 设置代理
git config --global http.https://github.com.proxy http://127.0.0.1:7890
```

#### 如果你有 SOCKS5 代理

```bash
git config --global http.proxy socks5://127.0.0.1:1080
git config --global https.proxy socks5://127.0.0.1:1080
```

#### 取消代理设置

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

---

### 方案 3: 使用 GitHub CLI（gh）

```bash
# 安装 GitHub CLI
brew install gh

# 登录
gh auth login

# 推送代码
git push -u origin main
```

---

### 方案 4: 修改 hosts 文件（临时方案）

```bash
# 编辑 hosts 文件
sudo nano /etc/hosts

# 添加以下内容（IP 地址可能需要更新）
140.82.112.3 github.com
140.82.112.4 github.com
```

⚠️ 注意：这种方法可能不稳定，IP 地址会变化。

---

## 🎯 推荐流程

**最佳方案：使用 SSH**

1. 生成 SSH key
2. 添加到 GitHub
3. 改用 SSH 地址推送

**备选方案：配置代理**

如果你已经有代理工具（如 Clash、V2Ray 等），配置 Git 代理最简单。

---

## 📝 快速命令（SSH 方案）

```bash
# 1. 生成 SSH key
ssh-keygen -t ed25519 -C "1406134023@qq.com"

# 2. 复制公钥（macOS）
pbcopy < ~/.ssh/id_ed25519.pub

# 3. 访问 https://github.com/settings/keys 添加 SSH key

# 4. 更改远程地址
git remote set-url origin git@github.com:ck1406134023/python-learn.git

# 5. 测试并推送
ssh -T git@github.com
git push -u origin main
```

---

## ❓ 常见问题

### Q: SSH 连接也失败怎么办？
A: 检查代理设置，SSH 也可能需要代理：
```bash
# 在 ~/.ssh/config 中添加
Host github.com
    ProxyCommand nc -X 5 -x 127.0.0.1:1080 %h %p
```

### Q: 如何查看当前代理设置？
```bash
git config --global --get http.proxy
git config --global --get https.proxy
```

### Q: 如何查看远程仓库地址？
```bash
git remote -v
```

