import { Node } from './node.entity';
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';

@Injectable()
export class NodeManagerService {
  constructor(
    @InjectRepository(Node)
    private readonly nodeRepository: Repository<Node>,
  ) {}

  async getNodeList(): Promise<Node[]> {
    return this.nodeRepository.find();
  }

  async getNode(nodeId: string): Promise<Node> {
    return this.nodeRepository.findOne(nodeId);
  }

  async createNode(node: Node): Promise<Node> {
    return this.nodeRepository.save(node);
  }

  async updateNode(nodeId: string, node: Node): Promise<Node> {
    return this.nodeRepository.update(nodeId, node);
  }

  async deleteNode(nodeId: string): Promise<void> {
    return this.nodeRepository.delete(nodeId);
  }

  async getNodeStatus(nodeId: string): Promise<string> {
    // Implement node status logic here
    // For example, using a NodeJS-based health check
    const healthCheck = await fetch(`http://${nodeId}:8080/health`);
    return healthCheck.ok ? 'online' : 'offline';
  }
}
