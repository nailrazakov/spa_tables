import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
});

export const fetchTableData = async (params = {}) => {
  const response = await apiClient.get('/spa_tables/', { params });
  console.log(response)
  return response;
};

export default apiClient;