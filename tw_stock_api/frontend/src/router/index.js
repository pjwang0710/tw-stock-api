import { createRouter, createWebHistory } from 'vue-router'
// import _ from 'lodash';

import LandingPage from '../views/LandingPage.vue';
import Login from '../views/Login.vue';
import SignUp from '../views/SignUp.vue';
// import Admin from '../views/Admin.vue';
// import Invitation from '../views/Invitation.vue';
// import TraineeDashboard from '../views/TraineeDashboard.vue';
// import FirstReviewTask from '../views/FirstReviewTask.vue';

// import store from '../store';

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage,
  },
  // {
  //   path: '/dashboard',
  //   name: 'Dashboard',
  //   component: Dashboard,
  //   meta: { requiresAuth: true },
  //   children: [
  //     {
  //       path: 'Dashboard/Admin',
  //       component: Admin,
  //     },
  //     {
//         name: 'Dashboard/Trainee',
//         path: 'trainee',
//         component: TraineeDashboard,
//       },
//       {
//         name: 'Dashboard/Coach',
//         path: 'coach',
//         component: FirstReviewTask,
//       },
//     ],
//   },
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
//   {
//     path: '/invitation/:token',
//     name: 'Invitation',
//     component: Invitation,
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/me',
//     name: 'Profile',
//     component: () => import('../views/Profile.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/team',
//     name: 'Team',
//     component: () => import('../views/Team.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/teamInfo/:teamID',
//     name: 'TeamInfo',
//     component: () => import('../views/TeamInfo.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/team/member/:userId',
//     name: 'TeamMemberProfile',
//     component: () => import('../views/TeamMemberProfile.vue'),
//     meta: { requiresAuth: true },
//     beforeEnter: (to, from, next) => {
//       const me = store.state.profile.profile;
//       if (me._id === to.params.userId) next({ name: 'Profile' });
//       else next();
//     },
//   },
//   {
//     path: '/task1',
//     name: 'Task1',
//     component: () => import('../views/Task1/Main.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task1/overview',
//     name: 'Task1/overview',
//     component: () => import('../views/Task1/Overview.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task1/review/:taskID',
//     name: 'TaskOneReview',
//     component: () => import('../views/Task1/ReviewMain.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task2',
//     name: 'Task2',
//     component: () => import('../views/Task2/Main.vue'),
//     meta: { requiresAuth: true },
//     beforeEnter: (to, from, next) => {
//       const me = store.state.profile.profile;
//       if (me.team.taskProgress < 2) {
//         vm.$notify('請先完成前面任務', 'error');
//         next({ name: 'NotFound' });
//       } else {
//         next();
//       }
//     },
//   },
//   {
//     path: '/task2/overview',
//     name: 'Task2/overview',
//     component: () => import('../views/Task2/Overview.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task2/review/:taskID',
//     name: 'TaskTwoReview',
//     component: () => import('../views/Task2/ReviewMain.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task3',
//     name: 'Task3',
//     component: () => import('../views/Task3/Main.vue'),
//     meta: { requiresAuth: true },
//     beforeEnter: (to, from, next) => {
//       const me = store.state.profile.profile;
//       if (me.team.taskProgress < 3) {
//         vm.$notify('請先完成前面任務', 'error');
//         next({ name: 'NotFound' });
//       } else {
//         next();
//       }
//     },
//   },
//   {
//     path: '/task3/overview',
//     name: 'Task3/overview',
//     component: () => import('../views/Task3/Overview.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task3/review/:taskID',
//     name: 'TaskThreeReview',
//     component: () => import('../views/Task3/ReviewMain.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/teamProgress',
//     name: 'TeamProgress',
//     component: () => import('../views/TeamProgress.vue'),
//   },
//   {
//     path: '/task4',
//     name: 'Task4',
//     component: () => import('../views/Task4/Main.vue'),
//     meta: { requiresAuth: true },
//     beforeEnter: (to, from, next) => {
//       const me = store.state.profile.profile;
//       if (me.team.taskProgress < 4) {
//         vm.$notify('請先完成前面任務', 'error');
//         next({ name: 'NotFound' });
//       } else {
//         next();
//       }
//     },
//   },
//   {
//     path: '/task4/overview',
//     name: 'Task4/overview',
//     component: () => import('../views/Task4/Overview.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task4/review/:taskID',
//     name: 'TaskFourReview',
//     component: () => import('../views/Task4/ReviewMain.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/rethinkProgress',
//     name: 'RethinkProgress',
//     component: () => {
//       const me = store.state.profile.profile;
//       if (me.userRole === 'trainee') {
//         return import('../views/TraineeRethinkProgress.vue');
//       }
//       return import('../views/CoachRethinkProgress.vue');
//     },
//   },
//   {
//     path: '/rethinkDashboard',
//     name: 'RethinkDashboard',
//     component: () => import('../views/RethinkDashboard.vue'),
//   },
//   {
//     path: '/task5',
//     name: 'Task5',
//     component: () => import('../views/Task5/Main.vue'),
//     meta: { requiresAuth: true },
//     beforeEnter: (to, from, next) => {
//       const me = store.state.profile.profile;
//       if (me.team.taskProgress < 5) {
//         vm.$notify('請先完成前面任務', 'error');
//         next({ name: 'NotFound' });
//       } else {
//         next();
//       }
//     },
//   },
//   {
//     path: '/task5/overview',
//     name: 'Task5/Overview',
//     component: () => import('../views/Task5/Overview.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task5/review/:taskID',
//     name: 'TaskFiveReview',
//     component: () => import('../views/Task5/ReviewMain.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task6',
//     name: 'Task6',
//     component: () => import('../views/Task6/Main.vue'),
//     meta: { requiresAuth: true },
//     beforeEnter: (to, from, next) => {
//       const me = store.state.profile.profile;
//       if (me.team.taskProgress < 6) {
//         vm.$notify('請先完成前面任務', 'error');
//         next({ name: 'NotFound' });
//       } else {
//         next();
//       }
//     },
//   },
//   {
//     path: '/task6/overview',
//     name: 'Task6/Overview',
//     component: () => import('../views/Task6/Overview.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task6/review/:taskID',
//     name: 'TaskSixReview',
//     component: () => import('../views/Task6/ReviewMain.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/taskIntro/:task',
//     name: 'TaskIntro',
//     component: () => import('../views/TaskIntro.vue'),
//     meta: { requiresAuth: true },
//     beforeEnter: (to, from, next) => {
//       const me = store.state.profile.profile;
//       if (me.team.taskProgress < to.params.task) {
//         vm.$notify('請先完成前面任務', 'error');
//         next({ name: 'NotFound' });
//       } else {
//         next();
//       }
//     },
//   },
//   {
//     path: '/submitHistory',
//     name: 'SubmitHistory',
//     component: () => import('../views/SubmitHistory.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task1/history/:taskID',
//     name: 'TaskOneHistory',
//     component: () => import('../views/Task1/Overview.vue'),
//     meta: { requiresAuth: true, viewMode: true },
//   },
//   {
//     path: '/task1/reviewHistory/:taskID',
//     name: 'TaskOneReviewHistory',
//     component: () => import('../views/Task1/ReviewHistory.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task2/reviewHistory/:taskID',
//     name: 'TaskTwoReviewHistory',
//     component: () => import('../views/Task2/ReviewHistory.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task3/reviewHistory/:taskID',
//     name: 'TaskThreeReviewHistory',
//     component: () => import('../views/Task3/ReviewHistory.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task4/reviewHistory/:taskID',
//     name: 'TaskFourReviewHistory',
//     component: () => import('../views/Task4/ReviewHistory.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task5/reviewHistory/:taskID',
//     name: 'TaskFiveReviewHistory',
//     component: () => import('../views/Task5/ReviewHistory.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task6/reviewHistory/:taskID',
//     name: 'TaskSixReviewHistory',
//     component: () => import('../views/Task6/ReviewHistory.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/task2/history/:taskID',
//     name: 'TaskTwoHistory',
//     component: () => import('../views/Task2/Overview.vue'),
//     meta: { requiresAuth: true, viewMode: true },
//   },
//   {
//     path: '/task3/history/:taskID',
//     name: 'TaskThreeHistory',
//     component: () => import('../views/Task3/Overview.vue'),
//     meta: { requiresAuth: true, viewMode: true },
//   },
//   {
//     path: '/task4/history/:taskID',
//     name: 'TaskFourHistory',
//     component: () => import('../views/Task4/Overview.vue'),
//     meta: { requiresAuth: true, viewMode: true },
//   },
//   {
//     path: '/task5/history/:taskID',
//     name: 'TaskFiveHistory',
//     component: () => import('../views/Task5/Overview.vue'),
//     meta: { requiresAuth: true, viewMode: true },
//   },
//   {
//     path: '/task6/history/:taskID',
//     name: 'TaskSixHistory',
//     component: () => import('../views/Task6/Overview.vue'),
//     meta: { requiresAuth: true, viewMode: true },
//   },
//   {
//     path: '/forgot-password',
//     name: 'ForgotPassword',
//     component: () => import('../views/forgotPassword.vue'),
//   },
//   {
//     path: '/reset-password/:resetPasswordToken',
//     name: 'ResetPassword',
//     component: () => import('../views/resetPassword.vue'),
//   },
//   {
//     path: '/404',
//     name: 'NotFound',
//     component: () => import('../views/NotFound.vue'),
//   },
//   {
//     path: '/taskDashboard',
//     name: 'TaskDashboard',
//     component: () => import('../views/TaskDashboard.vue'),
//   },
//   {
//     path: '/taskFirstReviewProgress',
//     name: 'TaskFirstReviewProgress',
//     component: () => import('../views/TaskFirstReviewProgress.vue'),
//   },
//   {
//     path: '/secondaryReviewTask',
//     name: 'SecondaryReviewTask',
//     component: () => import('../views/SecondaryReviewTask.vue'),
//   },
//   {
//     path: '/coachDashboard',
//     name: 'CoachDashboard',
//     component: () => import('../views/CoachDashboard.vue'),
//   },
//   {
//     path: '/onboard',
//     name: 'Onboard',
//     component: () => import('../views/Onboard.vue'),
//   },
//   {
//     path: '/loopAction/main',
//     name: 'LoopAction',
//     component: () => import('../views/LoopAction/Main.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/history',
//     name: 'LoopAction_SubmitHistory',
//     component: () => import('../views/LoopAction/SubmitHistory.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/home',
//     name: 'LoopActionHome',
//     component: () => import('../views/LoopAction/Home.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/overview/:loopActionID',
//     name: 'LoopAction_Overview',
//     component: () => import('../views/LoopAction/Overview.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/review',
//     name: 'LoopAction_Reviews',
//     component: () => import('../views/LoopAction/Review.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/dashboard',
//     name: 'LoopActionDashboard',
//     component: () => import('../views/LoopAction/LoopActionDashboard.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/review/:loopActionID/:feedbackID',
//     name: 'LoopAction_Review',
//     component: () => import('../views/LoopAction/ReviewOverview.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/teamProgress',
//     name: 'LoopAction_TeamProgress',
//     component: () => import('../views/LoopAction/AllTeamProgress.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/profile',
//     name: 'LoopAction_Profile',
//     component: () => import('../views/LoopAction/LoopActionProfile.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/team',
//     name: 'LoopAction_Team',
//     component: () => import('../views/LoopAction/LoopActionTeam.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/onboard',
//     name: 'LoopActionOnboard',
//     component: () => import('../views/LoopAction/Onboard.vue'),
//     meta: { requiresAuth: true },
//   },
//   {
//     path: '/loopAction/teamDashboard',
//     name: 'LoopAction_TeamDashboard',
//     component: () => import('../views/LoopAction/TeamDashboard.vue'),
//   },
//   {
//     path: '/loopAction/storyline/:loopActionID',
//     name: 'LoopActionStoryline',
//     component: () => import('../views/LoopAction/Storyline.vue'),
//     meta: { requiresAuth: true },
//   },
];


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

