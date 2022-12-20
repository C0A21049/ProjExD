# 第5回
## 負けるな！こうかとん（ex05/fight_kokaton.py）
### ゲーム概要
- ex05/fight_kokaton.pyを実行すると，1600x900のスクリーンに草原が描画され，こうかとんを移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
### 追加機能
- 着弾するとこうかとんの画像が切り替わる
- 着弾すると爆弾もこうかとんもすべて停止し、rキーを押すとリセットされる
- 着弾するとPress the 'r' key and try again! と表示されリセットを促す
- リセットした後にこうかとんの位置が初期設定のx:900,y:400に戻らないように修正
- ゲームしている間音楽が流れるように変更
### ToDo（実装しようと思ったけど時間がなかった）
- [ ] こうかとんに攻撃手段を与える。
- [ ] タイマー機能
### メモ
- クラスを導入するとmain関数の中が見やすくなる