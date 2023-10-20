投稿日 2023年03月31日
# ファイルツリーのフォルダ名をクリックしたらフォルダ名の前の矢印の向きが切り替わるようにする。

ファイルツリーのフォルダ名のspanタグの左側に矢印をつけたい。  
フォルダ名をクリックすると矢印の向きが切り替わるするようにしたい。

## まずは簡単な例で、spanタグに矢印をつける方法を理解する。

矢印をspanタグの左側に追加するには、styleタグの::before疑似要素を使用する。  
::before疑似要素は、要素の内容の前に装飾を追加するために使用する。

この例では、.arrow-rightクラスが適用された<span>要素の左側に、矢印（▶︎）を追加している。margin-rightプロパティを使って、矢印とテキストの間のスペースを調整できる。

矢印のデザインやスタイルはカスタマイズできる。


```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Arrow Left Example</title>
  <style>
    .arrow-right::before {
      content: "▶︎";
      margin-right: 5px; /* 矢印とテキストの間のスペースを調整する */
    }
  </style>
</head>
<body>
  <span class="arrow-right">Text with arrow on the left</span>
</body>
</html>
```

# 矢印の向きが入れ替わるようにしていく。クリック時にクラスを切り替えて矢印の方向を変更する
#### styleタグの説明
styleタグで右向き（▶︎）と下向き（▼）の２つの::before疑似要素を用意する。

矢印のデフォルトスタイル（▶︎）と、arrow-downクラスが適用された場合のスタイル（▼）を定義している。

#### htmlのbodyの説明
フォルダ名のspanタグには、デフォルトの右向きの矢印（▶︎）を付加する。

#### scriptタグの説明
constは、定数の宣言に使用される。  
idが"arrowElement"の要素のデフォルトのスタイルを取得し、arrowElementと名付ける。

arrowElement.addEventListener('click',関数);とは、arrowElementのクリック時に関数を実行するイベントリスナーである。

arrowElement.classList.toggle('arrow-down')は、arrowElementという要素のクラスリストにarrow-downというクラス名が存在する場合は削除し、存在しない場合は追加するという操作を行う。

※タグには複数のリストを付加できる。クラスリストと呼ぶ。  
※toggleとは、日本語訳すると「機能や状態のON/OFFを切り替える仕組み」である。

arrowElementに'arrow-right'と'arrow-down'両方のクラスが適用されている時、片方の矢印しか表示されない。  
かつ、後に記述されたルールが優先されので、Webページでは矢印の向きが切り替わる。

優先度の説明は長くなるので、コードの下に書く。

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Toggle Arrow Example</title>
  <style>
    .arrow-right::before {
      content: "▶︎";
      margin-right: 5px;
    }

    .arrow-down::before {
      content: "▼";
    }
  </style>
</head>
<body>
  <span class="arrow-right" id="arrowElement">Click to toggle arrow direction</span>

  <script>
    const arrowElement = document.getElementById('arrowElement'); 
    arrowElement.addEventListener('click', () => {
      arrowElement.classList.toggle('arrow-down');
    });
  </script>
</body>
</html>
```

## arrowElementに'arrow'と'arrow-down'両方のクラスが適用されている時、片方の矢印しか表示されないのはなぜか。
これは、CSSのカスケード（継承）と特異性（詳細度）の仕組みによって決まる。

CSSでは、複数のスタイルルールが同じ要素に適用される場合、特異性という概念に基づいてルールの優先順位が決まる。  
特異性が高いルールほど、適用される確率が高くなる。  
特異性は以下のように計算される。  

1. インラインスタイル（要素のstyle属性に直接記述されたスタイル）が最も高い特異性を持つ。
2. セレクタの中でIDセレクタ（#id）の数が次に高い特異性を持つ。
3. セレクタの中でクラスセレクタ（.class）、属性セレクタ（[attr]）、および疑似クラス（:pseudo-class）の数が次に高い特異性を持つ。
4. セレクタの中で要素セレクタ（element）および疑似要素（::pseudo-element）の数が最も低い特異性を持つ。

上のコードでは、.arrow-right::beforeと.arrow-down::beforeの2つのスタイルルールがある。
両方ともクラスセレクタと疑似要素を使用しているため、特異性は同じである。

特異性が同じ場合、後に記述されたルールが優先される。

arrowElementにarrow_rightとarrow-downの両方のクラスが適用されている場合、.arrow-down::beforeルールが優先されるため、矢印は下向きに表示される。  
.arrow::beforeルールは上書きされ、表示されない。



### （感想）
要素に複数のclassを付加できることを知らずclasslistの意味が最初は分からなかった。  
toggleについても知らなかったので戸惑った。