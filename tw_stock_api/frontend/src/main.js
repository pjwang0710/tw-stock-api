import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store';
import api from './apis';
import Toast from "vue-toastification";
import "tailwindcss/tailwind.css"

const options = {
    confirmButtonColor: '#17A2B8',
    cancelButtonColor: '#FF4F44',
};
const app = createApp(App)


app.use(router)
app.use(store)

app.use(Toast, options)

app.config.globalProperties.$api = api;

app.mount('#app')