// router.beforeEach(async (to, from, next) => {
//   const { token } = store.state.auth;

//   if (to.meta.requiresAuth && !token) {
//     next({ name: 'Login' });
//     return;
//   }

//   const { _id } = store.state.profile.profile;
//   if (token) {
//     if (!_id) {
//       try {
//         await store.dispatch('profile/getProfile');
//       } catch (error) {
//         const { status } = error.response;
//         if (status === 401) {
//           this.$notify('你沒有權限作出此操作');
//           await store.dispatch('auth/removeAuthToken');
//           await store.dispatch('profile/resetProfile');

//           next({ name: 'Login' });
//           return;
//         }
//       }
//     }
//     if (to.meta.requiresAdmin && store.state.profile.profile.userRole !== 'admin') {
//       if (_.get(store.state, 'profile.profile.team.fullAccessOfLoopAction')) {
//         next({ name: 'LoopActionHome' });
//       } else {
//         next({ name: 'Dashboard' });
//       }
//       return;
//     }
//     if (to.name === 'Login') {
//       if (_.get(store.state, 'profile.profile.team.fullAccessOfLoopAction')) {
//         next({ name: 'LoopActionHome' });
//       } else {
//         next({ name: 'Dashboard' });
//       }
//       return;
//     }
//   }

//   next();
// });

export default router;