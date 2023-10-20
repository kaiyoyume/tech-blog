投稿日 2023年03月22日
# ２台のMacを公開鍵暗号方式でssh接続した

AWSのEC2をMacのターミナルから操作したいと思い、練習としてmac同士をssh接続してみた。

####  まず２台のMacの役割の割り振りを決める。
私は家族に借りたMacをサーバ、自分のMacをクライアントと定めた。

#### まず、接続先のMacにリモートログインを許可する必要がある。
「システム環境設定」を開き、「共有」をクリックし、左側のサイドバーで「リモートログイン」を選択する。  

そこで、リモートログインを許可するユーザーアカウントを選択する。

#### 公開鍵と秘密鍵の生成
接続元のMacで公開鍵と秘密鍵を生成する。
次のコマンドを使用して、鍵を生成する。
```bash
ssh-keygen -t rsa
```
このコマンドを実行すると、鍵の生成場所を尋ねられる。
デフォルトの場所（/Users/ユーザ名/.ssh）にした。

もし、.sshフォルダがなければ作る。検索したら簡単に作れるので省略する。

#### 公開鍵の転送
次に、接続先のMacに公開鍵を転送する必要がある。
次のコマンドを使用して、公開鍵を転送する。
```bash
ssh-copy-id <接続先のユーザ名>@<接続先のIPアドレス>
```
このコマンドを実行すると、接続先のMacにログインするためのパスワードが求められる。
接続先のMacのログインパスワードを入力する。

接続先のユーザ名は、接続先のMacのターミナルウィンドウで'whoami'と入力すれば確認できる。  

接続先のIPアドレスは、接続先のMacの「システム環境設定」→「ネットワーク」→「詳細」→「TCP/IP」に載っているIPv4アドレスを入力する。


#### SSH接続
公開鍵が転送されたら、接続先のMacにSSH接続できる。
```bash
ssh <接続先のユーザ名>@<接続先のIPアドレス>
```
このコマンドを実行すると、公開鍵を使用して接続先のMacに自動的にログインされる。


#### SSH接続を終了
以下のコマンドを実行する
```bash
exit
```