import axios from "axios";

export default axios.create({
  baseURL: "/api",
  headers: {
  },
  'Content-Type': 'multipart/form-data'
});
