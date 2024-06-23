// ConsensusAlgorithm.java
import java.util.ArrayList;
import java.util.List;

public class ConsensusAlgorithm {
    private List<Node> nodes;
    private Blockchain blockchain;

    public ConsensusAlgorithm(List<Node> nodes, Blockchain blockchain) {
        this.nodes = nodes;
        this.blockchain = blockchain;
    }

    public void runConsensus() {
        // Implement your consensus algorithm logic here
        // For demonstration purposes, a simple majority vote is used
        int majority = nodes.size() / 2 + 1;
        int votes = 0;
        for (Node node : nodes) {
            if (node.vote()) {
                votes++;
            }
            if (votes >= majority) {
                blockchain.addBlock(new Block("Consensus reached!"));
                break;
            }
        }
    }
}

class Node {
    private boolean vote;

    public boolean vote() {
        // Implement your node's voting logic here
        return true; // For demonstration purposes, always vote yes
    }
}

class Blockchain {
    private List<Block> blocks;

    public Blockchain() {
        this.blocks = new ArrayList<>();
    }

    public void addBlock(Block block) {
        blocks.add(block);
    }
}

class Block {
    private String data;

    public Block(String data) {
        this.data = data;
    }
}
