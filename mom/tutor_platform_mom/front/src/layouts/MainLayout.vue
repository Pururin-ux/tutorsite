<template>
  <div>
    <Header />
    <main class="p-4">
      <slot />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';

export default {
  components: { Header, Footer },
};
</script>

<style scoped>
/* Добавь стили, если нужно */
</style>
