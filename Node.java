import java.util.*;
public class Node{

    String name;
    HashMap<String,Integer> adj;
    double d; 
    boolean explored;
    Node prev;

    public Node(String name){
        this.name = name;
        this.adj = new HashMap<String,Integer>();
        this.d = Double.POSITIVE_INFINITY;
        this.explored = false;
        this.prev = null;
    }

    public void setAdj(String adjNodeName,int d){
        this.adj.put(adjNodeName, d);
    }

    public void setExplored(boolean e){
        this.explored = e;
    }

    public void setD(double d){
        this.d = d;
    }

    public void setPrev(Node prev){
        this.prev = prev;
    }

    public HashMap<String,Integer> getAdj(){
        return this.adj;
    }

    public double getD(){
        return this.d;
    }

    public Node getPrev(){
        return this.prev;
    }

    public String getName(){
        return this.name;
    }

    public String toString(){
        return this.name;
    }
}