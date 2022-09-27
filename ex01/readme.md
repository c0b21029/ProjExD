# 第一回
## アルファベットクイズ(ex01/alphabet.py)
### 遊び方
* コマンドラインでalphabet.pyを実行すると、標準出力に問題が表示される。
* 標準入力から答えを入力する
* 初めに欠損文字の個数を聞かれる。
* 欠損文字の個数が正解だった場合、欠損文字を聞かれる。
* すべて正解なら「欠損文字も含めて完全正解です！！！」と表示される
### プログラム内の解説
* shutudai関数は全アルファベットから，対象文字をランダムに10文字選び、対象10文字から，欠損文字をランダムに2文字選ぶ。
* kaito関数は、正解かどうかを返す