投稿日 2023年03月30日
# ファイルツリー全体にonclick属性を付加する。ツリーの中のどの要素がクリックをされたのかを特定する方法の下調べ

## 結論
event.targetを使えば簡単に書ける。  
ファイルツリーにはフォルダとファイルがある。  
それぞれに、クラス名（class="folder"、class="file"）を付加する。  
onclickが発生すると、要素を特定する。  
要素のクラスを見て、処理を変える。  
ファイル（class="file"）の場合は、テキストを取り出してmainに表示する。  
フォルダ（class="folder"）の場合は、表示をtoggleする。  

displayのプロパティnoneと、blockをtoggleする。

## targetの使い方の例

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple Block Element with OnClick</title>
  <script>
    function handleDivClick(event) {
      const target = event.target;

      if (target.tagName === 'BUTTON') {
        alert(`You clicked on: ${target.textContent}`);
      }
    }
  </script>
</head>
<body>
  <div id="container" onclick="handleDivClick(event)" style="border: 1px solid black; padding: 20px;">
    <button id="button1">Button 1</button>
    <button id="button2">Button 2</button>
  </div>
</body>
</html>
```
