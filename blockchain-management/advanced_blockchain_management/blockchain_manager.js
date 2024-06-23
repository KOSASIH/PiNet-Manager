// blockchain_manager.js
const { Blockchain } = require('./blockchain');

class BlockchainManager {
    constructor(blockchain) {
        this.blockchain = blockchain;
    }

    async getBlockchainInfo() {
        return this.blockchain.getInfo();
    }

    async addBlock(block) {
        return this.blockchain.addBlock(block);
    }

    async getBlockByHash(hash) {
        return this.blockchain.getBlockByHash(hash);
    }

    async getBlockByNumber(number) {
        return this.blockchain.getBlockByNumber(number);
    }
}

class Blockchain {
    constructor() {
        this.blocks = [];
    }

    getInfo() {
        return { height: this.blocks.length, hash: this.blocks[this.blocks.length - 1].hash };
    }

    addBlock(block) {
        this.blocks.push(block);
        return block;
    }

    getBlockByHash(hash) {
        return this.blocks.find((block) => block.hash === hash);
    }

    getBlockByNumber(number) {
        return this.blocks[number];
    }
}

class Block {
    constructor(data) {
        this.data = data;
        this.hash = crypto.createHash('sha256').update(data).digest('hex');
    }
}

module.exports = { BlockchainManager, Blockchain,Block };
