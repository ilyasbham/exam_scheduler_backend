import axios from "axios";

const API_URL = "http://127.0.0.1:8000/research-assistants/";

class ResearchAssistantService {
  getAll() {
    return axios.get(API_URL);
  }

  create(assistant) {
    return axios.post(API_URL, assistant);
  }

  get(id) {
    return axios.get(`${API_URL}${id}/`);
  }

  update(id, assistant) {
    return axios.put(`${API_URL}${id}/`, assistant);
  }

  delete(id) {
    return axios.delete(`${API_URL}${id}/`);
  }
}

export default new ResearchAssistantService();
