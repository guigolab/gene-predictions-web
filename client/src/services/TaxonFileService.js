import http from "../http-common";
import download from "../http-download"

class TaxonFileDataService {
  getAll(taxId) {
    return http.get(`/files/${taxId}`);
  }

  download(name) {
    return download.post(`/download/${name}`);
  }

//   create(data) {
//     return http.post("/taxon-nodes", data);
//   }

//   update(id, data) {
//     return http.put(`/taxon-nodes/${id}`, data);
//   }

//   delete(id) {
//     return http.delete(`/taxon-nodes/${id}`);
//   }

//   deleteAll() {
//     return http.delete(`/taxon-nodes`);
//   }

}

export default new TaxonFileDataService();
