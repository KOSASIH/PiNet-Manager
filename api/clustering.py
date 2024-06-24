# clustering.py
import etcd

# Create etcd client
client = etcd.Client(host='example.com', port=2379)

# Create cluster
client.cluster_create('my_cluster')

# Add nodes to cluster
client.cluster_add_node('node1', 'http://node1:2380')
client.cluster_add_node('node2', 'http://node2:2380')

# Elect leader
leader = client.cluster_elect_leader()
print(f'Leader elected: {leader}')
