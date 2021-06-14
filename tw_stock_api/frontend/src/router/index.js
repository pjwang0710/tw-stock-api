import { createRouter, createWebHistory } from 'vue-router'
// import _ from 'lodash';

import LandingPage from '../views/LandingPage.vue';
import Login from '../views/Login.vue';
import SignUp from '../views/SignUp.vue';
import Dashboard from '../views/Dashboard.vue';
import Profile from '../views/Profile.vue';
import APIDocument from '../views/LandingAPI.vue'
// import Invitation from '../views/Invitation.vue';
// import TraineeDashboard from '../views/TraineeDashboard.vue';
// import FirstReviewTask from '../views/FirstReviewTask.vue';

import store from '../store';

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/api',
    name: 'APIDocument',
    component: APIDocument
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: { requiresAuth: true }
  },
  // {
  //   path: '/invitation/:token',
  //   name: 'Invitation',
  //   component: Invitation,
  //   meta: { requiresAuth: true },
  // }
];


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach(async (to, from, next) => {
  const { token } = store.state.auth;
  console.log(token)
  if (to.meta.requiresAuth && !token) {
    next({ name: 'Login' });
    return;
  }
  if (token) {
    if (to.name === 'Login' || to.name == 'SignUp') {
      next({ name: 'Dashboard' });
      return;
    }
  }
  next();
});

export default router;