import os

def extract_text_between(file_path):
    start_string = "<h1>"
    end_string ="</h1>"

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    start_index = text.find(start_string)

    if start_index == -1:  # 開始文字列が見つからない場合
        return None

    start_index += len(start_string)  # 開始文字列の直後から検索開始
    end_index = text.find(end_string, start_index)

    if end_index == -1:  # 終了文字列が見つからない場合
        return None

    return text[start_index:end_index]

def create_file_tree_html(path, relative_path=""):
    html = ""
    
    for entry in os.scandir(path):
        # .DS_Store ファイルを無視する
        if entry.name == ".DS_Store":
            continue
        if entry.is_file():
            file_path = os.path.join(relative_path, entry.name)
            file_name = extract_text_between(file_path)
            html += f'<li><span class="file" onclick="onfile(this)" data-filename="{file_path}">{file_name}</span></li>'
        elif entry.is_dir():
            sub_html = create_file_tree_html(entry.path, os.path.join(relative_path, entry.name))
            html += f'<p class="folder" onclick="onfolder(this)">{entry.name}</p><ul>{sub_html}</ul>'

    return html

def main():
    folder_path = "static/html-folder"
    output_path = "static/output.html"

    file_tree_html = create_file_tree_html(folder_path, folder_path)

    with open(output_path, "w") as output_file:
        output_file.write(f"""
<!DOCTYPE html>
<html>
    <head>
        <style>
            ul {{
                display: none;
                padding-left: 10px;
                list-style-type: none;
            }}
            li {{
                margin-bottom: 5px;
            }}
            .folder,
            .file {{
                cursor: pointer;
            }}
            .file::before {{
                content: "📄";  
                margin-right: 5px;
            }} 
            .folder:before {{
                content: "▶";
                display: inline-block;
                margin-right: 6px;
            }}

            .folder.open:before {{
                content: "▼";
            }}
            .selected {{
             font-weight: bold; /* 太字にするスタイルを追加 */
            }}
            .file:hover {{
                text-decoration: underline; /*ファイル名にカーソルを載せたときに下線を表示*/
            }}
        </style>
        <script>
            let selectedFile = null;
            function onfile(th){{
                const fname = th.getAttribute('data-filename');
                window.parent.setfiletomain(fname);
                if (selectedFile) {{
                    selectedFile.classList.remove('selected');
                }}
                th.classList.add('selected');
                selectedFile = th;
            }}
            function onfolder(th){{
                th.classList.toggle('open');
                const el = th.nextElementSibling;
                if (el.style.display === '' || el.style.display === 'none') {{
                    el.style.display = 'block';
                }} else {{
                    el.style.display = 'none';
                }}
            }}
        </script>
    </head>
    <body>
    {file_tree_html}
    </body>
</html>
""")

if __name__ == "__main__":
    main()
