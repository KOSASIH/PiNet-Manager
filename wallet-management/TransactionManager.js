class TransactionManager {
  constructor() {
    this.transactions = [];
  }

  addTransaction(transaction) {
    this.transactions.push(transaction);
  }

  getTransactions() {
    return this.transactions;
  }

  getTransaction(hash) {
    return this.transactions.find((transaction) => transaction.hash === hash);
  }
}

export default TransactionManager;
