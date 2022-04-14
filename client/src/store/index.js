import Vue from 'vue'
import Vuex from 'vuex'
import form from './modules/form'
import jbrowse from './modules/jbrowse'
import result from './modules/result'
import portal from './modules/portal'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
    plugins: [createPersistedState()],
    modules: {
      form,
      result,
      portal,
      jbrowse
    }
})