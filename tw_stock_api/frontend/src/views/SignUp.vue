<template>
  <div>
    <LandingNav />
    <section class="relative pt-16 items-center flex h-screen max-w-7xl mx-auto">
      <div class="grid mx-auto">
        <div class="mt-5">
          <form action="#" method="POST">
              <div class="shadow overflow-hidden sm:rounded-md">
              <div class="px-4 py-5 bg-white sm:p-6">
                  <div class="grid grid-cols-6 gap-6">
                  <div class="col-span-6 sm:col-span-3">
                      <label for="first_name" class="block text-sm font-medium text-gray-700">First name</label>
                      <input class="mt-2 appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="first_name" v-model="signupInfo.first_name" name="first_name" type="text" placeholder="Jane">
                  </div>

                  <div class="col-span-6 sm:col-span-3">
                      <label for="last_name" class="block text-sm font-medium text-gray-700">Last name</label>
                      <input class="mt-2 appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="last_name" v-model="signupInfo.last_name" name="last_name" type="text" placeholder="Doe">
                  </div>

                  <div class="col-span-6">
                      <label for="email_address" class="block text-sm font-medium text-gray-700">Email address</label>
                      <input class="mt-2 appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="email" v-model="signupInfo.email" name="email" type="text" placeholder="Email">
                  </div>
                  <div class="col-span-6 sm:col-span-3">
                      <label for="password1" class="block text-sm font-medium text-gray-700">Password</label>
                      <input class="mt-2 appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="password1" v-model="password1" name="password1" type="password">
                  </div>

                  <div class="col-span-6 sm:col-span-3">
                      <label for="password2" class="block text-sm font-medium text-gray-700">Confirm password</label>
                      <input class="mt-2 appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="password2" v-model="password2" name="password2" type="password">
                  </div>
                  </div>
              </div>
              <div class="px-4 py-3 bg-gray-50 text-right sm:px-6">
                  <button type="button" @click="signUp()"  class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                  Submit
                  </button>
              </div>
              </div>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
import LandingNav from "./LandingNav.vue";
import { useToast } from 'vue-toastification'
import { required, email, minLength } from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'

const toast = useToast()

export default {
  name: "LandingPage",
  components: {
    LandingNav,
  },
  data () {
    return {
      signupInfo: {
        first_name: '',
        last_name: '',
        email: ''
      },
      password1: '',
      password2: ''
    }
  },
  setup: () => ({ v$: useVuelidate() }),
  validations () {
    return {
      signupInfo: {
        first_name: { required },
        last_name: { required },
        email: { required, email },
      },
      password1: { required, minLength: minLength(8) },
      password2: { required, minLength: minLength(8) }
    }
  },
  methods: {
    async signUp() {
      if (this.v$.signupInfo.first_name.$invalid || this.v$.signupInfo.last_name.$invalid) {
        toast.error('欄位皆為必填')
        return;
      }
      if (this.v$.signupInfo.email.$invalid) {
        toast.error('Email 不符合格式')
        return;
      }
      if (this.v$.password1.$invalid) {
        toast.error('密碼至少 8 碼')
        return;
      }
      console.log(this.v$.password2.sameAsPassword)
      if (this.password1 != this.password2) {
        toast.error('兩次密碼不同')
        return;
      }
      this.signupInfo.hashed_password = this.password1
      this.$api.auth.signup(this.signupInfo).then(async (response) => {
        const { data } = response;
        toast.success('註冊成功')
        console.log(data)
        window.location.href = '/Login';
      }).catch(() => {
        toast.error('註冊失敗')
      });
    }
  }
};
</script>