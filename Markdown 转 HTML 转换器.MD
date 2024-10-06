

---

# Markdown 转 HTML 转换器

这个仓库包含一个简单的 Python 应用程序，它将 Markdown 文件转换为美观的 HTML 页面，具有 GitHub 风格的主题。它使用 Flask 来提供一个轻量级的本地服务器，方便你在浏览器中预览转换后的 Markdown 文件。

## 功能
- **Markdown 转 HTML**：将 Markdown (`.md`) 文件转换为 HTML 格式，保留代码块并使用 Highlight.js 进行语法高亮。
- **GitHub 样式**：应用 GitHub Markdown 样式，输出页面整洁美观，便于阅读。
- **简单易用**：通过交互方式输入文件路径，并启动 Flask 服务器在浏览器中预览 HTML。
- **代码高亮**：支持代码块的语法高亮，使用 Highlight.js 让代码展示更加专业。

## 使用方法
1. **安装依赖**：确保已安装 Flask 和 Python-Markdown，可以通过以下命令安装：
    ```sh
    pip install Flask markdown
    ```

2. **运行应用**：使用以下命令启动程序：
    ```sh
    python app.py
    ```

3. **输入文件路径**：打开`http://localhost:5000`后，终端会提示你输入需要转换的 Markdown 文件路径。你也可以指定输出的 HTML 文件名（可选）。

4. **在浏览器中查看**：转换完成后，应用会在 `http://localhost:5000` 提供生成的 HTML 文件，你可以在浏览器中查看和验证效果。

## 示例
启动程序后，你会看到类似以下的提示：
- "请输入 Markdown 文件路径:" （例如 `example.md`）
- "请输入 HTML 输出文件路径（可选）:" （按回车键可使用默认输出文件）

生成的 HTML 文件会有类似于 GitHub 上的 Markdown 风格，非常适合文档、项目报告或者便于分享的展示用途。

## 技术栈
- **Flask**：用于运行本地服务器，查看 HTML 文件。
- **Python-Markdown**：将 Markdown 转换为 HTML。
- **Highlight.js**：对代码块进行语法高亮。
- **GitHub CSS**：提供 GitHub 风格的 Markdown 样式。

## 适用场景
- **文档生成**：快速将项目文档转换为 HTML 格式。
- **便捷分享**：生成精美 HTML，便于分享，无需 Markdown 查看器。
- **本地预览**：在发布前预览 Markdown 文件在 HTML 中的呈现效果。

## 贡献
欢迎提出问题或提交 Pull Request 来改进这个应用！无论是新功能、修复 Bug 还是优化代码，任何贡献都非常欢迎。

## 许可证
本项目采用 MIT 许可证进行授权。

