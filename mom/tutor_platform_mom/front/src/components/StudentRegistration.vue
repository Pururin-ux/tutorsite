<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-300 via-purple-400 to-pink-400 py-12 px-4 sm:px-6 lg:px-8">
    <div class="w-full max-w-5xl mx-auto p-8 bg-white bg-opacity-80 rounded-3xl shadow-2xl">
      <div class="flex flex-wrap justify-center -mx-4">
        <!-- Registration Form -->
        <div class="w-full sm:w-1/2 px-4 mb-8 sm:mb-0">
          <div class="p-8 bg-white rounded-2xl shadow-lg transition-transform duration-300 transform hover:scale-105">
            <h2 class="text-4xl font-bold text-center text-gray-800 mb-8 font-heading">Регистрация для студентов</h2>
            <form @submit.prevent="submitForm" class="space-y-6">
              <div class="space-y-2">
                <label for="name" class="block text-gray-700 font-semibold font-body">Имя</label>
                <input type="text" id="name" v-model="form.name" placeholder="Введите ваше имя" class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-300 font-body" required />
              </div>

              <div class="space-y-2">
                <label for="email" class="block text-gray-700 font-semibold font-body">Электронная почта</label>
                <input type="email" id="email" v-model="form.email" placeholder="example@mail.com" class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-300 font-body" required />
              </div>

              <div class="space-y-2">
                <label for="password" class="block text-gray-700 font-semibold font-body">Пароль</label>
                <input type="password" id="password" v-model="form.password" placeholder="Ваш надежный пароль" class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-300 font-body" required />
              </div>

              <div>
                <button type="submit" class="w-full bg-gradient-to-r from-blue-500 to-purple-500 text-white font-bold py-3 rounded-lg hover:bg-gradient-to-r hover:from-purple-500 hover:to-blue-500 transition-all duration-300 transform hover:scale-105 font-body">
                  Зарегистрироваться
                </button>
              </div>
            </form>
          </div>
        </div>

        <!-- Registration Image -->
        <div class="w-full sm:w-1/2 px-4">
          <div class="rounded-2xl overflow-hidden shadow-lg">
            <img src="mascot1.png" alt="Registration Image" class="w-full h-full object-cover transition-transform duration-500 transform hover:scale-105" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        email: '',
        password: ''
      }
    };
  },
  methods: {
    submitForm() {
      console.log('Регистрация студента:', this.form);
      // Здесь можно добавить логику для отправки данных на сервер.
    }
  }
};
</script>

<style scoped>
/* Шрифты */
.font-heading {
  font-family: 'Montserrat', sans-serif; /* Пример более выразительного шрифта для заголовков */
}

.font-body {
  font-family: 'Open Sans', sans-serif; /* Пример более читабельного шрифта для основного текста */
}

/* Поля ввода */
input {
  height: 48px;
}

input::placeholder {
  color: #a0aec0; /* Цвет плейсхолдера */
  opacity: 1;
  font-size: 0.9rem;
}
/* Адаптивность */
@media (max-width: 640px) {
  .w-full {
    width: 100%;
  }
  .sm\:w-1\/2 {
    width: 100%;
  }
  .mb-8 {
    margin-bottom: 2rem;
  }
}
</style>