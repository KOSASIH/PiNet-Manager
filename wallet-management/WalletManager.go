package main

import (
	"fmt"
	"crypto/ecdsa"
	"crypto/rand"
	"crypto/sha256"
	"golang.org/x/crypto/ripemd160"
)

type WalletManager struct {
	wallets map[string]*ecdsa.PrivateKey
}

func NewWalletManager() *WalletManager {
	return &WalletManager{
		wallets: make(map[string]*ecdsa.PrivateKey),
	}
}

func (wm *WalletManager) CreateWallet() (*ecdsa.PrivateKey, error) {
	privateKey, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	if err!= nil {
		return nil, err
	}
	wm.wallets[privateKey.PublicKey.Hash().String()] = privateKey
	return privateKey, nil
}

func (wm *WalletManager) GetWallet(address string) (*ecdsa.PrivateKey, error) {
	return wm.wallets[address], nil
}

func main() {
	wm := NewWalletManager()
	privateKey, err := wm.CreateWallet()
	if err!= nil {
		fmt.Println(err)
		return
	}
	fmt.Println(privateKey.PublicKey.Hash().String())
}
