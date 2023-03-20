import { axiosService } from './index'

function registerUser (data) {
  return axiosService.post('/api/users/', data)
}
  
function loginUser (data) {
  return axiosService.post('/api/users/login/', data)
}

export {
  registerUser,
  loginUser
};
