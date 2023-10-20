投稿日 2023年03月21日
# MacでMAMPのMySQLを操作する方法を一通り説明する

MySQLの起動→データベース作成→テーブル作成→テーブル削除→データベース削除→MySQLの停止の順で説明する。

MacでMAMPのMySQLを操作する方法を一通り知りたい場合は、下記のコードを上から順に実行していくと良い。

## １、MAMPアプリケーションを開き、STARTボタンを押して、起動する。

## ２、Macのターミナルを開き、mysqlのパスに移動して、MySQLを起動する。
方法１か方法２を実行する。

mysqlのユーザ名とパスワードはデフォルトでは、rootである。
MySQLのパスワードを設定していない場合は、""かEnterだと勘違いしていたので手間取った。

### 方法１
```bash
% cd /Applications/MAMP/Library/bin/
% ./mysql -u root -p
// Enter password: ←MySQLのパスワードを設定していない場合はroot
//Welcome to the MySQL monitor
```
これでMySQLが起動できた。

### 方法2
MySQLのホストとポート番号を指定する。
```bash
% cd /Applications/MAMP/Library/bin/
% ./mysql --host = localhost -uroot -proot -P8889
```

## 2,データベースを見る
```sql
SHOW DATABASES;
```
## 3,データベースを作成
database_nameという名前のデータベースを作成
```sql
CREATE DATABASE database_name;
```
## 4,特定のデータベースを使用する
USE文を使って、現在の作業用データベースを指定できる。
以降のSQL文は、このデータベース上で実行される。
database_nameを作業用データベースとして設定する場合は以下のコードを実行する。
```sql
USE database_name;
```


## 5,データベースにテーブルを作成
４の通りにdatabase_nameという名前のデータベースに移動した状態で、table_nameテーブルを作る。

テーブルはデータベースに所属していてデータベース内で一意である。テーブルの操作を行うには、どのデータベースに所属しているテーブルなのかを明確にする必要がある。

```sql
CREATE TABLE table_name (
       id INT,
       name VARCHAR(50),
      );
```
table_nameという名前のテーブルに、idとnameという2つのカラムを定義した。  
idは整数型(INT)、nameは文字列型(VARCHAR)にした。

## 6,テーブルのカラムを確認
```sql
DESC table_name;
```

## 7,テーブルにデータを挿入する
```sql
INSERT INTO table_name (id, name) VALUES (1, 'yume');
```
## 8,テーブルのデータを見る
```sql
SELECT * FROM table_name;
```
*を使用することで、すべてのカラムのデータが取得される。
特定のカラムだけを指定することも可能。

## 9,テーブルを削除
```sql
　DROP TABLE table_name;
```
## 10,データベースを削除
```sql
DROP DATABASE database_name;
```

## 11,MySQLサーバーを停止
```sql
exit;
```

## 番外編、MySQLのステータス確認方法
ステータス情報には、MySQLサーバーのバージョン、現在のデータベース名、現在のユーザ、接続されているクライアントのIPアドレスなどの情報が含まれている。
```sql
status;
```