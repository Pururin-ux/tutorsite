<!-- src/pages/HomePage.vue -->
<template>
  <div class="min-h-screen flex flex-col bg-gray-100">
    <!-- Header -->
    <header class="fixed inset-x-0 top-0 bg-white text-gray-800 shadow-md z-50">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center py-4">
        <!-- Logo -->
        <router-link to="/" class="flex items-center space-x-3">
          <img src="/mascot1.png" alt="Tutor Platform Logo" class="h-12 w-12 rounded-full shadow" />
          <h1 class="text-xl font-bold tracking-tight text-blue-800">Tutor Platform</h1>
        </router-link>

        <!-- Desktop nav -->
        <nav class="hidden lg:flex space-x-8 items-center">
          <router-link to="/students" class="nav-link">Для студентов</router-link>
          <router-link to="/tutors" class="nav-link">Для репетиторов</router-link>
          <router-link to="/features" class="nav-link">Возможности</router-link>
          <router-link to="/about" class="nav-link">О нас</router-link>
          <router-link to="/login" class="btn-primary-new">Войти</router-link>
        </nav>

        <!-- Burger -->
        <button
          class="lg:hidden bg-blue-50 text-blue-700 hover:bg-blue-100 font-medium py-2 px-4 rounded-lg transition duration-300"
          @click="toggleMenu"
        >
          <i class="fas fa-bars fa-lg" />
        </button>
      </div>
    </header>

    <!-- Mobile menu -->
    <div
      v-if="isMenuOpen"
      @click="toggleMenu"
      class="fixed inset-0 bg-black/25 flex justify-end z-40"
    >
      <nav
        @click.stop
        class="bg-white w-3/4 sm:w-1/2 h-full p-6 space-y-4 overflow-y-auto"
      >
        <div class="flex justify-end">
          <button
            @click="toggleMenu"
            class="text-gray-600 hover:text-blue-700 font-medium py-2 px-4 rounded-lg transition duration-300"
          >
            <i class="fas fa-times fa-lg" />
          </button>
        </div>

        <router-link to="/students" class="mobile-link">Для студентов</router-link>
        <router-link to="/tutors" class="mobile-link">Для репетиторов</router-link>
        <router-link to="/features" class="mobile-link">Возможности</router-link>
        <router-link to="/about" class="mobile-link">О нас</router-link>
        <router-link to="/login" class="btn-primary w-full text-center mt-4">Войти</router-link>
      </nav>
    </div>

    <!-- Hero -->
    <main
      class="flex-grow pt-24 flex items-center justify-center py-32 bg-cover bg-center relative"
      :style="{ backgroundImage: `url(${bg})` }"
    >
      <div class="absolute inset-0 bg-gradient-to-r from-blue-900 to-blue-700 opacity-70"></div>

      <div class="max-w-5xl mx-auto text-center space-y-10 relative z-10">
        <h2
          class="text-6xl font-extrabold text-white leading-tight animate__animated animate__fadeIn"
          style="text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.8)"
        >
          Найдите своего идеального репетитора
        </h2>
        <p
          class="text-xl text-gray-100"
          style="text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8)"
        >
          Персонализированное обучение для достижения ваших целей.
        </p>
        <div class="flex justify-center space-x-6">
          <router-link to="/students" class="btn-primary-hero">Найти репетитора</router-link>
          <router-link to="/tutors" class="btn-secondary-hero">Стать репетитором</router-link>
        </div>
      </div>
    </main>

    <!-- Features -->
    <section class="bg-white py-24">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <h3 class="text-4xl font-bold text-center mb-12 text-blue-800">
          Почему выбирают Tutor Platform
        </h3>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
          <div class="feature-item">
            <div class="flex items-center space-x-4 mb-4">
              <i class="fas fa-users fa-2x text-blue-700"></i>
              <h4>Большой выбор репетиторов</h4>
            </div>
            <p>Найдите идеального преподавателя под ваши нужды.</p>
          </div>

          <div class="feature-item">
            <div class="flex items-center space-x-4 mb-4">
              <i class="fas fa-calendar-alt fa-2x text-blue-700"></i>
              <h4>Удобное расписание</h4>
            </div>
            <p>Планируйте занятия в удобное для вас время.</p>
          </div>

          <div class="feature-item">
            <div class="flex items-center space-x-4 mb-4">
              <i class="fas fa-comments fa-2x text-blue-700"></i>
              <h4>Простая коммуникация</h4>
            </div>
            <p>Легко связывайтесь с репетиторами через нашу платформу.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-blue-800 text-white py-12">
      <div class="container mx-auto text-center">
        <p class="mb-6 text-gray-200">&copy; 2024 Tutor Platform. Все права защищены.</p>
        <div class="flex justify-center space-x-6">
          <a href="#" class="social-icon"><i class="fab fa-facebook-f fa-lg"></i></a>
          <a href="#" class="social-icon"><i class="fab fa-twitter fa-lg"></i></a>
          <a href="#" class="social-icon"><i class="fab fa-instagram fa-lg"></i></a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import bg from '@/assets/background.jpg'

const isMenuOpen = ref(false)
const toggleMenu = () => (isMenuOpen.value = !isMenuOpen.value)

// Лочим / возвращаем скролл при открытии мобильного меню
watch(isMenuOpen, (val) => {
  document.body.classList.toggle('overflow-hidden', val)
})
</script>

<style scoped>
/* ---------- Классы навигации и кнопок ---------- */
.nav-link {
  @apply text-gray-600 hover:text-blue-900 transition duration-300 font-medium;
}

.btn-primary-new {
  @apply bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-md transition duration-300 shadow-md;
}

.btn-primary-hero {
  @apply bg-yellow-500 hover:bg-yellow-600 text-blue-900 font-bold py-4 px-8 rounded-lg transition duration-300 shadow-lg;
}

.btn-secondary-hero {
  @apply bg-transparent hover:bg-blue-50 text-white font-bold py-4 px-8 rounded-lg transition duration-300 border border-white;
}

.mobile-link {
  @apply block text-gray-600 hover:text-blue-700 transition duration-300 py-2;
}

/* ---------- Блок преимуществ ---------- */
.feature-item {
  @apply p-8 bg-blue-50 rounded-xl shadow-md hover:shadow-lg transition duration-300;
}

.feature-item h4 {
  @apply text-xl font-semibold text-blue-800;
}

.feature-item p {
  @apply text-gray-700 mt-2;
}

/* ---------- Соцсети в футере ---------- */
.social-icon {
  @apply text-gray-300 hover:text-white transition duration-300;
}

/* Затемнение картинки в Hero добавлено через `bg-gradient` в разметке */
</style>