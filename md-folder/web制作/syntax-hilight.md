投稿日 2023年04月05日

# Webページ上のコードブロックにシンタックスハイライトを適用する

### コードブロックとは、ソースコードやコードの一部を示すために使用される区間を指す。
HTMLではpreタグとcodeタグを組み合わせてコードブロックを表現することが一般的である。

- preタグは、前後の改行や空白をそのまま表示するためのタグである。
- codeタグはコードやコンピュータ上の要素を示すためのタグである。

これらのタグを組み合わせることで、コードの構造を保持したままコードブロックを表示できる。

### シンタックスハイライトは、ソースコードの構造や構文に基づいて異なる要素に色を付けることで読みやすくする。
ウェブページに埋め込まれたコードブロックに、シンタックスハイライトを適用することができる。
この場合、highlight.jsやPrismなどのJavaScriptライブラリを使用することが一般的である。




## コードブロックにシンタックスハイライトを適用するプログラムの例
html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Example</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
</head>
<body>
  <h1>Pythonのプログラムを表示する例</h1>
  <pre><code class="language-python">
    def hello_world():
        print("Hello, World!")
    
    hello_world()
  </code></pre>

  <h1>シェルコマンドを表示する例</h1>
  <pre><code class="language-bash">
    chmod 400 key.pem
  </code></pre>

  <script>hljs.highlightAll();</script>
</body>
</html>
```
### 2つのscriptタグを使用して、まずライブラリを読み込み、次にライブラリを初期化し、シンタックスハイライトを適用する処理が行われている。

#### 1つ目のscriptタグは、src属性を使用してhighlight.jsのJavaScriptライブラリを読み込んでいる。
ここではCDN（Content Delivery Network）を使用して読み込んでいるが、ライブラリをローカルにダウンロードして使用することもできる。  

CDNとは、インターネット上でコンテンツ（画像、動画、スタイルシート、JavaScriptファイルなど）を高速かつ効率的に配信するためのネットワークシステムである。  

CDNは、世界中に分散配置されたサーバー群から構成されている。  

これにより、ユーザーがアクセスする際に最も近いサーバーからコンテンツを取得できるようになる。

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css">
```
##### scriptタグの下のlinkタグは、HTMLファイルにhighlight.jsのCSSスタイルシートをリンクする。
CSSスタイルシートは、シンタックスハイライトの見た目（色、フォントスタイルなど）を定義している。

linkタグは、HTML文書と外部リソース（通常はスタイルシート）を関連付けるために使用される。

rel属性は、linkタグ内で使用され、リンクされた文書と現在の文書の関係を定義する。
relは"relationship"（関係）の略。

#### ２つ目のscriptタグは、ライブラリを初期化し、シンタックスハイライトを適用するためのコードを実行している。
hljs.highlightAll()は、ページ内のすべてのコードブロックにシンタックスハイライトを適用する関数。
この関数を呼び出すことで、ページ内のコードブロックがシンタックスハイライトされた状態で表示される。

## 補足
MacのターミナルのシェルコマンドをWebページに表示したいと思い、codeタグのclass="language-zsh"にしたらシンタックスハイライトが適用されなかった。

bashは適用された。