# dijkstra_queue
A template for manually implementing Dijkstra+ algorithms

#　実行方法
main.pyを実行すると定義した隣接行列に対応する無向グラフがmain.pyと同じディレクトリに出力される。(G.png)

アルゴリズム本体はPathFinderクラスに記述。

以下コード(main.pyの100行目)について、左に開始地点、右に目的地のパラメータをセットすると、最短経路とかかる時間(経路の重みの合計)がターミナルに出力される。

```python
print(W.dijkstra("A","B"))
print(W.dijkstra("B","A"))
print(W.dijkstra("D","C"))
print(W.dijkstra("E","F"))
print(W.dijkstra("A","D"))
```