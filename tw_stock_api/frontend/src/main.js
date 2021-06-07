import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store';
import api from './apis';
import Toast, {POSITION} from "vue-toastification";
import "vue-toastification/dist/index.css";
import "tailwindcss/tailwind.css"

import PerfectScrollbar from 'vue3-perfect-scrollbar'
import 'vue3-perfect-scrollbar/dist/vue3-perfect-scrollbar.css'

import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'

const options = {
    position: POSITION.BOTTOM_RIGHT
};
const app = createApp(App)


app.use(router)
app.use(store)

app.use(Toast, options)
app.use(PerfectScrollbar)
app.use(VueSidebarMenu)

app.config.globalProperties.$api = api;

app.mount('#app')
