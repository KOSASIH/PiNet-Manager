// blockchain.rs
use std::collections::HashMap;
use std::sync::{Arc, Mutex};

struct Blockchain {
    chain: Vec<Block>,
    pending_transactions: Vec<Transaction>,
    node_map: HashMap<String, Node>,
}

struct Block {
    transactions: Vec<Transaction>,
    previous_hash: String,
    timestamp: u64,
}

struct Transaction {
    sender: String,
    recipient: String,
    amount: u64,
}

struct Node {
    address: String,
    public_key: String,
}

impl Blockchain {
    fn new() -> Self {
        Blockchain {
            chain: vec![],
            pending_transactions: vec![],
            node_map: HashMap::new(),
        }
    }

    fn add_node(&mut self, node: Node) {
        self.node_map.insert(node.address.clone(), node);
    }

    fn add_transaction(&mut self, transaction: Transaction) {
        self.pending_transactions.push(transaction);
    }

    fn mine_block(&mut self) {
        let block = Block {
            transactions: self.pending_transactions.clone(),
            previous_hash: self.chain.last().unwrap().hash(),
            timestamp: std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap().as_secs(),
       };
        self.chain.push(block);
        self.pending_transactions.clear();
    }
}
