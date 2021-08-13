import http from "../http-common";

class TaxonNodeDataService {
  getAll() {
    return http.get("/taxon-nodes");
  }
}

export default new TaxonNodeDataService();
