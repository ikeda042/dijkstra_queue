import java.nio.file.Path;
import java.util.*;
public class PathFinder {
    HashMap<String,Node> nodes;
    String[] stringNodes;

    public PathFinder(HashMap<String,Double> paths, String[] stringNodes){
        this.stringNodes = stringNodes;
        this.nodes = new  HashMap<String,Node>();

        for (int i = 0; i < stringNodes.length; i++) {
            this.nodes.put(stringNodes[i], new Node(stringNodes[i]));
        }
         
        String entryString;
        for (Map.Entry<String,Double> entry : paths.entrySet()){
            entryString = entry.getKey();
            this.nodes.get(entryString.charAt(0)+"").setAdj(entryString.charAt(3)+"",   entry.getValue());
        }

    }

    public void search(String starNode, String endNode){
        //到達距離を無限遠に初期化
        for (int i = 0; i < stringNodes.length; i++) {
            this.nodes.get(stringNodes[i]).setD(Double.POSITIVE_INFINITY);
        }
        
        //キューを初期化
        Queue<String> queue = new LinkedList<String>();
        queue.add(starNode);
        //currNodeを初期化
        String currNode = queue.peek();
        this.nodes.get(starNode).setD(0);
        //初期ノードのprevNodeを初期化
        this.nodes.get(currNode).setPrev(null);
        
        //探索開始
        while (queue.size() > 0){
            currNode = queue.remove();
            
            HashMap<String,Double> adjs = this.nodes.get(currNode).getAdj();

            for (Map.Entry<String,Double> entry : adjs.entrySet()){
                if (entry.getValue() != 0.0){
                    double tmpD = this.nodes.get(currNode).getD() + (double) this.nodes.get(currNode).getAdj().get(entry.getKey());
                    if (this.nodes.get(entry.getKey()).getD() > tmpD){
                        this.nodes.get(entry.getKey()).setD(tmpD);
                        this.nodes.get(entry.getKey()).setPrev(this.nodes.get(currNode));
                        this.nodes.get(entry.getKey()).setExplored(true);
                        queue.add(entry.getKey());
                    }
                }
               
            }
        }

        
        Node node = this.nodes.get(endNode);

        //バックトラックの開始
        LinkedList<String> s = new LinkedList<String>();
        s.add(endNode);
        
         while(node.getPrev() != null){
            node = node.getPrev();
            s.add(node.getName());
        }

        while(!s.isEmpty()) {
            System.out.print(s.remove(s.size()-1) + "->");

        }
        System.out.println();
        System.out.println(this.nodes.get(endNode).getD());


        
        
        


        
    }




    public static void main(String[] args) {
        int[][] D = { 
            {0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0}, 
            {3, 0, 0, 0, 0, 0, 0}, 
            {0, 1, 4, 0, 0, 0, 0}, 
            {0, 2, 1, 0, 0, 3, 0}, 
            {2, 6, 2, 0, 0, 0, 0}, 
            {0, 2, 0, 0, 0, 5, 0} 
        };

        int[][] DT = new int[D.length][D.length];

        for (int i = 0; i < DT.length; i++) {
            for (int j = 0; j < DT.length; j++) {
                    DT[i][j] = D[j][i];
            }
        }
        
        String[] nodeStrings = new String[D.length];
        for (int i = 0; i < nodeStrings.length; i++) {
            nodeStrings[i] = ((char) (i+97) +"").toUpperCase();
        }

        //全経路と重みの取得
        HashMap<String,Double> allPaths = new HashMap<String,Double>();

        double[][] G = new double[D.length][D.length];
        for (int i = 0; i < G.length; i++) {
            for (int j = 0; j < G.length; j++){
                if (i != j){
                    G[i][j] = D[i][j] + DT[i][j];
                    allPaths.put(nodeStrings[i] + "->" + nodeStrings[j],G[i][j]);
                    System.out.println(nodeStrings[i] + "->" + nodeStrings[j] + " " + G[i][j]);
                }
               
            }
            
        }


        PathFinder p = new PathFinder(allPaths, nodeStrings);
        p.search("A", "B");
    }


}
