// network_communication.js
const WebSocket = require('ws');

class NetworkCommunication {
    constructor(nodes) {
        this.nodes = nodes;
        this.ws = new WebSocket.Server({ port: 8080 });
    }

    async sendMessage(nodeId, message) {
        const node = this.nodes.find((node) => node.id === nodeId);
        if (node) {
            node.ws.send(message);
        }
    }

    async start() {
        this.ws.on('connection', (ws) => {
            console.log('Node connected');

            ws.on('message', (message) => {
                console.log(`Received message: ${message}`);
                // Handle incoming message
            });

            ws.on('close', () => {
                console.log('Node disconnected');
            });
        });
    }
}

module.exports = NetworkCommunication;
