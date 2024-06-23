import { Injectable } from '@nestjs/common';
import { WebSocket } from 'ws';

@Injectable()
export class NetworkCommunicationService {
  private wss: WebSocket.Server;

  constructor() {
    this.wss = new WebSocket.Server({port: 8080 });
  }

  async sendMessage(nodeId: string, message: string): Promise<void> {
    // Send a message to a specific node
    this.wss.clients.forEach((client) => {
      if (client.nodeId === nodeId) {
        client.send(message);
      }
    });
  }

  async broadcastMessage(message: string): Promise<void> {
    // Broadcast a message to all nodes
    this.wss.clients.forEach((client) => {
      client.send(message);
    });
  }
  }
