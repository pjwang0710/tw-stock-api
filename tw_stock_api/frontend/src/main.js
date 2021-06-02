import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store';
import api from './apis';
import Toast, {POSITION} from "vue-toastification";
import "vue-toastification/dist/index.css";
import "tailwindcss/tailwind.css"

const options = {
    position: POSITION.BOTTOM_RIGHT
};
const app = createApp(App)


app.use(router)
app.use(store)

app.use(Toast, options)

app.config.globalProperties.$api = api;

app.mount('#app')
