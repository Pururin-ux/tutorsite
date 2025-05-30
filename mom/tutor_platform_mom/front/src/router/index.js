import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import StudentRegistration from '@/components/StudentRegistration.vue';
import TutorRegistration from '@/components/TutorRegistration.vue';
import LoginPage from '@/components/LoginPage.vue';
import UserDashboard from '@/components/UserDashboard.vue';
import ProfileUser from '@/components/ProfileUser.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/students', component: StudentRegistration },
  { path: '/tutors', component: TutorRegistration },
  { path: '/login', component: LoginPage },
  {
    path: '/dashboard',
    name: 'UserDashboard',
    component: UserDashboard,
  },
  {
    path: '/profile',
    name: 'ProfileUser',
    component: ProfileUser,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
