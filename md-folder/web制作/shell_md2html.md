投稿日 2023年03月22日
# ディレクトリ内のMarkdownファイルを全てHTMLに変換するシェルスクリプトを作る

- 指定されたディレクトリ内のMarkdownファイルをHTMLに変換するためのスクリプトを作る。

- 変換されたHTMLファイルは、元のMarkdownファイルと同じディレクトリに保存される。

- 変換後のHTMLファイルがすでに存在していて、元のMarkdownファイルよりも新しい場合は変換しないようにしている。

以下のコードをsh拡張子のファイルで保存する。
```bash
#シェルの宣言
#!/bin/bash　

#パラメータとして渡されたディレクトリを変数directoryに格納
directory=$1

#ディレクトリが指定されていない場合、スクリプトの使用方法を出力して、スクリプトを終了
if [ -z "$directory" ]
then
    echo "Usage: convert_md_to_html.sh [directory]"
    exit 1
fi

#forループを使用して、ディレクトリ内のMarkdownファイルを１つずつ処理
for file in "$directory"/*.md; do
    html_file="${file%.md}.html" #変換後のHTMLファイル名を作成

    #変換後のHTMLファイルがすでに存在、かつ元のMarkdownファイルよりも新しい場合は、処理をスキップ
    if [ -e "$html_file" ] && [ $(date -r "$html_file" +%s) -ge $(date -r "$file" +%s) ]; then
        echo "Skipping $file - $html_file already exists and is newer than $file"
    else
        pandoc -s "$file" -o "$html_file"    #MarkdownファイルをHTMLに変換
        echo "Converted $file to $html_file" #処理されたファイル名を表示
    fi
done
```


## このシェルスクリプトの使い方
私はmdフォルダを作り、Markdown形式のファイルをそこに保存している。
上のシェルスクリプトもchange.shという名前でMarkdownフォルダ内に保存する。
Macのターミナルで、mdフォルダに移動して以下のコマンドを実行。
```bash
sh change.sh .
```
これで、mdフォルダ内のMarkdownファイルを変換できる。