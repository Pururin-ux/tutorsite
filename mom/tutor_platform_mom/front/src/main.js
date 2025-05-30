import { createApp } from 'vue';
import App from './App.vue';
import './assets/main.css';  // Путь к файлу в public
import router from './router';

createApp(App).use(router).mount('#app');