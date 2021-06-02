import * as axios from 'axios';
import store from '../store';
// import router from '../router';

// import { useToast } from 'vue-toastification'

// const toast = useToast()

// function errorHandler(response) {
//   const { status } = response;
//   const { message } = response.data;

//   switch (status) {
//     case 400:
//       toast.error(message);
//       break;
//     case 401:
//       toast.error(message);
//       break;
//     case 403:
//       toast.error(message);
//       break;
//     case 404:
//       router.replace({ name: 'NotFound' });
//       break;
//     default:
//       toast.error(response);
//       console.log('Unknown Error: ', response);
//   }
// }

const instance = axios.default.create({
  baseURL: `${process.env.VUE_APP_SERVER_URI}`,
});

instance.interceptors.request.use((config) => {
  const { token } = store.state.auth;
  const newConfig = config;
  if (token) {
    newConfig.headers.Authorization = `Bearer ${token}`;
  }
  return newConfig;
}, (error) => Promise.reject(error));

instance.interceptors.response.use((response) => response, (error) => {
  const { response } = error;
  if (response) {
    // errorHandler(response);
    return Promise.reject(error);
  }
  return Promise.reject(error);
});

export default instance;