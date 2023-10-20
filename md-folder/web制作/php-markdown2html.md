投稿日 2023年03月21日
# PHPを使用して、Markdownファイルをブラウザに表示する

htmlファイルの作成に慣れていないので、Markdown形式のファイルを書いてHTML形式に変換することにした。

私はlamp構成のMAMPでwebページを作っているので、phpを使用して変換した。  
まず「PHP Markdown」というライブラリをダウンロードして使用してみたが、上手くいかなった。

PHPのパッケージ管理ソフトであるcomposerを使用したら上手くいったのでその方法を書いていく。 

## macのターミナルを起動
ターミナルでcomposerをダウンロードしていく。
どこのディレクトリでダウンロードしてもいいらしいので、私は~/Documents上で行った。
## composerをダウンロード
下のリンクからcomposerをダウンロードする。
https://getcomposer.org/download
ターミナルで各行を実行してcomposerをダウンロードする。
```bash
$ php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
$ php -r "if (hash_file('sha384', 'composer-setup.php') === '55ce33d7678c5a611085589f1f3ddf8b3c52d662cd01d4ba75c0ee0459970c2200a51f492d557530c71c15d8dba01eae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
$ php composer-setup.php
$ php -r "unlink('composer-setup.php');"
```
各行が何をしているかというと、  
1. 現在のディレクトリにインストーラをダウンロードする  
2. インストーラを検証する  
3. インストーラを実行する  
4. インストーラを削除する  

4を実行後にlsコマンドで確認してみるとカレントディレクトリにcomposer.pharがある。  	

## composer.pharを移動
下記のコマンドで、ローカルのディレクトリからcomposer.pharファイルを /usr/local/bin/composer に移動する。  
これで、どのディレクトリからでも composer コマンドを実行できるようになる。

このコマンドは sudo コマンドを使って実行されるので、root権限が必要である。  
```bash
$ sudo mv composer.phar /usr/local/bin/composer
#Password: パスワードが求められるので自分のmacのログインパスワードを入れる。
```
## composerがインストールされているか確認する。

```bash
$ composer

#Composer version 2.5.4 2023-02-15 13:10:06
```

## michelf/php-markdownをインストール
michelf/php-markdownは、Markdown形式のテキストをHTMLに変換するためのライブラリ。  
下記のコマンドを実行してダウンロードする。
```bash
$ composer require michelf/php-markdown
```
私の場合は~/Document上でインストールしたので、"ls ~/Document/vendor"でvendorフォルダにautoload.php、composer、michelfがあることが確認できる。

## markdown形式（拡張がmd）のファイルを作成
私はVSCodeでMAMPのhtdocディレクトリを開きそこに、htdoc.mdファイルを作った。  
下記がhtdoc.mdのコードである。
```md
# 見出し1

これは本文の一部です。**太字** や *斜体* にすることができます。

## 見出し2

- リストアイテム1
- リストアイテム2
- リストアイテム3

### 見出し3

1. 番号付きリストアイテム1
2. 番号付きリストアイテム2
3. 番号付きリストアイテム3

#### 見出し4

[リンクのテキスト](https://www.example.com)

##### 見出し5
```
## PHPファイルにmarkdown形式のファイルを読み込み、html形式に変換してwebページに表示されるようにする。
htdoc.mdと同じディレクトリにb.phpファイルを作る。  
違うディレクトリに作ってもいいが、パスの指定が面倒である。  
b.phpファイルのコードを下に載せる。  

＜コマンドの説明＞
- require：ファイルを呼び出す  
- use：名前空間のパスを短くする  
- file_get_contents（）：ファイル読み込み  
- Markdown::defaultTransform()：MarkdownをHTMLに変換  

＜コードを自分用に書き直したい場合＞
1. require文はvendor/autoload.phpのパスを指定する。  
vendor/autoload.phpが~/Documentsにある場合はlocalを自分の名前に書き換えればOK。（ターミナルに'whoami'と入力すれば自分の名前がわかる。）
2. file_get_contentsの引数は表示したいMarkdown形式のファイルのパス名を記入する。


b.phpファイル
```php
<?php
//Composerでインストールされたphp-markdownのautoloadingを行う
require '/Users/local/Documents/vendor/autoload.php';
use Michelf\Markdown;

// Markdown形式のテキストファイルを読み込む
$text = file_get_contents('hdoc.md');

// MarkdownをHTMLに変換する
$html = Markdown::defaultTransform($text);

// HTMLを表示する
echo $html;
?>
```
b.phpファイルをブラウザで表示する。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3268288/18726417-4ed1-5b24-04e2-3d645bfa781c.png" alt="説明テキスト" width="600" height="400" />


## ＜改良版＞PHPファイルにmarkdown形式のファイルを読み込みから、HTMLファイルとしてブラウザに出力するまでを関数にする。
htdoc.mdと同じディレクトリにbb.phpファイルを作る。  
先程のb.phpファイルからの変更箇所は、関数化したところと、requireをrequire_onceにしたところである。

関数化したのは、複数のMarkdown形式のファイルの読み込みを容易に行えるようにするためである。

同じファイルを何度もrequireすると、同じコードが何度も実行されることになるので、パフォーマンス上の問題やクラスや関数の重複宣言によるエラーも発生する可能性があるらしい。  
この問題を回避するために、require_once関数を使用してみた。  
require_onceは、指定されたファイルが既に読み込まれている場合には、再度読み込まないようにするためのものである。

bb.php
```php
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <?php
    require_once '~/Documents/vendor/autoload.php';
    use Michelf\Markdown;
    // Markdown形式のテキストファイルを読み込む
    function f($t){
        $text = file_get_contents($t);
        $html = Markdown::defaultTransform($text);
        echo $html;
    }
    ?>
</head>
<body>
    <?php
    f('hdoc.md');
    ?>
  
</body>
</html>
```
bb.phpをブラウザで確認する。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3268288/e45dce05-3227-ce74-601a-8b3f9532b44a.png" alt="説明テキスト" width="600" height="400" />


