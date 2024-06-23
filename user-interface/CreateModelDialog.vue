<template>
  <div>
    <h2>Create Model Dialog</h2>
    <form @submit.prevent="createModel">
      <label>IP Address:</label>
      <input type="text" v-model="ipAddress" />
      <br />
      <label>Host Name:</label>
      <input type="text" v-model="hostName" />
      <br />
      <button type="submit">Create Model</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      ipAddress: "",
      hostName: ""
    };
  },
  methods: {
    createModel() {
      // Call API to create model
      console.log("Model created successfully!");
    }
  }
};
</script>
