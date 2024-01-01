import matplotlib.pyplot as plt
import networkx as n 
import numpy as np 
from graphviz import Graph
import os 

os.system("pip install matplotlib")
os.system("pip install networkx")
os.system("pip install numpy")
os.system("pip install graphviz")


G = np.array([
    #A  B  C  D  E  F  G
    [0, 0, 0, 0, 0, 0, 0], #A
    [0, 0, 0, 0, 0, 0, 0], #B
    [3, 0, 0, 0, 0, 0, 0], #C
    [0, 1, 4, 0, 0, 0, 0], #D
    [0, 2, 1, 0, 0, 0, 0], #E
    [2, 6, 2, 0, 3, 0, 0], #F
    [0, 2, 0, 0, 0, 5, 0]  #G
])

G += np.transpose(G)
G2 = Graph(format="png")
G2.attr("node", shape="circle")
nodes = [str(chr(i).upper()) for i in range(97,104)]
path_weights = {}
for i in range(len(G)):
    for j in range(len(G[0])):
        if G[i][j] != 0:
            G2.edge(str(nodes[i]),str(nodes[j]),label=str(G[i][j]))
            path_weights[f"{nodes[i]}->{nodes[j]}"] = G[i][j]
G2.render("G")


class Node:
    def __init__(self,name:str) -> None:
        self.name:str = name
        self.adj:dict[str,int] = {}
        self.d:float = float('inf')
        self.explored:bool = False
        self.prevNode:Node | None = None
    
    def __repr__(self) -> str:
        return self.name

    def set_explored(self,e:bool) -> None:
        self.explored = e

    def set_d(self,d:int) -> None:
        self.d = d 

class PathFinder:
    def __init__(self,all_paths:dict[str,int],nodes_string:list[str]) -> None:
        self.nodes_string: list[str] = nodes_string
        self.nodes:dict[str,Node] = {i:Node(i) for i in nodes_string}
        for i in all_paths.keys():
            self.nodes[i[0]].adj[i[3]] = all_paths[i]
    
    def dijkstra(self,startNode:str,endNode:str):

        #最短距離を無限大に初期化
        for i in self.nodes.keys():
            self.nodes[i].d = float('inf')

       
        queue:list[str] = [startNode]
        #currNodeを初期化
        currNode: str = queue[0]
        #currNodeの距離を初期化
        self.nodes[currNode].set_d(0)
        #初期ノードのprevNodeを初期化
        self.nodes[currNode].prevNode = None


        while len(queue) >0:
            currNode = queue.pop(0)
            adjs = self.nodes[currNode].adj
            for i in adjs.keys():
                tmp_d:float = self.nodes[currNode].d + self.nodes[currNode].adj[i]
                if self.nodes[i].d > tmp_d:
                    #スタートノードからの最短到達距離を更新
                    self.nodes[i].set_d(int(tmp_d))
                    self.nodes[i].prevNode = self.nodes[currNode]
                    self.nodes[i].set_explored(True)
                    queue.append(i)
        cNode:Node = self.nodes[endNode]
    
        #バックトラック
        s:list[str] = [endNode]
        while cNode.prevNode != None:
            cNode = cNode.prevNode
            s.append(cNode.name)

        return [s[::-1],self.nodes[endNode].d]

W = PathFinder(path_weights,nodes)

print(W.dijkstra("A","B"))
print(W.dijkstra("B","A"))
print(W.dijkstra("D","C"))
print(W.dijkstra("E","F"))
print(W.dijkstra("A","D"))

