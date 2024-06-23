// NodeManagement.js
import React, { useState, useEffect } from 'eact';
import axios from 'axios';

function NodeManagement() {
  const [nodes, setNodes] = useState([]);
  const [newNode, setNewNode] = useState({ name: '', ip_address: '', status: '' });

  useEffect(() => {
    axios.get('/nodes')
     .then(response => {
setNodes(response.data);
     })
     .catch(error => {
       console.error('Error fetching nodes:', error);
     });
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('/nodes', newNode)
     .then(response => {
       setNodes([...nodes, response.data]);
       setNewNode({ name: '', ip_address: '', status: '' });
     })
     .catch(error => {
       console.error('Error creating node:', error);
     });
  };

  return (
    <div>
      <h1>Node Management</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" value={newNode.name} onChange={(event) => setNewNode({ ...newNode, name: event.target.value })} />
        </label>
        <label>
          IP Address:
          <input type="text" value={newNode.ip_address} onChange={(event) => setNewNode({ ...newNode, ip_address: event.target.value })} />
        </label>
        <label>
          Status:
          <input type="text" value={newNode.status} onChange={(event) => setNewNode({ ...newNode, status: event.target.value })} />
        </label>
        <button type="submit">Create Node</button>
      </form>
      <ul>
        {nodes.map(node => (
          <li key={node.id}>
            {node.name} ({node.ip_address}) - {node.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default NodeManagement;
