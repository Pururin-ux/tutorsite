<template>
  <div class="relative p-4 rounded-xl bg-white shadow-md">
    <label :for="id" class="block text-sm font-semibold text-gray-700 mb-2">
      {{ label }}
    </label>

    <div class="relative">
      <input
        v-if="isSearch"
        :id="id"
        type="text"
        :value="modelValue"
        @input="updateSearchValue"
        :placeholder="placeholder"
        class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2 text-sm shadow-sm transition duration-200 hover:border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400"
      />

      <button
        v-else
        @click="toggleDropdown"
        class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2 text-sm flex justify-between items-center shadow-sm transition duration-200 hover:border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400 cursor-pointer"
        tabindex="0"
        @keydown.enter="toggleDropdown"
        @keydown.space="toggleDropdown"
      >
        <span class="text-gray-800 truncate">{{ displayValue || placeholder }}</span>
        <svg
          :class="['h-4 w-4 transition-transform duration-300 ease-in-out text-gray-500', { 'rotate-180': isOpen }]"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewbox="0 0 24 24"
          stroke="currentColor"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      <transition name="dropdown">
        <div
          v-show="isOpen"
          class="absolute z-10 mt-2 w-full bg-white border border-gray-200 rounded-xl shadow-lg overflow-hidden max-h-60 overflow-y-auto custom-scrollbar"
        >
          <div v-if="isRange" class="px-4 py-4">
            <input
              type="range"
              :min="min"
              :max="max"
              v-model.number="rangeValue"
              class="w-full appearance-none"
            />
            <div class="flex justify-between text-xs text-gray-500 mt-1">
              <span>{{ min }}</span>
              <span class="font-semibold text-blue-600">{{ rangeValue }}</span>
              <span>{{ max }}</span>
            </div>
          </div>
          <ul v-else>
            <li
              v-for="option in options"
              :key="option.value !== undefined ? option.value : option"
              @click="selectOption(option)"
              :class="{
                'bg-blue-50 text-blue-700 font-medium':
                  (isSort && option.value === modelValue) || (!isSort && option === modelValue),
                'hover:bg-blue-100 hover:text-blue-700':
                  (isSort && option.value !== modelValue) || (!isSort && option !== modelValue),
              }"
              class="px-4 py-2 text-gray-700 cursor-pointer transition duration-200"
            >
              {{ isSort ? option.label : option }}
            </li>
          </ul>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: "FilterSelect",
  props: {
    label: String,
    options: {
      type: Array,
      default: () => [],
    },
    modelValue: [String, Number],
    placeholder: {
      type: String,
      default: "Выберите значение",
    },
    isRange: {
      type: Boolean,
      default: false,
    },
    isSearch: {
      type: Boolean,
      default: false,
    },
    isSort: {
      type: Boolean,
      default: false,
    },
    min: {
      type: Number,
      default: 0,
    },
    max: {
      type: Number,
      default: 100,
    },
  },
  data() {
    return {
      isOpen: false,
      selected: this.modelValue, // Используем для обычных фильтров
      rangeValue: this.isRange && this.modelValue ? Number(this.modelValue.split("-")[1]) : this.min,
    };
  },
  methods: {
    toggleDropdown() {
      if (this.isSearch) return; // Поиск не имеет выпадающего списка
      this.isOpen = !this.isOpen;
      if (this.isOpen) {
        document.addEventListener('click', this.handleClickOutside);
      } else {
        document.removeEventListener('click', this.handleClickOutside);
      }
    },
    selectOption(option) {
      if (this.isSort) {
        this.$emit("update:modelValue", option.value);
      } else {
        this.$emit("update:modelValue", option);
      }
      this.isOpen = false;
      document.removeEventListener('click', this.handleClickOutside);
    },
    updateSearchValue(event) {
      if (this.isSearch) {
        this.$emit("update:modelValue", event.target.value);
      }
    },
    handleClickOutside(event) {
      if (!this.$el.contains(event.target)) {
        this.isOpen = false;
        document.removeEventListener('click', this.handleClickOutside);
      }
    },
  },
  computed: {
    id() {
      return this.label.toLowerCase().replace(/\s+/g, "-");
    },
    displayValue() {
      if (this.isSort) {
        // Найти метку для текущего выбранного значения сортировки
        const selectedOption = this.options.find(opt => opt.value === this.modelValue);
        return selectedOption ? selectedOption.label : '';
      }
      return this.selected;
    }
  },
  watch: {
    modelValue(newVal) {
      if (!this.isSearch && !this.isSort) { // Только для обычных фильтров
        this.selected = newVal;
      }
      if (this.isRange && typeof newVal === 'string' && newVal.includes('-')) {
        this.rangeValue = Number(newVal.split("-")[1]);
      } else if (this.isRange && (newVal === null || newVal === undefined || newVal === '')) {
         this.rangeValue = this.min; // Сброс, если значение range обнулено
      }
    },
    rangeValue(newVal) {
      if (this.isRange) {
        this.$emit("update:modelValue", `0-${newVal}`);
      }
    },
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleClickOutside);
  }
};
</script>

<style scoped>
/* Базовый стиль контейнера */
.relative.p-4.rounded-xl.bg-white.shadow-md {
  min-width: 150px; /* Чтобы не сжимался сильно */
}

/* Анимация dropdown */
.dropdown-enter-active,
.dropdown-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.dropdown-enter-from, /* Vue 3 syntax */
.dropdown-leave-to { /* Vue 3 syntax */
  opacity: 0;
  transform: translateY(-10px);
}

/* Стилизация range */
input[type="range"] {
  transition: all 0.3s ease;
  width: 100%;
  height: 0.5rem;
  background-color: transparent;
}

input[type="range"]::-webkit-slider-runnable-track {
  background: #d1d5db; /* Tailwind gray-300 */
  height: 4px;
  border-radius: 9999px;
}
input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  height: 1rem;
  width: 1rem;
  background: #3b82f6; /* Tailwind blue-500 */
  border-radius: 9999px;
  margin-top: -6px;
  /* Centering the thumb on the track */
  cursor: pointer;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  transition: background 0.2s ease, box-shadow 0.2s ease;
}
input[type="range"]::-moz-range-track {
  background: #d1d5db;
  height: 4px;
  border-radius: 9999px;
}
input[type="range"]::-moz-range-thumb {
  height: 1rem;
  width: 1rem;
  background: #3b82f6;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  transition: background 0.2s ease, box-shadow 0.2s ease;
}

/* Добавленные стили для скроллбара */
.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #f0f0f0;
  border-radius: 4px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #cbd5e0; /* Tailwind gray-300 */
  border-radius: 4px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #a0aec0; /* Tailwind gray-400 */
}
</style>