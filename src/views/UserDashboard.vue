<template>
  <div class="min-h-screen flex flex-col bg-gray-50">
    <header class="bg-white shadow-md p-4 flex justify-between items-center flex-wrap gap-4">
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

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
          <FilterSelect label="Предмет" :options="subjects" v-model="filters.subject" />
          <FilterSelect label="Рейтинг" :options="ratings" v-model="filters.rating" />
          <FilterSelect label="Цена (руб)" :options="prices" v-model="filters.price" :is-range="true" :min="0" :max="100" />
          <FilterSelect label="Город" :options="cities" v-model="filters.city" />
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <FilterSelect
            label="Поиск по имени"
            placeholder="Введите имя..."
            :is-search="true"
            v-model="filters.name"
          />

          <FilterSelect
            label="Сортировать по"
            :options="sortOptions"
            :is-sort="true"
            v-model="sortBy"
            placeholder="Выберите тип сортировки"
          />
        </div>
      </section>

      <section>
        <transition-group
          name="fade"
          tag="div"
          class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
          appear
        >
          <div
            v-for="tutor in sortedTutors"
            :key="tutor.id"
            class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-all duration-300 transform"
          >
            <img
              :src="tutor.image || '/default-avatar.png'"
              :alt="`Фото репетитора ${tutor.name}`"
              class="w-full h-[400px] object-cover rounded-t-lg"
            />
            <div class="p-6 space-y-2">
              <div class="flex items-center space-x-2">
                <span
                  :class="getStatusClass(tutor.status, tutor.lastOnline).colorClass"
                  v-tippy="{ content: getStatusClass(tutor.status, tutor.lastOnline).tooltipText }"
                  class="h-2 w-2 rounded-full cursor-pointer"
                ></span>
                <h3 class="text-lg font-bold text-gray-800">{{ tutor.name }}</h3>
              </div>
              <div>
                <span class="inline-block px-2 py-1 text-xs font-medium rounded-full bg-blue-100 text-blue-700">
                  {{ tutor.subject }}
                </span>
              </div>
              <p class="text-sm text-gray-600">Опыт: {{ tutor.exp }} лет</p>
              <p class="text-sm text-gray-600">Город: {{ tutor.city }}</p>
              <p class="text-sm text-gray-600">Цена: {{ tutor.price }} руб.</p>
              <p class="text-sm text-gray-600 flex items-center space-x-2">
                <span class="relative flex items-center">
                  <span class="flex text-gray-300">
                    <i class="fas fa-star" v-for="n in 5" :key="n"></i>
                  </span>
                  <span
                    class="flex text-yellow-400 absolute top-0 left-0 overflow-hidden"
                    :style="{ width: (tutor.rating / 5) * 100 + '%' }"
                  >
                    <i class="fas fa-star" v-for="n in 5" :key="n"></i>
                  </span>
                </span>
                <span class="ml-1">({{ tutor.rating?.toFixed(2) ?? '—' }})</span>
                <span class="ml-2 text-gray-500">({{ tutor.reviewCount }} отзывов)</span>
              </p>

              <button class="btn-primary w-full">Выбрать репетитора</button>
            </div>
          </div>
        </transition-group>
      </section>
    </main>

    <footer class="bg-gray-800 text-white text-center p-6 mt-4">
      <p>&copy; 2024 Tutor Platform. Все права защищены.</p>
    </footer>
  </div>
</template>

<script>
import FilterSelect from '../components/FilterSelect.vue';

