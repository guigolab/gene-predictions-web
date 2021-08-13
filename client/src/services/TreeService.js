import http from "../http-common";

class TreeDataService {

    getTree(node){
        if (node) {
            return http.get(`/tree/${node}`);
        }
        else {
            return http.get('/tree');
        }
           
    }
  
}

export default new TreeDataService();
