投稿日 2023年03月23日 更新日 2023年04月02日
# ライブラリを使用せずに、簡単なFileTreeを作成する

chatGPT4に「ライブラリを使用しないで、filetreeを作る」と入力したら、希望通りに実装してくれた。

## htmlファイル(filetree.html)：
### フォルダはspanタグとulタグで構成する。
- **ulタグでフォルダを表す。**
- **フォルダ名をつけるのとフォルダの開閉の操作をするために、ulタグの上にspanタグを置く。**


まずはここまでを理解するのが重要である。
後の説明は、コードの後ろに書く。
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>FileTree Example</title>
    <link rel="stylesheet" href="fileTree.css" />
</head>
<body>
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
    <script src="fileTree.js"></script>
</body>
</html>

```
spanタグとulタグ（順序なしリスト）とliタグ（リストアイテム）を使用して、ファイルツリーを作成している。  

ulタグとliタグでファイルツリー構造を作る。 

spanタグは、フォルダ名とファイル名の表示と、後から機能を追加するために必要である。  

具体的には、
- フォルダ名のspanタグは、クラス属性folderを付加する。  
folderクラスの要素のクリック時に、フォルダの中身（ドロップダウンリスト）の非表示/表示を切り替える機能を付加する。  
- ファイル名のspanタグは、クラス属性fileを付加する。

ファイルツリーは、divタグの中に入っている。  
divタグには、file-treeクラスが付加されている。   
divタグで囲みクラス名を付加することで、スタイル適用の範囲をファイルツリーに限定できる。


## CSSファイル（fileTree.css）:

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
ファイルツリーのフォルダ名の前につけている矢印の仕組みをリンク先で説明している。
<p>参照：
    <a href="filetree-toggle.html">AWSのEC2インスタンスへMacからSSH接続する（接続失敗の解決策も記載）</a></p>

## JavaScriptファイル（fileTree.js）:
ファイルツリーのフォルダをクリックすることで、サブフォルダやファイルを表示/非表示にする動的な操作を実現している。


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
- documentは、JavaScriptにおけるウェブページのHTML文書を表すオブジェクト。  
- DOMContentLoadedイベントが発生したときにfunction(){・・・}を実行する。  
 DOMContentLoadedはHTML文書の解析が完了し、DOMツリーが構築されたタイミングを示す。  
-  .folderクラスが適用された要素をすべて取得し、folders定数に代入する。  
##### for文の中身
-  各フォルダ要素に対して、クリックイベントリスナーを追加する。  
フォルダがクリックされると、function(){・・・}が実行されるようにする。

- this.classList.toggle('open');とは、
thisのクラス属性にアクセスして、要素に'open'クラスがあるかどうかを確認する。  
'open'クラスがあれば、それを削除し、無ければ追加する。  

- nextElementSibling はDOMプロパティであり、ある要素の次にある同階層（兄弟）の要素を取得する。  
次の要素がない場合はnullを返す。

- ? と : は、簡潔なif-else文の作成に使われている。  
ulタグで囲まれたリスト要素が表示されていたらblock、非表示だったらnoneである。  
ul.style.display = {（ul.style.display == 'none'） がTrueの場合は'block'、Falseの場合は'none'}
##### クリックイベントリスナーの外
ページの読み込み時にすべてのサブフォルダやファイルをデフォルトで非表示にする。

# 　webページで確認。使える。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3268288/e84bfa2a-ea58-0c05-4822-11ec0bade40c.png" alt="説明テキスト" width="600" height="400" />