export default {
  name: 'UserDashboard',
  components: { FilterSelect },
  data() {
    return {
      sortBy: '',
      filters: {
        subject: '',
        rating: '',
        price: '',
        city: '',
        name: '',
      },
      subjects: [
        'Любой', 'Начальная школа', 'Математика', 'Физика', 'Русский язык', 'Белорусский язык',
        'Иностранные языки', 'Биология', 'Химия', 'История', 'Обществоведение', 'Предметы ВУЗов',
      ],
      // Обновленные опции для фильтрации по рейтингу
      ratings: ['Любой', '4.5 и выше', '4.0 и выше', '3.5 и выше'],
      // Оставим prices с "Любая", если цена будет исключительно через range
      prices: ['Любая'],
      cities: ['Любой', 'Минск', 'Могилёв', 'Брест', 'Витебск', 'Гродно', 'Гомель'],
      sortOptions: [
        { label: 'Цене (возрастание)', value: 'price_asc' },
        { label: 'Цене (убывание)', value: 'price_desc' },
        { label: 'Рейтингу (возрастание)', value: 'rating_asc' },
        { label: 'Рейтингу (убывание)', value: 'rating_desc' },
      ],
      tutors: [
        { id: 1, subject: 'Математика', rating: 4.85, price: 20, city: 'Минск', name: 'Репетитор 1', exp: 3, reviewCount: 25, image: 'rep1.jpg', status: 'online', lastOnline: null },
        { id: 2, subject: 'Физика', rating: 3.92, price: 30, city: 'Могилёв', name: 'Репетитор 2', exp: 7, reviewCount: 18, image: 'rep2.jpg', status: 'offline', lastOnline: new Date(Date.now() - 20 * 60 * 1000) },
        { id: 3, subject: 'Русский язык', rating: 5.00, price: 40, city: 'Брест', name: 'Репетитор 3', exp: 4, reviewCount: 32, image: 'rep3.jpg', status: 'last_seen', lastOnline: new Date(Date.now() - 5 * 60 * 1000) },
        { id: 4, subject: 'Математика', rating: 4.18, price: 50, city: 'Витебск', name: 'Репетитор 4', exp: 6, reviewCount: 11, image: 'rep4.jpg', status: 'online', lastOnline: null },
        { id: 5, subject: 'Химия', rating: 4.50, price: 20, city: 'Гродно', name: 'Репетитор 5', exp: 2, reviewCount: 29, image: 'rep5.jpg', status: 'offline', lastOnline: new Date(Date.now() - 60 * 60 * 1000) },
        { id: 6, subject: 'Биология', rating: 3.55, price: 30, city: 'Гомель', name: 'Репетитор 6', exp: 4, reviewCount: 15, image: 'rep6.jpg', status: 'last_seen', lastOnline: new Date(Date.now() - 10 * 60 * 1000) },
        { id: 7, subject: 'История', rating: 4.20, price: 35, city: 'Минск', name: 'Репетитор 7', exp: 5, reviewCount: 20, image: 'rep7.jpg', status: 'offline', lastOnline: new Date(Date.now() - 40 * 60 * 1000) },
      ],
    };
  },
  computed: {
    filteredTutors() {
      return this.tutors.filter(tutor => {
        const { subject, rating, price, city, name } = this.filters;

        const isSubjectMatch = !subject || subject === 'Любой' || tutor.subject === subject;

        const isRatingMatch =
          !rating ||
          rating === 'Любой' ||
          (rating === '4.5 и выше' && tutor.rating >= 4.5) ||
          (rating === '4.0 и выше' && tutor.rating >= 4.0) ||
          (rating === '3.5 и выше' && tutor.rating >= 3.5);

        const isPriceMatch =
          !price ||
          price === 'Любая' ||
          (() => {
            if (typeof price === 'string' && price.includes('-')) {
              const [minRange, maxRange] = price.split('-').map(Number);
              return tutor.price >= minRange && tutor.price <= maxRange;
            }
            return true;
          })();

        const isCityMatch = !city || city === 'Любой' || tutor.city === city;
        const isNameMatch = !name || tutor.name.toLowerCase().includes(name.toLowerCase());

        return isSubjectMatch && isRatingMatch && isPriceMatch && isCityMatch && isNameMatch;
      });
    },
    sortedTutors() {
      const sorted = [...this.filteredTutors];
      if (this.sortBy === 'price_asc') sorted.sort((a, b) => a.price - b.price);
      if (this.sortBy === 'price_desc') sorted.sort((a, b) => b.price - a.price);
      if (this.sortBy === 'rating_asc') sorted.sort((a, b) => a.rating - b.rating);
      if (this.sortBy === 'rating_desc') sorted.sort((a, b) => b.rating - a.rating);
      return sorted;
    },
  },
  methods: {
    getStatusClass(status, lastOnline) {
      const fifteenMinutesAgo = new Date(Date.now() - 15 * 60 * 1000);
      const currentTime = new Date();
      let colorClass = 'bg-gray-300';
      let tooltipText = 'Статус неизвестен';

      if (status === 'online') {
        colorClass = 'bg-green-500';
        tooltipText = 'Онлайн';
      } else if (status === 'offline' || status === 'last_seen') {
        if (lastOnline && lastOnline instanceof Date) {
          if (lastOnline > fifteenMinutesAgo) {
            colorClass = 'bg-gray-400';
            const minutesAgo = Math.round((currentTime - lastOnline) / (1000 * 60));
            tooltipText = `Был в сети ${minutesAgo} мин. назад`;
          } else {
            colorClass = 'bg-red-500';
            tooltipText = 'Оффлайн';
          }
        } else {
          colorClass = 'bg-red-500';
          tooltipText = 'Оффлайн';
        }
      }

      return { colorClass, tooltipText };
    },
  }
};
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
.fade-leave-active {
  position: absolute;
}

.btn-primary {
  background-color: #4a90e2;
  color: white;
  padding: 12px 24px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  transition: background-color 0.2s ease;
}

.btn-primary:hover {
  background-color: #3b56cc;
}

.btn-secondary {
  background-color: transparent;
  border: 2px solid #4a90e2;
  color: #4a90e2;
  padding: 12px 24px;
  font-size: 16px;
  border-radius: 5px;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background-color: #4a90e2;
  color: white;
}
</style>