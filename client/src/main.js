import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import App from './App.vue'
import router from './utils/router'
import store from './store'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { VuePlugin } from 'vuera'

Vue.config.productionTip = false
Vue.use(VuePlugin)

// Make BootstrapVue available throughout the project
Vue.use(BootstrapVue)
// BootstrapVue icon components plugin
Vue.use(IconsPlugin)

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
