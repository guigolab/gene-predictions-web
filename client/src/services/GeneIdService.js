import http from "../http-common";
import httpForm from "../http-formdata"

class GeneDataService {

    getParams(){
        return http.get('/geneid');   
    }

    sendForm(form) {
        return httpForm.post('/geneid',form)
    }
  
}

export default new GeneDataService();
