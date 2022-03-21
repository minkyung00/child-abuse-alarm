import { users } from './index'

function logoutUser (data) {
  return users.post('logout/', data)
}

function refreshAccessToken (data) {
  return users.post('login/refresh/', data)
}

export {
  logoutUser,
  refreshAccessToken
};
