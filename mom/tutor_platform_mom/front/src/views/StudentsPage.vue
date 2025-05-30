<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
    <header class="w-full py-4 bg-blue-600 text-white text-center">
      <h1 class="text-4xl font-bold">Страница студентов</h1>
      <p class="mt-2 text-lg">Выберите подходящего преподавателя и начинайте обучение.</p>
    </header>

    <div class="w-full flex justify-center mt-10">
      <button class="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700">Поиск преподавателей</button>
    </div>

    <footer class="w-full bg-gray-800 text-white text-center py-4 mt-10">
      <p>&copy; 2024 Tutor Platform. Все права защищены.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'StudentsPage',
};
</script>
