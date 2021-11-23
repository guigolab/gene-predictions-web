import http from "../http-common";
import download from "../http-download"

class TaxonFileDataService {
  getAll(params) {
    return http.get('/files' , {
      params: params
    })
  }

  download(name) {
    return download.get(`/files/${name}`);
  }

  // getTracks(name) {
  //   return http.get(`/file/${name}`)
  // }
}

export default new TaxonFileDataService();
