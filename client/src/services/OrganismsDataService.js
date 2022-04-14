import http from "../http-common";

class OrganismsDataService {
  getOrganisms(params) {
      return http.get("/organisms", {
        params: params
      })
    }
  getFilteredOrganisms(params){
    return http.get("/organisms/search", {
      params: params
    })
  }
  getOrganism(name) {
    return http.get(`/organisms/${name}`)
  }
  deleteAll(){
    return http.delete('/input')
  }
}

export default new OrganismsDataService();
