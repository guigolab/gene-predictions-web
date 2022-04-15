import http from "../utils/http-axios"

const base = http.base

class DataPortalService {

    getOrganisms(params) {
        return base.get("/organisms", {
        params: params
        })
    }
    getFilteredOrganisms(params){
        return base.get("/organisms/search", {
        params: params
        })
    }
    getOrganism(name) {
        return base.get(`/organisms/${name}`)
    }
    getTree(node){
        return base.get(`/tree/${node}`);    
    }
    getTaxonChildren(name) {
        return base.get(`/taxons/${name}`)
    }
    // getData(model, params){
    //     return base.get('/files', {
    //         params:params
    //     })
    // }
    getFiles(model,params){
        return base.get(`files/${model}`, {
            params:params
        })
    }
}

export default new DataPortalService();


  