import http from "../http-common";

class TaxonNodeDataService {
  getAll() {
    return http.get("/taxon-nodes");
  }

  getChildren(tax_id) {
    return http.get(`/taxon-nodes/${tax_id}`);
  }

  // get(id) {
  //   return http.get(`/taxon-nodes/${id}`);
  // }

  create(data) {
    return http.post("/taxon-nodes", data);
  }

  update(id, data) {
    return http.put(`/taxon-nodes/${id}`, data);
  }

  delete(id) {
    return http.delete(`/taxon-nodes/${id}`);
  }

  deleteAll() {
    return http.delete(`/taxon-nodes`);
  }

}

export default new TaxonNodeDataService();
