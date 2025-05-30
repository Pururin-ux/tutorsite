<template>
  <div>
    <h2>Register as a Tutor or Student</h2>
    <form @submit.prevent="submitForm">
      <input v-model="name" type="text" placeholder="Name" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      email: ''
    }
  },
  methods: {
    submitForm() {
      // Make API call to Django to register user
      console.log(this.name, this.email)
    }
  }
}
</script>
