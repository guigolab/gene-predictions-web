import http from "../http-common";
import httpForm from "../http-formdata"
import download from "../http-download"


class GeneDataService {

    downloadFile(id){
        return download.get(`/results/${id}`);
    }
    getResult(id){
        return http.get(`/geneid/${id}`)
    }
    sendForm(form) {
        return httpForm.post('/geneid',form)
    }
    delete(geneId) {
        return http.delete(`/geneid/${geneId}`);
    }
  
}

export default new GeneDataService();
