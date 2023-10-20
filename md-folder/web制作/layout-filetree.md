投稿日 2023年03月23日
# ページレイアウトのサイドバーにfiletreeを入れる

## chatGPTにページレイアウト構成を正確に指定して、サイドバーにfiletreeを入れる。
以前chatGPTに作ってもらったページレイアウト構成のプログラムと、ファイルツリーのプログラムを組み合わせたかった。

しかし、前と同じ質問をしても同じプログラムを返してくれないので思い通りにはならなかった。  
chatGPTに作ってもらった２つ以上のプログラムを結合したいときは、手動の方が早い。

具体的に２つのプログラムを指定して、結合したプログラムを要求すれば上手くいくような気がするが、プログラムの入力方法が分からない。

何回か質問し直したり、手直ししたりして完成した。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3268288/59caa7fc-d56d-d264-23c8-89a4c4286c23.png" alt="説明テキスト" width="600" height="400" />

下にプログラムを書く。
## htmlファイル

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid Layout with FileTree Example</title>
    <link rel="stylesheet" href="gridLayout.css" />
    <link rel="stylesheet" href="fileTree.css" />
</head>
<body>
    <header>Header</header>
    <aside>
        <div class="file-tree">
            <ul>
                <li>
                    <span class="folder">Root</span>
                    <ul>
                        <li>
                            <span class="folder">Folder 1</span>
                            <ul>
                                <li><span class="file">file1.txt</span></li>
                                <li><span class="file">file2.txt</span></li>
                            </ul>
                        </li>
                        <li>
                            <span class="folder">Folder 2</span>
                            <ul>
                                <li><span class="file">file3.txt</span></li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
    </aside>
    <main>Main Content</main>
    <footer>Footer</footer>
    <script src="fileTree.js"></script>
</body>
</html>
```
## gridLayout.css
ページレイアウトのスタイルを指定するcssファイル
```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    display: grid;
    grid-template-columns: 200px 1fr;
    grid-template-rows: auto 1fr auto;
    grid-template-areas:
        "header header"
        "sidebar main"
        "footer footer";
    height: 100vh;
    width: 100vw;
}

header {
    grid-area: header;
    background-color: #c09af3;
    display: flex;
    justify-content: center;
    align-items: center;
}

aside {
    grid-area: sidebar;
    background-color: #f8ccf5;
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 5px;
}

main {
    grid-area: main;
    background-color: #fdfdfd;
    display: flex;
    justify-content: center;
    align-items: center;
}

footer {
    grid-area: footer;
    background-color: #c09af3;
    display: flex;
    justify-content: center;
    align-items: center;
}
```
## fileTree.js
filetreeのフォルダの開閉機能のJavascriptファイル
```javascript
document.addEventListener('DOMContentLoaded', function () {
    const folders = document.querySelectorAll('.folder');

    for (let i = 0; i < folders.length; i++) {
        folders[i].addEventListener('click', function () {
            this.classList.toggle('open');
            let ul = this.nextElementSibling;

            if (ul) {
                ul.style.display = ul.style.display === 'none' ? 'block' : 'none';
            }
        });

        let ul = folders[i].nextElementSibling;

        if (ul) {
            ul.style.display = 'none';
        }
    }
});
```
## fileTree.css
fileTreeのスタイルを指定するcssファイル
```css
.file-tree ul {
    list-style-type: none;
    padding-left: 20px;
}

.folder,
.file {
    cursor: pointer;
}

.folder:before {
    content: "▶";
    display: inline-block;
    margin-right: 6px;
}

.folder.open:before {
    content: "▼";
}
```
