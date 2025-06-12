<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-300 via-purple-400 to-pink-400 py-12 px-4 sm:px-6 lg:px-8">
    <div class="w-full max-w-5xl mx-auto p-8 bg-white bg-opacity-80 rounded-3xl shadow-2xl">
      <div class="flex flex-wrap justify-center -mx-4">

        <div class="w-full sm:w-1/2 px-4 mb-8 sm:mb-0">
          <div class="p-8 bg-white rounded-2xl shadow-lg transition duration-300 registration-form-card">
            <h2 class="text-4xl font-bold text-center text-gray-800 mb-8 font-heading">Регистрация для студентов</h2>
            <form @submit.prevent="submitForm" class="space-y-6" novalidate>

              <!-- Никнейм -->
              <div class="relative group cursor-pointer text-gray-500">
                <label for="nickname" class="block text-gray-700 font-semibold font-body flex items-center gap-2">
                  Никнейм
                  <div
                    @mouseenter="showNicknameTip = true"
                    @mouseleave="showNicknameTip = false"
                    class="relative cursor-pointer text-blue-600 flex items-center"
                    aria-describedby="nickname-tip"
                    tabindex="0"
                    @focus="showNicknameTip = true"
                    @blur="showNicknameTip = false"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" >
                      <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 16v-4m0-4h.01" />
                    </svg>
                    <div
                      v-if="showNicknameTip"
                      id="nickname-tip"
                      class="absolute top-1/2 left-1/4 ml-2 -translate-y-1/2 w-72 bg-white text-sm text-gray-800 rounded-xl px-4 py-3 shadow-2xl font-body z-50 border border-gray-200 opacity-0 scale-95 group-hover:opacity-90 group-hover:scale-100 transition-all duration-300 ease-out pointer-events-none"

                      role="tooltip"
                    >
                      Никнейм укажите сейчас, а настоящее имя и фамилию можно будет добавить позже в профиле
                    </div>
                  </div>
                </label>
                <div class="relative">
                  <input
                    type="text"
                    id="nickname"
                    v-model="form.nickname"
                    @input="validateNickname"
                    placeholder="Введите никнейм"
                    class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-300 font-body outline-none pr-10"
                    required
                    autocomplete="username"
                  />
                  <button
                    v-if="form.nickname"
                    type="button"
                    @click="form.nickname = ''"
                    class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 focus:outline-none"
                    aria-label="Очистить поле никнейм"
                  >
                    ×
                  </button>
                </div>
                <p v-if="nicknameError" class="text-red-600 text-sm mt-1">{{ nicknameError }}</p>
              </div>

              <!-- Email -->
              <div class="space-y-1 relative">
                <label for="email" class="block text-gray-700 font-semibold font-body">Электронная почта</label>
                <div class="relative">
                  <input
                    type="email"
                    id="email"
                    v-model="form.email"
                    @input="validateEmail"
                    placeholder="example@mail.com"
                    class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-300 font-body outline-none pr-10"
                    required
                    autocomplete="email"
                  />
                  <button
                    v-if="form.email"
                    type="button"
                    @click="form.email = ''"
                    class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 focus:outline-none"
                    aria-label="Очистить поле email"
                  >
                    ×
                  </button>
                </div>
                <p v-if="emailError" class="text-red-600 text-sm mt-1">{{ emailError }}</p>
              </div>

              <!-- Пароль -->
              <div class="space-y-1 relative">
                <label for="password" class="block text-gray-700 font-semibold font-body flex items-center justify-between">
                  <span>Пароль</span>
                  <button
                    type="button"
                    @click="togglePassword"
                    class="text-blue-600 hover:text-blue-800 focus:outline-none text-sm"
                    :aria-label="showPassword ? 'Скрыть пароль' : 'Показать пароль'"
                  >
                    {{ showPassword ? 'Скрыть' : 'Показать' }}
                  </button>
                </label>
                <div class="relative">
                  <input
                    :type="showPassword ? 'text' : 'password'"
                    id="password"
                    v-model="form.password"
                    @input="validatePassword"
                    placeholder="Ваш надёжный пароль"
                    class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-300 font-body outline-none pr-10"
                    required
                    autocomplete="new-password"
                  />
                  <button
                    v-if="form.password"
                    type="button"
                    @click="form.password = ''"
                    class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 focus:outline-none"
                    aria-label="Очистить поле пароль"
                  >
                    ×
                  </button>
                </div>
                <p v-if="passwordError" class="text-red-600 text-sm mt-1">{{ passwordError }}</p>
              </div>

              <!-- Подтверждение пароля -->
              <div class="space-y-1 relative">
                <label for="confirmPassword" class="block text-gray-700 font-semibold font-body">Подтвердите пароль</label>
                <div class="relative">
                  <input
                    :type="showPassword ? 'text' : 'password'"
                    id="confirmPassword"
                    v-model="form.confirmPassword"
                    @input="validateConfirmPassword"
                    placeholder="Повторите пароль"
                    class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-300 font-body outline-none pr-10"
                    required
                    autocomplete="new-password"
                  />
                  <button
                    v-if="form.confirmPassword"
                    type="button"
                    @click="form.confirmPassword = ''"
                    class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 focus:outline-none"
                    aria-label="Очистить поле подтверждение пароля"
                  >
                    ×
                  </button>
                </div>
                <p v-if="confirmPasswordError" class="text-red-600 text-sm mt-1">{{ confirmPasswordError }}</p>
              </div>

              <!-- Кнопка -->
              <div>
                <button
                  :disabled="!formIsValid"
                  type="submit"
                  class="w-full bg-gradient-to-r from-blue-500 to-purple-500 text-white font-bold py-3 rounded-xl shadow-md transition-transform duration-150 ease-in-out transform hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed font-body"
                >
                  Зарегистрироваться
                </button>
              </div>

            </form>
          </div>
        </div>

        <div class="w-full sm:w-1/2 px-4 flex items-center justify-center">
          <img
            src="mascot1.png"
            alt="Registration Image"
            class="w-full h-auto object-contain transition-transform duration-500 transform hover:scale-105"
          />
        </div>

      </div>
    </div>

    <!-- Уведомление успешной регистрации -->
    <transition name="fade">
      <div
        v-if="showSuccess"
        class="fixed top-5 right-5 bg-green-500 text-white px-6 py-3 rounded-xl shadow-lg font-body z-50"
      >
        Регистрация прошла успешно! Сейчас перенаправим...
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const form = ref({
  nickname: '',
  email: '',
  password: '',
  confirmPassword: ''
});

