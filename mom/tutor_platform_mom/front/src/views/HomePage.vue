<template>
  <div class="min-h-screen flex flex-col bg-gray-50">
    <!-- Хедер -->
    <header class="fixed top-0 left-0 right-0 bg-white text-gray-800 shadow-md z-50">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center py-4">
        <router-link to="/" class="flex items-center space-x-3">
          <img src="/owl-logo.png" alt="Логотип" class="h-12 w-12 rounded-full shadow-lg border-2 border-yellow-400">
          <h1 class="text-xl font-bold tracking-tight text-orange-600 font-comic">Умный Малыш</h1>
        </router-link>
        <nav class="hidden lg:flex space-x-8 items-center">
          <router-link to="/programs" class="nav-link">Программы</router-link>
          <router-link to="/teachers" class="nav-link">Педагоги</router-link>
          <router-link to="/pricing" class="nav-link">Стоимость</router-link>
          <router-link to="/contacts" class="nav-link">Контакты</router-link>
          <a href="tel:+375291234567" class="btn-primary-new">
            <i class="fas fa-phone mr-2"></i>+375 (29) 123-45-67
          </a>
        </nav>
        <button class="lg:hidden bg-orange-100 text-orange-700 hover:bg-orange-200 font-medium py-2 px-4 rounded-lg transition duration-300" @click="toggleMenu">
          <i class="fas fa-bars fa-lg"></i>
        </button>
      </div>
    </header>

    <!-- Мобильное меню -->
    <div v-if="isMenuOpen" @click="toggleMenu" class="fixed inset-0 bg-black bg-opacity-25 flex justify-end">
      <nav @click.stop="" class="bg-white w-3/4 sm:w-1/2 p-6 space-y-4">
        <div class="flex justify-end">
          <button @click="toggleMenu" class="text-gray-600 hover:text-orange-700 font-medium py-2 px-4 rounded-lg transition duration-300">
            <i class="fas fa-times fa-lg"></i>
          </button>
        </div>
        <router-link to="/programs" class="block text-gray-600 hover:text-orange-700 transition duration-300 py-2">Программы</router-link>
        <router-link to="/teachers" class="block text-gray-600 hover:text-orange-700 transition duration-300 py-2">Педагоги</router-link>
        <router-link to="/pricing" class="block text-gray-600 hover:text-orange-700 transition duration-300 py-2">Стоимость</router-link>
        <router-link to="/contacts" class="block text-gray-600 hover:text-orange-700 transition duration-300 py-2">Контакты</router-link>
        <a href="tel:+375291234567" class="btn-primary w-full text-center mt-4">
          <i class="fas fa-phone mr-2"></i>Позвонить
        </a>
      </nav>
    </div>

    <!-- Основной контент -->
    <main class="flex-grow flex items-center justify-center py-32 bg-cover bg-center relative" style="background-image: url('/kids-bg.jpg')">
      <div class="absolute inset-0 bg-gradient-to-r from-orange-600 to-orange-400 opacity-85"></div>
      <div class="max-w-5xl mx-auto text-center space-y-10 relative z-10 px-4">
        <h2 class="text-5xl font-bold text-white leading-tight animate__animated animate__fadeInDown font-comic">
          Подготовка к школе и развитие детей 4-7 лет
        </h2>
        <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-6">
          <router-link to="/trial-lesson" class="btn-primary-hero">
            <i class="fas fa-gift mr-2"></i>Бесплатный пробный урок
          </router-link>
          <router-link to="/schedule" class="btn-secondary-hero">
            <i class="fas fa-calendar-alt mr-2"></i>Расписание занятий
          </router-link>
        </div>
      </div>
    </main>

    <!-- Преимущества -->
    <section class="bg-white py-24">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <h3 class="text-4xl font-bold text-center mb-12 text-orange-600 font-comic">Наши преимущества</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="feature-item p-6 bg-orange-50 rounded-xl shadow-md hover:shadow-lg transition duration-300">
            <div class="flex flex-col items-center text-center">
              <img src="/icons/group-icon.svg" class="h-20 w-20 mb-4" alt="Группы">
              <h4 class="text-xl font-semibold text-orange-800 mb-2">Маленькие группы</h4>
              <p class="text-gray-700">Занятия в группах до 6 человек для индивидуального подхода</p>
            </div>
          </div>
          <div class="feature-item p-6 bg-orange-50 rounded-xl shadow-md hover:shadow-lg transition duration-300">
            <div class="flex flex-col items-center text-center">
              <img src="/icons/book-icon.svg" class="h-20 w-20 mb-4" alt="Методики">
              <h4 class="text-xl font-semibold text-orange-800 mb-2">Авторские методики</h4>
              <p class="text-gray-700">Обучение через игру с использованием современных пособий</p>
            </div>
          </div>
          <div class="feature-item p-6 bg-orange-50 rounded-xl shadow-md hover:shadow-lg transition duration-300">
            <div class="flex flex-col items-center text-center">
              <img src="/icons/teacher-icon.svg" class="h-20 w-20 mb-4" alt="Педагоги">
              <h4 class="text-xl font-semibold text-orange-800 mb-2">Опытные педагоги</h4>
              <p class="text-gray-700">Преподаватели с 10+ летним опытом работы с детьми</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Футер -->
    <footer class="bg-orange-800 text-white py-12">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h5 class="text-lg font-bold mb-4 font-comic">Умный Малыш</h5>
            <p class="text-sm text-orange-100">Лицензия №12345 от 20.03.2025</p>
          </div>
          <div>
            <h5 class="text-lg font-bold mb-4">Контакты</h5>
            <p class="text-sm mb-2"><i class="fas fa-map-marker-alt mr-2"></i>г. Смолевичи, ул. Детская, 15</p>
            <p class="text-sm"><i class="fas fa-clock mr-2"></i>Пн-Пт: 9:00-19:00</p>
          </div>
          <div>
            <h5 class="text-lg font-bold mb-4">Соцсети</h5>
            <div class="flex space-x-4">
              <a href="#" class="social-icon"><i class="fab fa-vk fa-lg"></i></a>
              <a href="#" class="social-icon"><i class="fab fa-odnoklassniki fa-lg"></i></a>
              <a href="#" class="social-icon"><i class="fab fa-telegram-plane fa-lg"></i></a>
            </div>
          </div>
          <div>
            <h5 class="text-lg font-bold mb-4">Безопасность</h5>
            <p class="text-sm text-orange-100">Видеонаблюдение и охраняемая территория</p>
          </div>
        </div>
        <div class="border-t border-orange-700 mt-8 pt-6 text-center">
          <p class="text-sm text-orange-200">&copy; 2025 Умный Малыш. Все права защищены.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isMenuOpen: false
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@700&display=swap');

.font-comic {
  font-family: 'Comic Neue', cursive;
}

.nav-link {
  @apply text-gray-700 hover:text-orange-600 transition duration-300 font-medium;
}

.btn-primary-new {
  @apply bg-orange-600 hover:bg-orange-700 text-white font-medium py-3 px-6 rounded-lg transition duration-300 shadow-md;
}

.btn-primary-hero {
  @apply bg-white hover:bg-orange-50 text-orange-600 font-bold py-4 px-8 rounded-full transition duration-300 shadow-lg text-lg;
}

.btn-secondary-hero {
  @apply bg-transparent hover:bg-orange-600 text-white font-bold py-4 px-8 rounded-full transition duration-300 border-2 border-white hover:border-orange-600 text-lg;
}

.feature-item {
  @apply transform hover:-translate-y-2 transition-all duration-300;
}

.social-icon {
  @apply text-orange-200 hover:text-white transition duration-300;
}

/* Анимация для заголовка */
.animate__fadeInDown {
  animation: fadeInDown 1s ease-out;
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
