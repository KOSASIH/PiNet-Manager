// consensus.go
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

type Consensus struct {
	nodes    []string
	proposal []byte
	deadline time.Time
}

func (c *Consensus) propose(proposal []byte) {
	c.proposal = proposal
	c.deadline = time.Now().Add(10 * time.Second)
}

func (c *Consensus) vote(node string, vote bool) {
	if vote {
		c.nodes = append(c.nodes, node)
	}
}

func (c *Consensus) decide() bool {
	if len(c.nodes) > len(c.nodes)/2 {
		return true
	}
	return false
}

func main() {
	nodes := []string{"node1", "node2", "node3"}
	consensus := &Consensus{nodes: nodes}
	proposal := []byte("Hello, World!")

	consensus.propose(proposal)

	wg := &sync.WaitGroup{}
	for _, node := range nodes {
		wg.Add(1)
		go func(node string) {
			defer wg.Done()
			time.Sleep(time.Duration(rand.Intn(5)) * time.Second)
			consensus.vote(node, true)
		}(node)
	}

	wg.Wait()
	if consensus.decide() {
		fmt.Println("Consensus reached!")
	} else {
		fmt.Println("Consensus not reached.")
	}
}
