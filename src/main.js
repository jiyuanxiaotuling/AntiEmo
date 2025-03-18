import Vue from 'vue'
import App from './App.vue'

import axios from 'axios'
import VueAxios from 'vue-axios'
import VueRouter from 'vue-router'
import VueClipBoard from 'vue-clipboard2'
import router from './router'
Vue.use(VueClipBoard)
//use：将第三方模块 注入到Vue实例对象中的方法
Vue.use(VueAxios, axios)
Vue.use(VueRouter)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
