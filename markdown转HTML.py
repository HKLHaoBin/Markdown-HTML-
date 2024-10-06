import markdown
import os
from flask import Flask, send_file, request

app = Flask(__name__)

# 全局变量保存 HTML 文件路径
html_file_path = None

# Markdown 转换为 HTML 的函数
GITHUB_CSS_URL = "https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css"
HIGHLIGHT_JS_CSS_URL = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/github.min.css"
HIGHLIGHT_JS_URL = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"

def md_to_html(md_file_path, html_file_path=None):
    # 读取 Markdown 文件
    if not os.path.exists(md_file_path):
        print(f"Error: 文件 {md_file_path} 不存在.")
        return None
    
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 转换为 HTML
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'codehilite'])

    # 添加 GitHub 风格的 CSS 和 Highlight.js 支持
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{GITHUB_CSS_URL}">
        <link rel="stylesheet" href="{HIGHLIGHT_JS_CSS_URL}">
        <title>Markdown to HTML</title>
        <style>
            body {{
                box-sizing: border-box;
                min-width: 200px;
                max-width: 980px;
                margin: 0 auto;
                padding: 45px;
            }}
            .markdown-body {{
                box-sizing: border-box;
                min-width: 200px;
                max-width: 980px;
                margin: 0 auto;
                padding: 30px;
                border: 1px solid #e1e4e8;
                border-radius: 6px;
                background-color: #ffffff;
            }}
        </style>
    </head>
    <body>
        <article class="markdown-body">
            {html_content}
        </article>
        <script src="{HIGHLIGHT_JS_URL}"></script>
        <script>hljs.highlightAll();</script>
    </body>
    </html>
    """

    # 如果没有指定输出文件，则在当前目录生成同名的 HTML 文件
    if html_file_path is None:
        html_file_path = os.path.splitext(md_file_path)[0] + '.html'
    
    # 写入 HTML 文件
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"转换完成: {md_file_path} -> {html_file_path}")
    return html_file_path

# Flask 部分
@app.route('/')
def index():
    global html_file_path

    # 如果 HTML 文件路径还没有生成
    if html_file_path is None:
        # 提示用户输入 Markdown 文件路径和 HTML 输出路径
        md_file = input("请输入 Markdown 文件路径: ")
        html_file = input("请输入 HTML 输出文件路径（可选，直接回车则保存为同名 .html 文件）: ")

        if html_file.strip() == "":
            html_file = None

        # 调用转换函数
        html_file_path = md_to_html(md_file, html_file)

    # 检查 HTML 文件是否已生成
    if html_file_path is not None and os.path.exists(html_file_path):
        return send_file(html_file_path)
    else:
        return "HTML 文件生成失败，请重试。"

if __name__ == "__main__":
    # 启动 Flask 服务器，展示生成的 HTML 文件
    app.run(host='0.0.0.0', port=5000, debug=True)
