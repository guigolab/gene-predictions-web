import http from "../http-common";

class TaxonNodeDataService {
  getAll() {
    return http.get("/taxon-nodes");
  }

  getTree(to_tree) {
    return http.get(`/taxon-nodes/${to_tree}`);
  }

  getChildren(tax_id) {
    return http.get(`/taxon-node/${tax_id}`);
  }

}

export default new TaxonNodeDataService();
