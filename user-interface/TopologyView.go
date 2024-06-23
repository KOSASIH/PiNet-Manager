package main

import (
	"fmt"

	"github.com/pi-net-manager/topology-view"
)

func main() {
	tv := topologyview.NewTopologyView()
	tv.AddDevice("Device 1", "192.168.1.1")
	tv.AddDevice("Device 2", "192.168.1.2")
	tv.AddNetworkGroup("Network Group 1", "192.168.1.0/24")
	tv.AddNetworkGroup("Network Group 2", "192.168.2.0/24")

	fmt.Println(tv.Render())
}
