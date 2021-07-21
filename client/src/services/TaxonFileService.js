import http from "../http-common";
import download from "../http-download"

class TaxonFileDataService {
  getAll(taxId) {
    return http.get(`/files/${taxId}`);
  }

  download(name) {
    return download.post(`/file/${name}`);
  }

  getTracks(name) {
    return http.get(`/file/${name}`)
  }
}

export default new TaxonFileDataService();
