import http from "../http-common";
import httpForm from "../http-formdata"
import download from "../http-download"


class GeneDataService {

    getParams(geneId){
        if(geneId){
            return download.get(`/geneid/${geneId}`);
        }
        else{
            return http.get('/geneid')
        }
    }

    sendForm(form) {
        return httpForm.post('/geneid',form)
    }
    delete(geneId) {
        return http.delete(`/geneid/${geneId}`);
      }
  
}

export default new GeneDataService();
