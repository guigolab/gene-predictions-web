import geneidService from '../../services/GeneIdService'

const getDefaultState = () => {
    return {
        jpg: null,
        ps: null,
        run_time: '',
        ouput_file: null,
        ouput: '',
        geneid_cmd: '',
        param_species: ''
    }
}
const state = getDefaultState()

const mutations= {
    setResult(state, id){
        geneidService.getResult(id).then(response => {
            Object.assign(state, response.data)
            return response.data
        })
    },
    setJpg(state, file){
        state.jpg = file
    },
    updateForm(state, payload){
        state.sampleForm[payload.label] = payload.value
    },
    resetForm(state){
        Object.assign(state, getDefaultState())
    },
}
const actions= {
    reset(context){
        context.commit('resetForm')
    }
}
const getters = {
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}