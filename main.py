from graphviz import Graph
from components import PathFinder, AdjNode, transpose, add_matrices, generate_random_G
from typing import cast

#隣接行列の生成
G = generate_random_G(15)

#グラフインスタンスの初期化
GraphvizObject = Graph(format="png")
GraphvizObject.attr("node", shape="circle")

#隣接行列を無向グラフに変換
G : list[AdjNode] = add_matrices(G, transpose(G))

#ノードの文字列を生成(例: A,B,C,D,E,F,G...) + 各エッジの重みを初期化
nodes, path_weights = [str(chr(i).upper()) for i in range(97,len(G)+97)], {}

#GraphvizObjectにノード、エッジを追加
for i in range(len(G)):
    for j in range(len(G[0])):
        #エッジの重みが0の時はエッジがないとみなす
        if cast(AdjNode,G[i][j]).weight != 0:
            path_weights[f"{nodes[i]}->{nodes[j]}"] = G[i][j]
            #無向グラフなので、i>jのときはエッジを追加しない
            if i>j:
                #非バリアフリー経路を赤色で描画、それ以外を黒色で描画
                GraphvizObject.edge(str(nodes[i]),str(nodes[j]),label=str(cast(AdjNode,G[i][j]).weight),color='black' if cast(AdjNode,G[i][j]).is_Barrier_free else 'red')
GraphvizObject.render("G")

path_weights : dict[str,int] = {i: cast(AdjNode,path_weights[i]).weight for i in path_weights.keys() if cast(AdjNode,path_weights[i]).is_Barrier_free}
print(path_weights)
W = PathFinder(path_weights,nodes)

print(W.search_path("A","B"))
print(W.search_path("A","C"))
print(W.search_path("A","D"))
print(W.search_path("A","E"))
print(W.search_path("A","F"))
print(W.search_path("A","G"))





