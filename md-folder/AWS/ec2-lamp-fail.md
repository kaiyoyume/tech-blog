投稿日　2023年3月21日
# LAMPをEC2にインストールする（失敗し断念）

## 失敗した方法

AWSのチュートリアルに従ってLAMPをEC2にインストールする。

参照：

<a href="https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/install-LAMP.html" target="_blank">チュートリアル: Amazon Linux AMI への LAMP ウェブサーバーのインストール</a>


Amazon Linux AMIのec2にLAMPをインストールしようとしたが、下のコマンドができなかった。

```bash
sudo yum install -y httpd24 php72 mysql57-server php72-mysqlnd

// Last metadata expiration check: 4:37:06 ago on Mon Mar 20 01:48:33 2023.
// No match for argument: httpd24
// No match for argument: php72
// No match for argument: mysql57-server
// No match for argument: php72-mysqlnd
// Error: Unable to find a match: httpd24 php72 mysql57-server php72-mysqlnd

```
原因を調べてみても、うまくいっている例が見つからなかった。
チュートリアルの記事が古いかもしれないので、断念した。

webでよくあるAmazon Linux 2のec2インスタンス上にLAMPを構成することにする。

