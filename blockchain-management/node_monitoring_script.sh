# node_monitoring_script.sh
#!/bin/bash

# Set node IP addresses and names
declare -a nodes=("node1" "192.168.1.100" "node2" "192.168.1.101" "node3" "192.168.1.102")

# Function to check node status
check_node_status() {
    local node_name=$1
    local node_ip=$2
    if ping -c 1 $node_ip &> /dev/null; then
        echo "$node_name is online"
    else
        echo "$node_name is offline"
    fi
}

# Monitor nodes
while true; do
    for ((i=0; i<${#nodes[@]}; i+=2)); do
        check_node_status ${nodes[$i]} ${nodes[$i+1]}
    done
    sleep 10
done
