<template>
  <div>
    <h2>Wallet</h2>
    <form @submit.prevent="createWallet">
      <label>Wallet Name:</label>
      <input type="text" v-model="walletName" />
      <br />
      <button type="submit">Create Wallet</button>
    </form>
    <ul>
      <li v-for="wallet in wallets" :key="wallet.address">
        {{ wallet.address }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      walletName: "",
      wallets: []
    };
  },
  methods: {
    createWallet() {
      // Call API to create wallet
      console.log("Wallet created successfully!");
    }
  }
};
</script>