const showPassword = ref(false);
const showNicknameTip = ref(false);
const showSuccess = ref(false);

const nicknameError = ref('');
const emailError = ref('');
const passwordError = ref('');
const confirmPasswordError = ref('');

// Валидация никнейма (мин. 3 символа, буквы, цифры, _)
const validateNickname = () => {
  const nick = form.value.nickname.trim();
  if (nick.length < 3) {
    nicknameError.value = 'Никнейм должен быть минимум 3 символа';
  } else if (!/^[a-zA-Z0-9_]+$/.test(nick)) {
    nicknameError.value = 'Никнейм может содержать только буквы, цифры и _';
  } else {
    nicknameError.value = '';
  }
};

// Валидация email
const validateEmail = () => {
  const email = form.value.email.trim();
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    emailError.value = 'Введите корректный email';
  } else {
    emailError.value = '';
  }
};

// Валидация пароля (мин. 6 символов)
const validatePassword = () => {
  if (form.value.password.length < 6) {
    passwordError.value = 'Пароль должен быть не менее 6 символов';
  } else {
    passwordError.value = '';
  }
  // Также проверим подтверждение пароля заново, если оно заполнено
  if (form.value.confirmPassword) validateConfirmPassword();
};

// Валидация подтверждения пароля
const validateConfirmPassword = () => {
  if (form.value.confirmPassword !== form.value.password) {
    confirmPasswordError.value = 'Пароли не совпадают';
  } else {
    confirmPasswordError.value = '';
  }
};

const formIsValid = computed(() => {
  return (
    form.value.nickname &&
    !nicknameError.value &&
    form.value.email &&
    !emailError.value &&
    form.value.password &&
    !passwordError.value &&
    form.value.confirmPassword &&
    !confirmPasswordError.value
  );
});

const togglePassword = () => {
  showPassword.value = !showPassword.value;
};

const submitForm = () => {
  validateNickname();
  validateEmail();
  validatePassword();
  validateConfirmPassword();

  if (!formIsValid.value) return;

  // Здесь должна быть логика регистрации (API, например)
  // Для примера покажем успех и редирект через 2 секунды

  showSuccess.value = true;
  setTimeout(() => {
    showSuccess.value = false;
    router.push('/dashboard');
  }, 2000);
};
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

</style>