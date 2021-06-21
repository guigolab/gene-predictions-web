import http from "../http-common";

class SpeciesDataService {
  getAll() {
    return http.get("/species");
  }

  get(id) {
    return http.get(`/species/${id}`);
  }

  create(data) {
    return http.post("/species", data);
  }

  update(id, data) {
    return http.put(`/species/${id}`, data);
  }

  delete(id) {
    return http.delete(`/species/${id}`);
  }

  deleteAll() {
    return http.delete(`/species`);
  }

}

export default new SpeciesDataService();
