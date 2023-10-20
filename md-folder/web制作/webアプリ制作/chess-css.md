投稿日 2023年04月08日
# オセロの盤面の表示のCSS

## オセロの表示はCSSのみで、可能である。
## まずはオセロの表示方法を確認する
chatGPT4に、「htmlでオセロを作りたい。まずは表示方法だけ知りたい。横並びに３つのセルがあり、１個目は中身が空白で、２個目は白の石、３個目は黒の石がある。」
と聞いたら、作ってくれた。

html:
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>オセロゲーム</title>
  <style>
    /* CSS styles */
    .container {
      display: flex;
    }

    .cell {
      width: 50px;
      height: 50px;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: darkgreen;
      border: 1px solid black;
    }

    .stone {
      width: 90%;
      height: 90%;
      border-radius: 50%;
    }

    .black {
      background-color: black;
    }

    .white {
      background-color: white;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="cell"></div> <!-- 空白のセル -->
    <div class="cell">
      <div class="stone white"></div> <!-- 白い石が入ったセル -->
    </div>
    <div class="cell">
      <div class="stone black"></div> <!-- 黒い石が入ったセル -->
    </div>
  </div>
</body>
</html>
```
border-radiusは、要素の角を丸くするために使用される。  
border-radius: 50%; の場合、要素の角が要素の半径（要素のwidthの50%）で丸くなる。  
これは、要素が正方形の場合、完全な円になることを意味する。  

## オセロの初期設定の盤面を作る
chatGPT4に「オセロの初期設定のデータを作成して、それを表示したい。」  
と聞いてみたら、作ってくれた。  
しかし、8x8の盤面の真ん中に４つ石を置いているのだが、位置が上に１行ずれている。  

「なんで、2次元配列の真ん中に石を置いてないの？」  
と聞いたが、オセロの盤面データの初期設定では、真ん中に白と黒の石を交互に置くという説明をしてくれたが、プログラムを直してくれなかった。  

「オセロの初期設定の盤面の２次元配列の石を、１行下にして」  
と明確に修正して欲しい箇所を指摘したら、直してくれた。

作ってもらったプログラムをwebページに表示してみら、ボードの右が無駄に長く、セルの枠に色がついていなかったので、そこも直してもらった。

「boardの右が無駄に長い。後、cellのborderを黒にして。」  
修正してくれたプログラムをweb表示してみたら、今度は問題なさそう。

これで、完成した。

完成バージョンのプログラムのみを載せておく。

html:
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>オセロゲーム</title>
  <style>
    .board {
      display: grid;
      grid-template-columns: repeat(8, 50px);
      grid-template-rows: repeat(8, 50px);
      gap: 1px;
      background-color: darkgreen;
      width: fit-content;
      margin: 0 auto;
    }

    .cell {
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      border: 1px solid black;
    }

    .stone {
      width: 90%;
      height: 90%;
      border-radius: 50%;
    }

    .black {
      background-color: black;
    }

    .white {
      background-color: white;
    }
  </style>
</head>
<body>
  <div class="board" id="board"></div>

  <script>
    const boardElement = document.getElementById("board");
    const initialBoard = [
      ['', '', '', '', '', '', '', ''],
      ['', '', '', '', '', '', '', ''],
      ['', '', '', '', '', '', '', ''],
      ['', '', '', 'black', 'white', '', '', ''],
      ['', '', '', 'white', 'black', '', '', ''],
      ['', '', '', '', '', '', '', ''],
      ['', '', '', '', '', '', '', ''],
      ['', '', '', '', '', '', '', '']
    ];

    function createCell(color) {
      const cell = document.createElement("div");
      cell.classList.add("cell");

      if (color) {
        const stone = document.createElement("div");
        stone.classList.add("stone", color);
        cell.appendChild(stone);
      }

      return cell;
    }

    function renderBoard(boardData) {
      boardElement.innerHTML = '';
      
      boardData.forEach(row => {
        row.forEach(color => {
          const cell = createCell(color);
          boardElement.appendChild(cell);
        });
      });
    }

    renderBoard(initialBoard);
  </script>
</body>
</html>
```
