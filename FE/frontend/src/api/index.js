import axios from 'axios';
import { setInterceptors } from './common/interceptors';

function createAxiosService () {
  return axios.create({
    baseURL: process.env.VUE_APP_API_URL
  });
}

function createAxiosServiceWithAuth() {
  const axiosService = axios.create({
    proxy: {
      baseURL: process.env.VUE_APP_API_URL
    }
  });

  return setInterceptors(axiosService);
}

export const axiosService = createAxiosService();
export const instance = createAxiosServiceWithAuth();
