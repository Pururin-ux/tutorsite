<template>
  <div class="min-h-screen flex flex-col bg-gray-50">
    <header class="bg-white shadow-md p-4 flex justify-between items-center">
      <router-link to="/" class="flex items-center space-x-2">
        <img src="/mascot1.png" alt="Tutor Platform Logo" class="h-8 w-8 rounded-full" />
        <h1 class="text-xl font-bold text-blue-700">Tutor Platform</h1>
      </router-link>
      <div class="flex space-x-4">
        <router-link to="/profile" class="btn-primary flex items-center">
          <i class="fas fa-user mr-2"></i> Мой профиль
        </router-link>
        <router-link to="/" class="btn-secondary flex items-center">
          <i class="fas fa-sign-out-alt mr-2"></i> Выйти
        </router-link>
      </div>
    </header>

    <main class="flex-grow p-6 container mx-auto">
      <section class="mb-8 p-6 bg-gradient-to-r from-white to-gray-50 rounded-lg shadow-lg">
        <h2 class="text-2xl font-semibold text-gray-800 mb-6 border-b pb-2">Найти репетитора</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
          <FilterSelect
            label="Предмет"
            :options="subjects"
            v-model="filters.subject"
            class="fade-in"
          />
          <FilterSelect
            label="Рейтинг"
            :options="ratings"
            v-model="filters.rating"
            class="fade-in"
          />
          <FilterSelect
            label="Цена (руб)"
            :options="prices"
            v-model="filters.price"
            class="fade-in"
          />
          <FilterSelect
            label="Город"
            :options="cities"
            v-model="filters.city"
            class="fade-in"
          />
        </div>
      </section>

      <section>
        <transition-group name="fade" tag="div" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6" appear>
  <div
    v-for="tutor in filteredTutors"
    :key="tutor.id"
    class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-all duration-300 transform"
    :class="{'opacity-0 translate-y-10': !tutor.id, 'opacity-100 translate-y-0': tutor.id}"
  >
            <img
              src="https://source.unsplash.com/random/400x300/?portrait"
              alt="Tutor"
              class="w-full h-48 object-cover"
            />
            <div class="p-6 space-y-2">
              <h3 class="text-lg font-bold text-gray-800">{{ tutor.name }}</h3>
              <p class="text-sm text-gray-600">Предмет: {{ tutor.subject }}, опыт {{ tutor.exp }} лет</p>
              <p class="text-sm text-gray-600">Город: {{ tutor.city }}</p>
              <p class="text-sm text-gray-600">Цена: {{ tutor.price }} руб.</p>
              <p class="text-sm text-gray-600 flex items-center space-x-2">
                <span>Рейтинг:</span>
                <span class="flex relative">
                  <template v-for="n in 5" :key="n">
                    <i class="far fa-star text-gray-300"></i>
                    <i
                      v-if="tutor.rating >= n"
                      class="fas fa-star text-yellow-400 absolute top-0 left-0 overflow-hidden"
                      style="width: 100%;"
                    ></i>
                    <i
                      v-else-if="tutor.rating > n - 1"
                      class="fas fa-star text-yellow-400 absolute top-0 left-0 overflow-hidden"
                      :style="{ width: (tutor.rating - (n - 1)) * 100 + '%' }"
                    ></i>
                  </template>
                </span>
                <span class="ml-1">({{ tutor.rating.toFixed(2) }})</span>
                <span class="ml-2 text-gray-500">({{ tutor.reviewCount }} отзывов)</span>
              </p>
              <button class="btn-primary w-full">Выбрать репетитора</button>
            </div>
          </div>
        </transition-group>
      </section>
    </main>

    <footer class="bg-gray-800 text-white text-center p-6">
      <p>&copy; 2024 Tutor Platform. Все права защищены.</p>
    </footer>
  </div>
</template>

<script>
import FilterSelect from './FilterSelect.vue';

export default {
  name: 'UserDashboard',
  components: {
    FilterSelect,
  },
  data() {
    return {
      filters: {
        subject: '',
        rating: '',
        price: '',
        city: '',
      },
      subjects: [
        'Любой',
        'Начальная школа',
        'Математика',
        'Физика',
        'Русский язык',
        'Белорусский язык',
        'Иностранные языки',
        'Биология',
        'Химия',
        'История',
        'Обществоведение',
        'Предметы ВУЗов',
      ],
      ratings: ['Любой', '5', '4 и выше'],
      prices: ['Любая', '15-25', '25-35', '35-45', '45 и выше'],
      cities: ['Любой', 'Минск', 'Могилёв', 'Брест', 'Витебск', 'Гродно', 'Гомель'],
      tutors: [
        { id: 1, subject: 'Математика', rating: 4.85, price: 20, city: 'Минск', name: 'Репетитор 1', exp: 3, reviewCount: 25 },
        { id: 2, subject: 'Физика', rating: 3.92, price: 30, city: 'Могилёв', name: 'Репетитор 2', exp: 7, reviewCount: 18 },
        { id: 3, subject: 'Русский язык', rating: 5.00, price: 40, city: 'Брест', name: 'Репетитор 3', exp: 4, reviewCount: 32 },
        { id: 4, subject: 'Математика', rating: 4.18, price: 50, city: 'Витебск', name: 'Репетитор 4', exp: 6, reviewCount: 11 },
        { id: 5, subject: 'Химия', rating: 4.50, price: 20, city: 'Гродно', name: 'Репетитор 5', exp: 2, reviewCount: 29 },
        { id: 6, subject: 'Биология', rating: 3.55, price: 30, city: 'Гомель', name: 'Репетитор 6', exp: 4, reviewCount: 15 },
      ],
    };
  },
  computed: {
    filteredTutors() {
      return this.tutors.filter(tutor => {
        const isSubjectMatch = this.filters.subject === '' || this.filters.subject === 'Любой' || tutor.subject === this.filters.subject;
        const isRatingMatch = this.filters.rating === '' || this.filters.rating === 'Любой' ||
                             (this.filters.rating === '5' && tutor.rating >= 5) ||
                             (this.filters.rating === '4 и выше' && tutor.rating >= 4);
        const isPriceMatch = this.filters.price === '' || this.filters.price === 'Любая' || (() => {
          if (this.filters.price && this.filters.price !== 'Любая') {
            const [min, max] = this.filters.price.split('-').map(Number);
            return tutor.price >= min && tutor.price <= max;
          }
          return true;
        })();
        const isCityMatch = this.filters.city === '' || this.filters.city === 'Любой' || tutor.city === this.filters.city;

        return isSubjectMatch && isRatingMatch && isPriceMatch && isCityMatch;
      });
    },
  },
};
</script>

<style scoped>
/* Анимация появления/исчезновения карточек */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

/* Стиль для карточек */
.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* Кнопка */
.btn-primary {
  background-color: #4a90e2;
  color: white;
  padding: 12px 24px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  width: 100%;
  transition: background-color 0.2s ease;
}

.btn-primary:hover {
  background-color: #3b56cc;
}
</style>
