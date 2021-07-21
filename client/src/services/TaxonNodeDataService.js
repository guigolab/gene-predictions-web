import http from "../http-common";

class TaxonNodeDataService {
  getAll() {
    return http.get("/taxon-nodes");
  }

  getChildren(tax_id) {
    return http.get(`/taxon-nodes/${tax_id}`);
  }

}

export default new TaxonNodeDataService();
