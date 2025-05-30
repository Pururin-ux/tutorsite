<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './views/HomePage.vue';
import StudentsPage from './views/StudentsPage.vue';
import TutorsPage from './views/TutorsPage.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/students', component: StudentsPage },
  { path: '/tutors', component: TutorsPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default {
  name: 'App',
  router,
};
</script>
