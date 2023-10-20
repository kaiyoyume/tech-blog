投稿日　2023年3月22日
# AWS上にWebサーバを作成した

## EC2を立てる。
- Amazon マシンイメージはAmazon linux 2　AMI（無料枠）を選択。
- キーペアを作成。
- セキュリティグループは、
インバウンドルールはhttp、httpsはすべてのIPアドレスを許可、sshは自分のIPを許可した。  
アウトバンドルールは全面的に許可した
- 他の設定はデフォルトのままにした。

## Elastic IPアドレスをEC2に割り当てる
検索すれば記事がたくさんあるので説明は省略。

## Macからssh接続
参照：

<a href="mac-ec2-connect.html">AWSのEC2インスタンスへMacからSSH接続する（接続失敗の解決策も記載）</a>


## LAMP構成のwebサーバをEC2にインストール
AWSのチュートリアルに従ってインストールする。

<a href="https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.html" target="_blank">チュートリアル: Amazon Linux 2 に LAMP ウェブサーバーをインストールする</a>

これで、Webサーバの構築終了。
