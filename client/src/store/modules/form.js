import {demoForm} from '../../static-config'
import portalService from '../../services/DataPortalService'

const state = () => ({
    geneidForm:{
        fastaText: '',
        // fastaFile: null, don't store files, reset on page refresh
        gffText: '',
        // gffFile: null,
        param: '',
        strands: '',
        mode: 'normal',
        exons: [],
        signals: [],
        output: '-G',
        gff2ps: true
    },
    params: []
})
const mutations= {
    updateForm(state, payload){
        console.log(payload)
        console.log(payload.value)
        state.geneidForm[payload.label] = payload.value
    },
    getParams(state){
        portalService.getFiles('parameters')
        .then(response => {
            state.params = response.data
        })
    },
    loadDemoForm(state){
        Object.assign(state.geneidForm, demoForm)
    }
}
const actions = {
    getParams(context){
        context.commit('getParams')
    },
    loadDemo(context){
        context.commit('loadDemoForm')
    }
}
const getters = {
    params(state){
        return state.params
    },
    getFastaFile(state){
        return state.geneidForm.fastaFile
    },
    getForm(state){
        return state.geneidForm
    }
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
