# dijkstra_queue
A template for manually implementing Dijkstra+ algorithms

# 実行方法
main.pyを実行すると定義した隣接行列に対応する無向グラフがmain.pyと同じディレクトリに出力される。(G.png)

アルゴリズム本体はPathFinderクラスに記述。

以下コードについて、左に開始地点、右に目的地のパラメータをセットすると、最短経路とかかる時間(経路の重みの合計)がターミナルに出力される。

```python
print(W.search_path("A","B"))
print(W.search_path("A","C"))
print(W.search_path("A","D"))
print(W.search_path("A","E"))
print(W.search_path("A","F"))
print(W.search_path("A","G"))
```