import http from "../http-common";

class NewickDataService {
  getAll() {
    return http.get("/newick");
  }

  get(id) {
    return http.get(`/newick/${id}`);
  }

  create(data) {
    return http.post("/newick", data);
  }

  update(id, data) {
    return http.put(`/newick/${id}`, data);
  }

  delete(id) {
    return http.delete(`/newick/${id}`);
  }

  deleteAll() {
    return http.delete(`/newick`);
  }

}

export default new NewickDataService();
