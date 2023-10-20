投稿日 2023年04月02日
# alias設定を使い、Python コマンドで Python 3 が実行されるようにする

Macのターミナルのpythonコマンドをpython3にalias設定して、pythonと入力するとPython3が実行されるようにする。

# 一時的なaliasを作成したい場合
aliasコマンドを実行すると、現在のセッションでのみ有効なaliasが作成される。

```bash
alias python='python3'
```

# 永続的なaliasを作成したい場合。
## 1. ~/.zshrcファイルにaliasを追加する
aliasを永続的に保存するには、設定ファイルに追加する必要がある。
```bash
echo "alias python='python3'" >> ~/.zshrc

```
このコマンドは、設定ファイル（.zshrc）の末尾に新しいaliasを追加する。

## 2. 設定ファイルを更新するために、sourceコマンドを使用して、変更を再読み込みする
```bash
source ~/.zshrc
```
この方法で新しいエイリアスがすぐに適用される。
ターミナルを閉じて開き直しても新しいエイリアスが適用されている。


## ＜補足＞
ターミナルでコマンドを実行する際、aliasは通常のコマンドよりも優先される。
python2を実行する必要がある場合は、'python2'と入力すればよい。