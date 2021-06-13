<template>
  <div class="flex flex-row min-h-screen bg-gray-100 text-gray-800">
    <Sidebar />
    <main class="main flex flex-col flex-grow -ml-64 md:ml-0 transition-all duration-150 ease-in">
        <Header />
        
        <div class="md:grid md:grid-cols-1 mt-10">
            <div class="md:mt-0 md:col-span-2 mx-auto">
            <form action="#" method="POST">
                <div class="grid grid-cols-5 gap-6">
                <div class="col-span-6 sm:col-span-3">
                    <label for="first_name" class="block text-sm font-medium text-gray-700">First name</label>
                    <input class="mt-2 appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" v-model="userInfo.first_name" id="first_name" name="first_name" type="text" placeholder="Jane">
                </div>

                <div class="col-span-6 sm:col-span-3">
                    <label for="last_name" class="block text-sm font-medium text-gray-700">Last name</label>
                    <input class="mt-2 appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" v-model="userInfo.last_name" id="last_name" name="last_name" type="text" placeholder="Doe">
                </div>

                <div class="col-span-6">
                    <label for="email_address" class="block text-sm font-medium text-gray-700">Email address</label>
                    <input class="mt-2 appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" v-model="userInfo.email" id="email" name="email" type="text" placeholder="Email">
                </div>
                <div class="col-span-6">
                    <div class="relative text-gray-700">
                        <label for="secret_key" class="block text-sm font-medium text-gray-700">Secret key</label>
                        <input class="mt-2 appearance-none block w-full text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" v-model="secret_key" id="secret_key" name="secret_key" type="text">
                        <button type="button" class="mt-7 absolute inset-y-0 right-0 flex items-center px-4 py-3 font-bold text-white bg-indigo-600 rounded-r-lg hover:bg-indigo-500 focus:bg-indigo-700" @click="updateSecretKey">{{  this.display }}</button>
                    </div>
                </div>
                <div class="col-span-6 text-center">
                    <button type="button" class="justify-center py-4 px-6 border border-transparent shadow-sm text-lg font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500" @click="updateDetails">
                        儲存
                    </button>
                    <!-- <button class="mt-7 flex items-center px-4 py-3 font-bold text-white bg-indigo-600 rounded-r-lg hover:bg-indigo-500 focus:bg-indigo-700">儲存</button> -->
                </div>
                </div>
                
            </form>
            </div>
        </div>
    </main>
  </div>
</template>

<script>

import Sidebar from './Sidebar.vue'
import Header from './Header.vue'
import { useToast } from 'vue-toastification'

const toast = useToast()

export default {
  name: 'Dashboard',
  components: {
    Sidebar,
    Header,
  },
  data() {
    return {
      userInfo: {
        first_name: '',
        last_name: '',
        email: ''
      },
      secret_key: '',
      display: '更新',
    }
  },
  methods: {
      async getUserDetails(){
        this.$api.auth.getDetails().then(async (response) => {
            const { data } = response;
            console.log(data)
            this.userInfo.first_name = data[0].first_name;
            this.userInfo.last_name = data[0].last_name;
            this.userInfo.email = data[0].email;
        }).catch(() => {
            toast.error('不明錯誤')
        });
      },
      async getSecretKey(){
        this.$api.auth.getSecretKey().then(async (response) => {
            const { data } = response;
            console.log(data)
            this.secret_key = data[0].secret_key;
        }).catch(() => {
            this.display = '新增'
        });
      },
      async updateSecretKey(){
        this.$api.auth.updateSecretKey().then(async (response) => {
            const { data } = response;
            console.log(data)
            this.secret_key = data.secret_key;
            this.display = '更新'
            toast.success('更新成功')
        }).catch(() => {
            toast.error('不明錯誤')
        });
      },
      async updateDetails(){
        this.$api.auth.updateDetails(this.userInfo).then(async (response) => {
            const { data } = response;
            console.log(data)
            toast.success('更新成功')
            window.location.reload();
        }).catch(() => {
            toast.error('不明錯誤')
        });
      },
      
  },
  mounted() {
    this.getUserDetails();
    this.getSecretKey();
  }
}
</script>