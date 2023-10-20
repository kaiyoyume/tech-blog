投稿日 2023年03月21日
# PDOを使ってMySQLのテーブルをPHPファイルのWebページに表示してみた

## まずphpファイルを作成してwebブラウザで表示できることを確認する。
1. MAMPを起動。
2. htmlファイルの雛形を用意。
3. VSCodeを起動して、MAMPのhtdocsフォルダを開く。
4. 新規ファイルを作成し、htmlファイルの雛形をコピペしてhdoc.phpという名前で保存。
5. chromeの検索バーで"http://localhost:8888/hdoc.php" を検索。表示されることを確認。

という手順で行った。

htmlファイルの雛形
```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>ページタイトル</title>
</head>
<body>
	<h1>見出し1</h1>
	<p>段落1</p>
	<h2>見出し2</h2>
	<p>段落2</p>
</body>
</html>
```

## 次に、MySQLのテーブルの表示に必要なコードを挿入する
hdoc.phpのbodyの段落1を消して、MySQLのテーブルの表示に必要なコードを挿入。

＜MySQLサーバーへの接続に必要な指定＞
- ホスト名、ユーザー名、パスワードはデフォルトだと"localhost"、"root"、"root"である。   
- portは、MySQLのデフォルトのポート番号は8889を設定している。  
MAMPでMySQLのポート番号を確認するには、MAMPアプリの画面左上の"Preferences"を選択する。"Ports"タブを選択して、MySQLのポート番号を確認できる。  
- dbnameは、接続したいデータベースの名前を選択する。

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>ページタイトル</title>
</head>
<body>
	<h1>見出し1</h1>
  <?php
    // MySQLサーバーへの接続
    $servername = "localhost"; // ホスト名
    $username = "root"; // ユーザー名
    $password = "root"; // パスワード
    $port = 8889; 
    $dbname = "shirokuma"; // データベース名

    try {
        $conn = new PDO("mysql:host=$servername;port=$port;dbname=$dbname", $username, $password);
        // PDOエラーモードを例外モードに設定
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        echo "Connected successfully"." <br>";
        echo "<br>";
        $stmt = $conn->prepare("SELECT * FROM menu");
        $stmt->execute();
        // set the resulting array to associative
        // 結果を取得
         $result = $stmt->fetchAll();

        // 結果を表示
        echo "price  menu"."<br>";
    foreach($result as $row) {
        echo $row['name']." ".$row['price']."円<br>";
        }
    } catch(PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }
    ?>
  
	<h2>見出し2</h2>
	<p>段落2</p>
</body>
</html>
```
chromeの検索バーで"http://localhost:8888/hdoc.php" を検索して、表示されることを確認する。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3268288/4c5f6599-e758-1a20-b2b1-5513d0cffae6.png" alt="説明テキスト" width="600" height="400" />

