<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
    <header class="w-full py-4 bg-green-600 text-white text-center">
      <h1 class="text-4xl font-bold">Страница преподавателей</h1>
      <p class="mt-2 text-lg">Предложите свои услуги студентам и развивайтесь как преподаватель.</p>
    </header>

    <div class="w-full flex justify-center mt-10">
      <button class="bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700">Предложить услуги</button>
    </div>

    <footer class="w-full bg-gray-800 text-white text-center py-4 mt-10">
      <p>&copy; 2024 Tutor Platform. Все права защищены.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'TutorsPage',
};
</script>
