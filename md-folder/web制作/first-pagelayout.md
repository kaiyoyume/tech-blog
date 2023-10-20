投稿日 2023年03月23日
# ページレイアウトを設計する

div要素にstyleを記述して配置する方法では、HTMLページのレイアウトが思い通りにならなかった。

だから、chatGPTに聞きながら、HTMLページを作成することにした。

私「htmlページの画面レイアウトが、思い通りできなくて困っている。簡単にできるレイアウトの手法を教えて。」

chatGPT「・・・、CSSのFlexboxとGrid Layoutがあります。・・・」

Grip Layoutを採用することにした。

## chatGPTに二回問いかけて、提示してくれたプログラムを１行だけ自分で書き直して使った。
指示１「bodyは、画面いっぱいの大きさにする。Grid Layoutでヘッダー、コンテンツエリア、フッターがある。各幅は画面いっぱいにする。位置は順序通りにする。」

指示２「body要素を2x2のグリッドに分割して」

htmlファイル
```html
<div class="grid-container">
  <div class="grid-item header">Header</div>
  <div class="grid-item sidebar">Sidebar</div>
  <div class="grid-item content">Content Area</div>
  <div class="grid-item footer">Footer</div>
</div>
```
cssファイル
```css
.grid-container {
  display: grid;
  /*grid-template-columns: 1fr 1fr; chatGPTは均等に分けたので、左を200pxに固定に修正する*/
  grid-template-columns: 200px auto;　/*手修正*/
  grid-template-rows: auto 1fr;
  height: 100vh;
}

.grid-item {
  padding: 20px;
  box-sizing: border-box;
}

.header {
  background-color: #ccc;
  grid-column: 1 / span 2;
}

.sidebar {
  background-color: #eee;
  grid-row: 2 / span 1;
}

.content {
  background-color: #fff;
  grid-row: 2 / span 1;
  grid-column: 2 / span 1;
}

.footer {
  background-color: #ccc;
  grid-column: 1 / span 2;
}
```
webに表示してみると

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3268288/16a6e2a9-658a-a6e3-27d6-148f9948aa18.png" alt="説明テキスト" width="600" height="400" />

## 注意書き
何度も指示の仕方を試行錯誤してうまくいった場合を書いた。  
gridの最終的な行列分割を指定すると上手くいく。
