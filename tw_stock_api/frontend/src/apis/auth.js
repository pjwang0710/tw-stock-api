// import { LoaderTargetPlugin } from 'webpack';
import req from './https';

const auth = {
    signup(params) {
      return req.post('/users/insert_user', params);
    },
    login(params) {
        return req.post('/users/login', params);
    },
    getDetails() {
        return req.get('/users/get_user_detail');
    },
    updateDetails(params) {
      return req.post('/users/update_user', params);
    },
    getSecretKey() {
      return req.get('/users/get_secret_key');
    },
    updateSecretKey() {
      return req.post('/users/update_secret_key');
    },
    getApiUseCount(){
      return req.get('/users/get_api_use_count');
    }
}

export default auth;