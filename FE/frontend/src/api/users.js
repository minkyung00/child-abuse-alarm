import { instance } from './index'

function logoutUser (data) {
  return instance.post('/api/users/logout/', data)
}

function refreshAccessToken (data) {
  return instance.post('/api/users/login/refresh/', data)
}

function getUserInfo (username) {
  return instance.get(`/api/users/${username}/`)
}

export {
  logoutUser,
  refreshAccessToken,
  getUserInfo
};
