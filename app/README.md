# Earthquakerアプリについて

## 必要環境

Python3が動き，以下のモジュールが入っている環境
1. fcn
2. torch
3. eel
4. ntplib

(1,2は予測のために3,4はGUIの利用のために必要です．3,4は pip installでいれられます
[EELについての参考Qiita](https://qiita.com/_dack_/items/e69e2d240a00ff08d10e))

## 実行方法

ビルドした後のアプリは重くてGitHubに上がらなかった上に，パス等を書き換えて再ビルドする必要があり大変そうだったので，再現用にシェルスクリプトを書きました．

Earthquaker/app/Earthquaker.sh
がそのファイルになります．


__ただし，アプリ実行に利用する学習済みデータ，「Earthquaker/app/web/python/model_13」が重くてGitHubにあげられなかったため，再度学習して配置していただくか，[人工知能第二ターム共有用Googleドライブ](https://drive.google.com/file/d/1f4XASTDSxmUR9bWc5vx17uN6QSfRgP86/view?usp=sharing) から取得してEarthquaker/app/web/python/model_13と配置してください__

以上のことがうまくいっていれば，
```bash
bash Earthquaker.sh
```
でアプリが起動するはずです．

## 注意点

* 起動が遅い

  Python-eelが重めなのでご容赦ください...

* RUNしても結果が変わらない(もしくは正しくなさそう)
  
  通信ラグ(？)の影響で一個前の実行結果を表示している場合があります．もう一度RUNしていただけると正しく表示されるはずです．

* ターミナルにいろいろ出力される

  入力検知や，データ受け渡しをプリントデバッグしたものをあえてそのままにしてあります．すみません．

