<template>
  <div class="w-full max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md">
    <h2 class="text-3xl font-semibold text-center mb-6">Вход</h2>

    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label for="email" class="block text-gray-700">Электронная почта</label>
        <input type="email" id="email" v-model="form.email" class="w-full px-4 py-2 border rounded-md" required />
      </div>

      <div>
        <label for="password" class="block text-gray-700">Пароль</label>
        <input type="password" id="password" v-model="form.password" class="w-full px-4 py-2 border rounded-md" required />
      </div>

      <div>
        <button type="submit" class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition duration-300">
          Войти
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email: '',
        password: ''
      }
    };
  },
  methods: {
    submitForm() {
      console.log('Вход с данными:', this.form);
      // Здесь можно добавить логику для отправки данных на сервер и получения токена или сессии.
    }
  }
};
</script>
