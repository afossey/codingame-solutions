import java.util.*;
import java.io.*;
import java.math.*;
import java.util.stream.*;

# https://www.codingame.com/ide/puzzle/skynet-revolution-episode-1

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player {
    
    static List<Node> level = new ArrayList<>();
    static boolean hasLinkBeenSevered;
    static List<Node> visitedNodes; 
    static Node lastParentNode;
    
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt(); // the total number of nodes in the level, including the gateways
        int L = in.nextInt(); // the number of links
        int E = in.nextInt(); // the number of exit gateways
        //List<Node> exitNodes = new ArrayList<>();
        IntStream.rangeClosed(0, N-1).forEach(i -> level.add(new Node(i)));
        
        for (int i = 0; i < L; i++) {
            int N1 = in.nextInt(); // N1 and N2 defines a link between these nodes
            Node node1 = getNode(N1);
            int N2 = in.nextInt();
            Node node2 = getNode(N2);
            node1.links.add(node2);
            node2.links.add(node1);
        }
        for (int i = 0; i < E; i++) {
            int EI = in.nextInt(); // the index of a gateway node
            Node exit = getNode(EI);
            exit.isExit = true;
            System.err.println("Exit gateway : " + EI);
            System.err.println("Exit links : " + exit.links);
           // exitNodes.add(exit);
        }

        // game loop
        while (true) {
            visitedNodes = new ArrayList<>();
            hasLinkBeenSevered = false;
            int SI = in.nextInt(); // The index of the node on which the Skynet agent is positioned this turn
            System.err.println("Agent node : " + SI);
            // To debug: System.err.println("Debug messages...");
            Node agentNode = getNode(SI);
            lastParentNode = getNode(0);
            List<Node> startBFS = new ArrayList<>();
            startBFS.add(agentNode);
            findAndSeverOneLinkToExitBFS(startBFS);

            // Example: 0 1 are the indices of the nodes you wish to sever the link between
           //System.out.println("0 1");
        }
    }
    
    public static Node getNode(int id) {
       return level.stream().filter(n -> n.id == id).findFirst().get();
    }
    
    public static void findAndSeverOneLinkToExitBFS(List<Node> nodes) {
        System.err.println("Inspecting level : " + nodes);
        
        Iterator itr = nodes.iterator();
        while(itr.hasNext()) {
            if(hasLinkBeenSevered) return;
            Node n = (Node)itr.next();
            //if(!visitedNodes.contains(n)) {
                //visitedNodes.add(n);
                if(n.isExit) {
                    severLink(n); 
                    return;
                }     
            //}  
        }
        itr = nodes.iterator();
        while(itr.hasNext()) {
            if(hasLinkBeenSevered) return;
            Node n = (Node)itr.next();
            if(!visitedNodes.contains(n)) {
                visitedNodes.add(n);
                lastParentNode = n;
                findAndSeverOneLinkToExitBFS(n.links);  
            }     
        }
    }
    
    public static void severLink(Node n) {
        lastParentNode.removeLink(n);
        n.removeLink(lastParentNode);
        hasLinkBeenSevered = true;
        System.out.println(lastParentNode.id + " " + n.id);
    }
    
}

class Node {
    int id;
    boolean isExit;
    List<Node> links;
    
    Node(int id) {
        this.id = id;
        this.links = new ArrayList<>();
        this.isExit = false;
    }
    
    public void removeLink(Node n) {
        System.err.println(id + " | Removing link to : " + n.id);
        this.links.remove(n);
        System.err.println(id + " | Links : " + this.links);
        
    }
    
    @Override
    public String toString() {
        return this.id +"";   
    }
}
