<template>
  <div>
    <LandingNav />
    <div class="flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
        <div>
        <img class="mx-auto h-12 w-auto" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="Workflow">
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
            會員登入
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
            <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500">
            已經有帳號了？
            </a>
        </p>
        </div>
        <form class="mt-8 space-y-6" action="#" method="POST">
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
            <div>
            <label for="email-address" class="sr-only">Email</label>
            <input id="email-address" v-model="loginInfo.email" name="email" type="email" autocomplete="email" required class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Email address">
            </div>
            <div>
            <label for="password" class="sr-only">Password</label>
            <input id="password" v-model="loginInfo.hashed_password" name="password" type="password" autocomplete="current-password" required class="mt-5 appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password">
            </div>
        </div>

        <div class="flex items-center justify-between">
            <div class="flex items-center">
            <input id="remember_me" name="remember_me" type="checkbox" class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded">
            <label for="remember_me" class="ml-2 block text-sm text-gray-900">
                記住我
            </label>
            </div>

            <div class="text-sm">
            <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500">
                忘記密碼
            </a>
            </div>
        </div>

        <div>
            <button type="button" @click="login()" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                <!-- Heroicon name: solid/lock-closed -->
                <svg class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
                </svg>
            </span>
            登入
            </button>
        </div>
        </form>
    </div>
    </div>
  </div>
</template>

<script>
// import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
import LandingNav from './LandingNav.vue'
import { useToast } from 'vue-toastification'
import { mapMutations } from 'vuex';

const toast = useToast()

export default {
  name: 'LandingPage',
  components: {
    LandingNav
  },
  data() {
    return {
      loginInfo: {
        email: '',
        hashed_password: ''
      }
    }
  },
  methods: {
    ...mapMutations('auth', [
      'SET_AUTH_TOKEN',
    ]),
    async login(){
      this.$api.auth.login(this.loginInfo).then(async (response) => {
        const { data } = response;
        if (data.token) {
          this.SET_AUTH_TOKEN(data.token);
          window.location.reload();
        }
      }).catch((err) => {
        toast.error(err)
      });
    }
  }
}
</script>