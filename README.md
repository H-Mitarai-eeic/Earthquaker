# Earthquaker

## データについて

学習に使用したデータのみこのリポジトリに挙げています。元データや成形用のコードなどは以下のリンクからどうぞ。学習のために，下のリンクのレポジトリからデータを持ってくる必要はありません．

https://github.com/H-Mitarai-eeic/Earthquake_Data

## 学習

istクラスタ上にこのレポジトリをcloneし，ターミナルで
```
$ cd AI
$ sbatch train.sh
```
とすると学習が始まり，`result`ディレクトリに生成されたモデルが入ります．

## テスト

続いて，
```
$ sbatch test.sh
```
とすると`result`ディレクトリ内の`model_1`をモデルとしてテストをします．出力はistクラスタの仕様で，`.out`としてAIディレクトリ内に出ます．

`test.sh`内の`model_1`の部分を好きな番号に変更することで，そのモデルでテストできます．

## 予測
続いて，
```
$ bash predict.sh
```
とすると，震源の座標$x=30$，$y=30$，深さ20km，マグニチュード8での予測が始まります．結果はAIディレクトリの中に，`predicted_data.csv`として出力されます．震源の座標等は，`predict.sh`の中身を変更して変えることができます．

## アプリについて

アプリについては，appディレクトリ内に別にreadmeが書かれています．[こちら](https://github.com/H-Mitarai-eeic/Earthquaker/tree/main/app#earthquaker%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)


(11/26追記)

授業時間外ではあるのですが，Python eelによるアプリ化から，ウェブアプリ化を意識したserver&clientで動く様なUIも作りました．
appClientAndServerに入っています．

詳しくは[こちら](https://github.com/H-Mitarai-eeic/Earthquaker/tree/main/appClientAndServer#earthquakerhttp%E9%80%9A%E4%BF%A1%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3)

node.jsが入っている場合は，こちらの方が軽量で再現実行が楽だと思われます．
(ただし，11/26日現在，結果保存機能が壊れている不具合があります．(通信ポリシーに反する的なエラー))