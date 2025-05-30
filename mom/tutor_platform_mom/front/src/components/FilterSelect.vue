<template>
  <div class="relative bg-gradient-to-r from-gray-50 to-white p-4 rounded-lg shadow-lg">
    <label :for="id" class="block text-gray-700 font-semibold mb-2">{{ label }}</label>
    <div class="relative">
      <button
        @click="toggleDropdown"
        :class="{
          'border-blue-400 ring-2 ring-blue-300': isOpen,
          'border-gray-300': !isOpen
        }"
        class="w-full bg-white border rounded-lg px-3 py-2 text-sm flex justify-between items-center transition duration-150"
      >
        <span>{{ selected || placeholder }}</span>
        <svg
          :class="{'transform rotate-180': isOpen}"
          class="fill-current h-4 w-4 transition-transform duration-200"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
        >
          <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
        </svg>
      </button>
      <transition name="dropdown">
        <div v-show="isOpen" class="absolute z-10 mt-1 w-full bg-white border border-gray-300 rounded-lg shadow-lg overflow-hidden">
          <div v-if="isRange" class="px-4 py-2">
            <input
              type="range"
              :min="min"
              :max="max"
              v-model.number="rangeValue"
              class="w-full transition duration-300 ease-in-out"
            />
            <div class="flex justify-between text-xs text-gray-500">
              <span>{{ min }}</span>
              <span>{{ rangeValue }}</span>
              <span>{{ max }}</span>
            </div>
          </div>
          <ul v-else>
            <li
              v-for="option in options"
              :key="option"
              @click="selectOption(option)"
              class="px-4 py-2 cursor-pointer hover:bg-blue-100 transition duration-300 transform hover:scale-105"
            >
              {{ option }}
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
    options: Array,
    modelValue: [String, Number],
    placeholder: {
      type: String,
      default: "Выберите значение",
    },
    isRange: {
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
      selected: this.modelValue,
      rangeValue: this.isRange && this.modelValue ? Number(this.modelValue.split('-')[1]) : this.min,
    };
  },
  methods: {
    toggleDropdown() {
      this.isOpen = !this.isOpen;
    },
    selectOption(option) {
      this.selected = option;
      this.$emit("update:modelValue", option);
      this.isOpen = false;
    },
  },
  computed: {
    id() {
      return this.label.toLowerCase().replace(/\s+/g, "-");
    },
  },
  watch: {
    modelValue(newVal) {
      this.selected = newVal;
      if (this.isRange && newVal) {
        this.rangeValue = Number(newVal.split('-')[1]);
      } else if (!this.isRange) {
        this.rangeValue = this.min;
      }
    },
    rangeValue(newVal) {
      if (this.isRange) {
        this.$emit("update:modelValue", `0-${newVal}`);
      } else {
        this.$emit("update:modelValue", newVal);
      }
    },
  },
};
</script>

<style scoped>
/* Анимация для появления выпадающего списка */
.dropdown-enter-active, .dropdown-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.dropdown-enter, .dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Плавная анимация для range input */
input[type="range"] {
  transition: all 0.3s ease;
}

/* Hover эффект для списка */
ul li {
  transition: transform 0.3s ease, background-color 0.3s ease;
}
ul li:hover {
  transform: scale(1.05);
  background-color: #e0f7fa;
}
</style>
