import http from "../http-common";

class TreeDataService {

    getTree(node){
        return http.get(`/tree/${node}`);
           
    }
    getHTMLTree(){
        return http.get('/ssr')
    }

    getChildren(name) {
      return http.get(`/taxons/${name}`)
    }

}

export default new TreeDataService();
