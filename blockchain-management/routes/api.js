const express = require('express');
const router = express.Router();
const Blockchain = require('../models/Blockchain');
const Wallet = require('../models/Wallet');

router.get('/blockchain/balance', async (req, res) => {
  try {
    const blockchain = new Blockchain();
    const balance = await blockchain.getBalance('0xYourAddress');
    res.json({ balance });
  } catch (error) {
    res.status(500).json({ error: 'Error getting balance' });
  }
});

router.post('/blockchain/transfer', async (req, res) => {
  try {
    const { recipient, amount } = req.body;
    const blockchain = new Blockchain();
    await blockchain.transfer('0xRecipientAddress', amount);
    res.json({ success: 'Transfer successful' });
  } catch (error) {
    res.status(500).json({ error: 'Error transferring funds' });
  }
});

router.get('/wallet/balance', async (req, res) => {
  try {
    const wallet = new Wallet();
    const balance = await wallet.getBalance();
    res.json({ balance });
  } catch (error) {
    res.status(500).json({ error: 'Error getting balance' });
  }
});

router.post('/wallet/deposit', async (req, res) => {
  try {
    const { amount } = req.body;
    const wallet = new Wallet();
    await wallet.deposit(amount);
    res.json({ success: 'Deposit successful' });
  } catch (error) {
    res.status(500).json({ error: 'Error depositing funds' });
  }
});

router.post('/wallet/withdraw', async (req, res) => {
  try {
    const { amount } = req.body;
    const wallet = new Wallet();
    await wallet.withdraw(amount);
    res.json({ success: 'Withdraw successful' });
  } catch (error) {
    res.status(500).json({ error: 'Error withdrawing funds' });
  }
});

module.exports = router;
