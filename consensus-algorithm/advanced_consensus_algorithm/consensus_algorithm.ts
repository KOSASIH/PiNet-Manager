import { Injectable } from '@nestjs/common';
import { Blockchain } from './blockchain.entity';
import { Node } from './node.entity';

@Injectable()
export class ConsensusAlgorithmService {
  async runConsensusAlgorithm(blockchain: Blockchain, nodes: Node[]): Promise<Blockchain> {
    // Implement your consensus algorithm logic here
    // For example, a simple proof-of-stake (PoS) algorithm:
    const stakeThreshold = 0.5;
    const nodeStakes = nodes.map((node) => node.nodeStake);
    const totalStake = nodeStakes.reduce((acc, curr) => acc + curr, 0);
    const winningNode = nodes.find((node) => node.nodeStake / totalStake >= stakeThreshold);

    if (winningNode) {
      blockchain.currentBlock = winningNode.nodeId;
      blockchain.blockchainStatus = 'updated';
    } else {
      blockchain.blockchainStatus = 'failed';
    }

    return blockchain;
  }
}
