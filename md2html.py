import os
import glob
import markdown

def convert_md_to_html(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as md_file:
        md_text = md_file.read()
        html = markdown.markdown(md_text, extensions=['fenced_code','md_in_html','mdx_math'])

    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(
f"""
<!DOCTYPE html>
<html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Converted Markdown</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
</head>
<body>
  {html}
<script>hljs.highlightAll();</script>
</body>
</html>
"""
        )

def main():
    input_folder = 'md-folder'
    output_folder = 'static/html-folder'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for md_file_path in glob.glob(f'{input_folder}/**/*.md', recursive=True):
        relative_path = os.path.relpath(md_file_path, input_folder)
        output_path = os.path.splitext(os.path.join(output_folder, relative_path))[0] + '.html'
        output_dir = os.path.dirname(output_path)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        convert_md_to_html(md_file_path, output_path)
        print(f"変換完了: {md_file_path} -> {output_path}")

if __name__ == '__main__':
    main()
