import Vue from 'vue';
import Router from 'vue-router';
import App from '../App.vue';
import Login from '../pages/login.vue';
import Main from '../pages/main.vue';
import ThreeScene from '../pages/character.vue';
Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/character',
      name: 'Character',
      component: ThreeScene
    }
  ]
});

router.beforeEach((to, from, next) => {
  const loggedIn = !!localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
    next('/login');
  } else {
    next();
  }
});

export default router;
