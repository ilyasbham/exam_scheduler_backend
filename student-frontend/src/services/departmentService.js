import axios from "axios";

const API_URL = "http://127.0.0.1:8000/department/"; // change if needed

export const getDepartments = () => axios.get(`${API_URL}list/`);
export const addDepartment = (data) => axios.post(`${API_URL}add/`, data);
export const deleteDepartment = (id) => axios.delete(`${API_URL}delete/${id}/`);
