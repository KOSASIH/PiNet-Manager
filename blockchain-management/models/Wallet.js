const Web3 = require('web3');

class Wallet {
  constructor() {
    this.web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'));
  }

  async getBalance() {
    const balance = await this.web3.eth.getBalance('0xYourAddress');
    return balance;
  }

  async deposit(amount) {
    const txCount = await this.web3.eth.getTransactionCount();
    const tx = {
      from: '0xYourAddress',
      to: '0xYourAddress',
      value: amount,
      gas: '20000',
      gasPrice: '20',
      nonce: txCount
    };
    const signedTx = await this.web3.eth.accounts.signTransaction(tx, '0xYourPrivateKey');
    await this.web3.eth.sendSignedTransaction(signedTx.rawTransaction);
  }

  async withdraw(amount) {
    const txCount = await this.web3.eth.getTransactionCount();
    const tx = {
      from: '0xYourAddress',
      to: '0xRecipientAddress',
      value: amount,
      gas: '20000',
      gasPrice: '20',
      nonce: txCount
    };
    const signedTx = await this.web3.eth.accounts.signTransaction(tx, '0xYourPrivateKey');
    await this.web3.eth.sendSignedTransaction(signedTx.rawTransaction);
  }
}

module.exports = Wallet;
