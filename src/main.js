// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/main.css'; // Путь к файлу в public

// --- Импорт Vue Tippy ---
import VueTippy from 'vue-tippy';
import 'tippy.js/dist/tippy.css'; // Базовые стили Tippy
import 'tippy.js/themes/light.css'; // Пример темы: 'light'
// --- Конец импорта Vue Tippy ---

// Создаем экземпляр приложения
const app = createApp(App);

// Регистрируем Vue Router
app.use(router);

// --- Регистрируем Vue Tippy (ДО монтирования приложения!) ---
app.use(VueTippy, {
  directive: 'tippy', // Имя директивы (например, v-tippy)
  component: 'tippy', // Имя компонента (например, <tippy>)
  defaultProps: {
    placement: 'top', // Позиция по умолчанию
    animation: 'fade', // Анимация по умолчанию
    theme: 'light', // Тема по умолчанию
    arrow: true, // Добавил стрелку тултипа, если она нужна
    delay: [100, 0], // Небольшая задержка перед появлением
  },
});
// --- Конец регистрации Vue Tippy ---

// Монтируем приложение
app.mount('#app');