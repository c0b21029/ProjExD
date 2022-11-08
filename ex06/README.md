# 第5回
## こうかとんに負けるな！(ex06/fight_kokaton.py)
### ゲーム概要
- ex06/fight_kokaton.pyを実行すると，500x400のスクリーンに草原が描画され，タイピングゲームが開始される
- スクリーンが表示された時点でタイマーが動き出す
- タイピングは計10回あり、内8回成功した場合はプレイヤーの勝利、7回以下は負けである
### 操作方法
- ランダムに表示される問題と同じ文章を入力する
### 実装機能
- タイピングゲームの実装
- スクリーンが表示された時点からタイマーが動き出す
- enterキーを入力したとき、表示された問題と入力した文章が同じだった場合、「正解！」と表示される。間違っていた場合、「残念！」と表示される
- backspaceキーで入力した文字を消すことができる
- 10回の内,8回正解した場合、「こうかとんに勝利」と表示される、7回以下の場合「こうかとんに負けちゃった…」と表示される
### ToDo（実装しようと思ったけど時間がなかった）
- [ ] 正解するとこうかとんが爆発するエフェクトを入れたかった。
### 参考サイト
- https://zenn.dev/takahashi_m/articles/a272cea4c3c4d7bb29e5
- https://imagingsolution.net/program/python/tkinter/widget_layout_grid/