// import { LoaderTargetPlugin } from 'webpack';
import req from './https';

const auth = {
    signup(params) {
      return req.post('/users/insert_user', params);
    },
    login(params) {
        return req.post('/users/login', params);
    }
}

export default auth;