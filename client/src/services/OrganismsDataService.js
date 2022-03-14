import http from "../http-common";

class OrganismsDataService {
  getOrganisms(params) {
      return http.get("/root_organisms", {
        params: params
      })
    }
  getFilteredOrganisms(params){
    return http.get("/root_organisms/search", {
      params: params
    })
  }
  getOrganism(name) {
    return http.get(`/root_organisms/${name}`)
  }
  deleteAll(){
    return http.delete('/input')
  }
}

export default new OrganismsDataService();
