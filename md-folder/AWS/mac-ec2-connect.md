投稿日　2023年3月21日
# AWSのEC2インスタンスへMacからSSH接続する（接続失敗の解決策も記載）

MAMPで作成したWebページをEC2上で公開するために、自分のMacのターミナルからEC2を操作したいので取り組んでみた。


#### AWSのコンソールにログインし、EC2ダッシュボードに移動。
ルートユーザーとしてログインした。
#### EC2インスタンスを選択し起動。EC2インスタンスのssh接続のコマンドをコピーする。

1. 選択したEC"インスタンスの2インスタンスIDをクリックし、「インスタンス概要」ページに移動する。
2. 右上にある「接続」をクリックして「インスタンスに接続」ページに移動する。
3. 「例」の下のコマンドをコピーしてターミナルで実行する。

下記のようなコマンドが、「例」の下にあるのでそれをコピー。

```bash
ssh -i key.pem ec2-user@<EC2インスタンスのパブリックDNS>
```

<コマンドの意味を簡単に説明>
- -iオプションを使用すると、SSH接続の認証に使用する秘密鍵ファイルを指定することができる。

- key.pemは秘密鍵ファイルのパス、ec2-userはログインするユーザー名である。

- EC2インスタンスを起動する際に使用したAMI（Amazon Machine Image）がAmazon Linuxの場合は、デフォルトのログインユーザー名がec2-userになる。

#### macのターミナルを開き、コピーしてきたコマンドを実行する。

4. Are you sure you want to continue connecting (yes/no/[fingerprint])?と聞かれたらyesと入力してEnterキーを押す。

5. パスワードを聞かれた場合は、自分のパソコンのログインアドレスを入力

#### SSH接続が確立されると、EC2インスタンスにログインできる。

#### SSH接続を解除するには、接続中のターミナルウィンドウで、以下のコマンドを入力。

```bash
exit
```



# 番外編：私がSSH接続で失敗した時の原因まとめ
1. ec2インスタンスが実行中かつ、ステータスチェックの項目２つに合格している必要がある。

2. キーペアを選択していないec2インスタンスにはssh接続できない。

3. ec2インスタンスのパブリックIPv4アドレスが動的割り当てなので、ec2インスタンスを停止したら次に開始した時は違うIPv4アドレスが割り振られている。

4. MacからEC2インスタンスにSSH接続するためには、EC2インスタンスのセキュリティグループでポート22が許可されている必要がある。

5. "Permissions 0644 for 'キーペアの名前' are too open."というエラーメッセージが出る。
このエラーメッセージは、秘密鍵ファイルのアクセス許可を他の人も読み取ることができるようになっているため、SSHが許可されていないことを示している。
以下のコマンドを使用して、秘密鍵ファイルのアクセス許可を修正し、再度試みたらssh接続ができた。

```bash
chmod 400 秘密鍵ファイルの名前
```

このコマンドで所有者に読み取りおよび書き込みの権限が与えられ、他の人にはアクセスできないようになる。
また、ssh接続ができるようになる。


## ＜セキュリティグループで自分のMacからのSSH接続を許可する方法＞
- EC2の「インスタンス」ページから接続したいEC2インスタンスを選択し、その詳細を表示する。
- 「セキュリティグループ」タブを選択。
- インバウンドルールを編集するために「インバウンド」タブをクリックし、下部の「ルールの追加」をクリックする。
- 「タイプ」で「SSH」を選択し、SSHを許可するIPアドレスを指定する。基本的には必要最小限の自分のIPアドレス、「マイIP」を指定する。
- 「ルールの追加」をクリックして、変更を保存する。
