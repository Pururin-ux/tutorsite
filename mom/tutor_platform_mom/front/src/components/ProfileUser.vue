<template>
  <div class="min-h-screen flex flex-col bg-gray-100">
    <!-- Header -->
    <header class="bg-white shadow-md p-4 flex justify-between items-center">
      <router-link to="/" class="flex items-center space-x-2">
        <img src="/mascot1.png" alt="Tutor Platform Logo" class="h-8 w-8 rounded-full">
        <h1 class="text-xl font-bold text-blue-700">Tutor Platform</h1>
      </router-link>
      <router-link
        to="/"
        class="btn-secondary"
      >
        Выйти
      </router-link>
    </header>

    <!-- Profile Content -->
    <main class="flex-grow container mx-auto py-12">
      <div class="bg-white shadow-lg rounded-lg overflow-hidden">
        <div class="px-6 py-4 border-b border-gray-200">
          <h2 class="text-2xl font-semibold text-gray-800">Мой профиль</h2>
        </div>
        <div class="p-6 space-y-6">
          <!-- User Info -->
          <section class="space-y-4">
            <h3 class="text-xl font-semibold text-gray-700">Информация о пользователе</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <p><strong class="font-medium text-gray-700">Имя:</strong> Иван Иванов</p>
              </div>
              <div>
                <p><strong class="font-medium text-gray-700">Email:</strong> example@mail.com</p>
              </div>
              <div>
                <p><strong class="font-medium text-gray-700">Роль:</strong> Репетитор</p>
              </div>
            </div>
          </section>

          <!-- Actions -->
          <section class="space-y-4">
            <h3 class="text-xl font-semibold text-gray-700">Действия</h3>
            <div class="flex flex-wrap gap-4">
              <button class="btn-primary">
                Редактировать профиль
              </button>
              <button class="btn-secondary">
                Посмотреть отзывы
              </button>
            </div>
          </section>
        </div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white text-center py-6">
      <p>&copy; 2024 Tutor Platform. Все права защищены.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "ProfileUser",
};
</script>

<style scoped>
/* Стили для кнопки btn-primary */
.btn-primary {
  background-color: #4c6ef5; /* Пример цвета */
  color: white;
  padding: 10px 20px;
  border-radius: 4px;
  text-transform: uppercase;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #3a56d9; /* Пример цвета при наведении */
}

/* Дополнительные стили для этой страницы, если необходимо */
</style>