投稿日　2023年3月21日
# chatGPTに聞きながら、Cloud9でApacheのインストール確認・起動・停止　
chatGPTに相談しながら、Cloud9でApacheを起動してホームページを作りたい。
## １、chatGPTにcloud9にはApacheがインストールされているかを確認する方法を聞いてみた。
chatGPTが教えてくれたコマンド
```bash
#間違っている
apache2 -v　　
```
このコマンドを実行すると"command not found"と返ってきた。  

Cloud9には、Apacheがインストールされてないのではないかと思い、インストール方法をweb検索した。

そうしたら、デフォルトでapacheがインストールされていることが分かった。

更に、Cloud9でApacheのインストールを確認する方法をweb検索した。
```bash
httpd -v
#Server version: Apache/2.4.55 ()
#Server built:   Feb  9 2023 18:42:11
```
このコマンドを実行して、Apacheがデフォルトでインストールされていることを確認できた。

とりあえずは、アップデートせずにこのまま進めることにした。

## ２、次にchatGPTにApacheの起動方法を聞いた。
「Cloud9には、デフォルトでApacheがインストールされており、起動する必要はありません。」と返ってきた。

更に「インストールしても起動はかかっていないよね？」と聞いてみたら、

「Cloud9では、Apacheが自動的に起動するわけではありません。手動でApacheを起動する必要があります。」

と答えてくれて、下のコマンド教えてくれた。

```bash
#間違っている
sudo service apache2 start
```

実行したら "Unit not found."と返ってきた。

次に、web検索して見つけた方法を試した。
```bash
sudo systemctl start httpd    
```
これで、Apacheを起動できた。

## 2、Apacheが起動しているか確認する方法

```bash
systemctl status httpd
```
起動していれば、Active: running　になっている。

起動していなければ、Active: inactive (dead)になる。

## ３、Apacheを停止する方法
```bash
sudo systemctl stop httpd
```
ちなみに、sudoは管理者権限がないと実行できないコマンドの先頭につける。

Apacheの起動と停止は管理者権限が必要だが、起動しているか状態を確認するだけなら必要ない。

## ４、解決した疑問点をまとめる

### ・web検索して分かったこと。
・Linuxディストリビューションによって、apache2とhttpdを使い分ける必要がある。

・Cloud9ではhttpdである。

#### serviceとsystemctlの違い
##### - service
serviceは、/etc/init.dにあるシェルスクリプトのファイルを指定し引数を与えると、シェルを実行してくれる。

例えば、service apache2 startの場合は、/etc/init.d/apache2と言うシェルスクリプトにstartと言う引数を与えることで、apache2を実行してくれる。
##### - systemctl
一方、systemctlは/lib/systemdにある各サービスの定義ファイル（.serviceファイル）に基づいて動作する。

systemctlは、Linuxシステムのサービスの管理を行うシステム管理用のツールである。

管理されるサービスに対して、起動、停止、再起動、有効化、無効化などの操作を行うことができる。



