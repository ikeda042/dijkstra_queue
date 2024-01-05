import random
import numpy as np
from typing import cast
class AdjNode:
    def __init__(self, weight: int, is_Barrier_free: bool) -> None:
        self.weight: int = weight
        self.is_Barrier_free: bool = is_Barrier_free
    
    def __repr__(self) -> str:
        return f"{self.weight}"

def transpose(G:list[list[AdjNode]]) -> list[list[AdjNode]]:
    rows = len(G)
    cols = len(G[0])
    G_T = [[None for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            G_T[j][i] = G[i][j]
    return G_T

def add_matrices(G, T):
    rows = len(G)
    cols = len(G[0])
    result = [[None for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if cast(AdjNode,G[i][j]).weight != 0:
                result[i][j] = G[i][j]
            elif cast(AdjNode,T[i][j]).weight != 0:
                result[i][j] = T[i][j]
            else:
                result[i][j] = G[i][j]
    return result

def generate_random_G(R:int) -> np.ndarray:
    random.seed(10)
    weights_cs = [0]*50 + [1]*4 + [2]*2 + [3]*2 + [3]*6 + [4]*3 + [5]*6
    p = [-1]*5 + [1]*21
    def get_weight():
        return random.choice(weights_cs) * random.choice(p)
    G : list[AdjNode] = [[AdjNode(0,False) for i in range(R)] for j in range(R)]
    for i in range(R):
        for j in range(R):
            if i == j or i < j:
                continue
            w = get_weight()
            cast(AdjNode,G[i][j]).weight = abs(w)
            cast(AdjNode,G[i][j]).is_Barrier_free = True if w > 0 else False
    return  G



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
            self.nodes[i.split("->")[0]].adj[i.split("->")[1]] = all_paths[i]
        print("##########")
        print(self.nodes)
    def search_path(self,startNode:str,endNode:str):

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
    
        #Backtrack
        s:list[str] = [endNode]
        while cNode.prevNode != None:
            cNode = cNode.prevNode
            s.append(cNode.name)

        return [s[::-1],self.nodes[endNode].d]