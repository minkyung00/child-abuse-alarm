import { instance } from './index'

function logoutUser (data) {
  return instance.post('/api/users/logout/', data)
}

function refreshAccessToken (data) {
  return instance.post('/api/users/login/refresh/', data)
}

export {
  logoutUser,
  refreshAccessToken
};
