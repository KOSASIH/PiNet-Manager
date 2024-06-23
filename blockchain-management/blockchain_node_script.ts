// blockchain_node_script.ts
import * as Web3 from 'web3';

const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'));

async function createBlock(data: string) {
  const block = {
    parentHash: web3.utils.sha3(''),
    uncleHash: web3.utils.sha3(''),
    coinbase: '0x0000000000000000000000000000000000000000',
    root: web3.utils.sha3(''),
    txTrie: web3.utils.sha3(''),
    receiptTrie: web3.utils.sha3(''),
    bloom: '0x0000000000000000000000000000000000000000000000000000000000000000',
    difficulty: '0x0000000000000000000000000000000000000000000000000000000000000001',
    number: '0x0000000000000000000000000000000000000000000000000000000000000001',
    gasLimit: '0x0000000000000000000000000000000000000000000000000000000000000001',
    gasUsed: '0x0000000000000000000000000000000000000000000000000000000000000001',
    timestamp: Date.now(),
    extraData: '0x0000000000000000000000000000000000000000000000000000000000000000',
    mixHash: web3.utils.sha3(''),
    nonce: '0x0000000000000000000000000000000000000000000000000000000000000001',
    data,
  };
  const blockHash = web3.utils.sha3(JSON.stringify(block));
  console.log(`Block created with hash ${blockHash}`);
}

async function startNode() {
  console.log('Blockchain node started');
  createBlock('Hello, world!');
}

startNode();
