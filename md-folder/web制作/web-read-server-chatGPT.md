投稿日 2023年03月26日
# webブラウザからサーバのファイルを読み込む方法をchatGPTに学ぶ

chatGPTが作ったプログラムは信用できないので、以下の手順で必要な関数を得る。  

- まず動くプログラムを作ってもらいテストする。  

- OKだったら動くプログラムから必要な部分だけを関数にしてもらう。  

- その関数を使って、さらにテストプログラムを作ってもらいチェックする。

## まず具体的なプログラムをchatGPT4に作ってもらう
私「bodyにボタン、テキスト表示エリア、テキスト入力エリアを配置する。クリックすると、入力エリアのテキストをファイル名として使用して、テキストエリアにファイルを読み込むようにしたい。サーバーのファイルを読み込むプログラムを書いて。」

chatGPT4はフレームワークなどを使用したプログラムの例を教えてくれたが、シンプルな構成がよかったので付け加えた。

私「apacheとjavascriptのみを使って」

これで期待していた、シンプルな動く例を得られた。
テストしたら、ちゃんと動いた。

ApacheサーバーとJavaScriptを使用して、クライアントからサーバーのファイルを読み込む例を作成する。

私「例題としてすごく参考になった。Javascriptの関数を書いてほしい。必要とする部分はファイル名を指定して、テキストファイルを返す関数が欲しい。」

望み通りの関数が得られた。

chatGPT4が作ってくれた、指定されたファイル名に基づいてテキストファイルの内容を取得し返すJavaScript関数
```javascript
async function fetchFileContent(filename) {
    try {
        const response = await fetch(filename);
        if (response.ok) {
            const fileContent = await response.text();
            return fileContent;
        } else {
            throw new Error('ファイルの読み込みに失敗しました。');
        }
    } catch (error) {
        console.error(error);
        throw error;
    }
}

```

## 使用例も書いてもらった
ファイル名を入力してボタンをクリックすると、指定されたファイル名のテキストファイルの内容を表示する

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Reader</title>
</head>
<body>
    <input type="text" id="filenameInput" placeholder="ファイル名を入力">
    <button id="loadBtn">ファイルを読み込む</button>
    <div id="fileContent" style="border: 1px solid black; padding: 10px;"></div>
    <script>
        async function fetchFileContent(filename) {
            try {
                const response = await fetch(filename);
                if (response.ok) {
                    const fileContent = await response.text();
                    return fileContent;
                } else {
                    throw new Error('ファイルの読み込みに失敗しました。');
                }
            } catch (error) {
                console.error(error);
                throw error;
            }
        }

        document.getElementById('loadBtn').addEventListener('click', async function() {
            const filename = document.getElementById('filenameInput').value;
            if (!filename) {
                alert('ファイル名を入力してください。');
                return;
            }

            try {
                const fileContent = await fetchFileContent(filename);
                document.getElementById('fileContent').innerText = fileContent;
            } catch (error) {
                console.error(error);
                alert('ファイルの読み込みに失敗しました。');
            }
        });
    </script>
</body>
</html>
```

## chatGPT4が教えてくれた注意事項
この方法ではセキュリティ上のリスクがある。  
認証や権限の設定を行わない場合、誰でもサーバー上の任意のファイルにアクセスできる可能性がある。  
実際のアプリケーションでこの方法を使用する場合は、適切な認証と権限の設定を行う必要がある。

## 初心者用の注意事項
Apacheが必要。  
ローカルでは動かない。
