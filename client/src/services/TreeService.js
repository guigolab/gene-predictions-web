import http from "../http-common";

class TreeDataService {

    getTree(node){
        return http.get(`/tree/${node}`);
           
    }
  
}

export default new TreeDataService();
