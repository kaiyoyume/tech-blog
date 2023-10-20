投稿日　2023年3月22日
# MacからEC2にHTMLファイルを送信して、Webで公開してみた
MAMPで作成したWebページをEC２上で公開したい。

MAMPのhdocフォルダに保存されているindex.htmlファイルをEC2上で公開してみようと思う。

## Macのターミナルを起動
1. EC2にssh接続する。（このターミナルウィンドウを以後、EC2と呼ぶ。）  
<a href="mac-ec2-connect.html">AWSのEC2インスタンスへMacからSSH接続する（接続失敗の解決策も記載）</a>

2. ターミナルの新規ウィンドウを立ち上げる。（以後、ターミナルと呼ぶ。）
この２つのターミナル画面から操作していく。

## EC2のホームディレクトリにhdocフォルダを作る。
```bash
mkdir hdoc
```
## EC２のhdocフォルダにファイルをコピーするシェルスクリプトを作る。
VSCodeで、ec2_scp.shという名前のファイルを作成して、Macのホームディレクトリに保存する。

c2_scp.shのコード
```bash
scp -i "キーペアのフルパス" $1 ec2-user@EC２のパブリック IPv4 DNS:/home/ec2-user/hdoc
```
$1は引数で、シェルスクリプトの実行時に送りたいファイルのパスを指定する。

※キーペアとシェルスクリプトが同じフォルダにないので、キーペアはフルパスで書く。

## ターミナルのホームディレクトリで、以下のコマンドを実行。
```bash
sh c2_scp.sh /Applications/MAMP/htdocs/index.html
```
MAMPのhtdocsフォルダにあるindex.htmlファイルがEC2のhtdocフォルダに送信される。

## EC2上で、ディレクトリからドキュメントルートへファイルをコピー
EC2のhdocディレクトリのindex.htmlをEC2のドキュメントルートへコピーする。

EC2のホームディレクトリで、以下のコマンドを実行。
```bash
sudo cp hdoc/index.html /var/www/html
```
EC２のパブリックIPv4DNSをコピーしてchromeで検索すると、index.htmlファイルが表示される。
