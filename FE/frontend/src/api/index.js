import axios from 'axios';
import { setInterceptors } from './common/interceptors';

function createAxiosService () {
  return axios.create({
    proxy: {
      target: process.env.VUE_APP_API_URL,
      changeOrigin: true
    }
  });
}

function createAxiosServiceWithAuth(url) {
    const axiosService = axios.create({
      proxy: {
        target: `${process.env.VUE_APP_API_URL}/api/${url}/`,
        changeOrigin: true
      }
    });
    
  return setInterceptors(axiosService);
}

export const axiosService = createAxiosService();
export const users = createAxiosServiceWithAuth('users');
