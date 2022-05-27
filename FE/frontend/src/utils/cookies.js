function saveAccessToCookie (value) {
  document.cookie = `til_access=${value}; path=/; max-age=1800`
}
  
function saveRefreshToCookie (value) {
  document.cookie = `til_refresh=${value}; path=/; max-age=86400`
}
  
function saveUserToCookie (value) {
  document.cookie = `til_user=${value}; path=/`
}

function saveCenterToCookie (value) {
  document.cookie = `til_center=${value}; path=/`
}
  
function getAccessFromCookie () {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)til_access\s*=\s*([^;]*).*$)|^.*$/,
    '$1'
  )
}
  
function getRefreshFromCookie () {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)til_refresh\s*=\s*([^;]*).*$)|^.*$/,
    '$1'
  )
}
  
function getUserFromCookie () {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)til_user\s*=\s*([^;]*).*$)|^.*$/,
    '$1'
  )
}

function getCenterFormCookie () {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)til_center\s*=\s*([^;]*).*$)|^.*$/,
    '$1'
  )
}
  
function deleteCookie (value) {
  document.cookie = `${value}=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT;`
}
  
export {
  saveAccessToCookie,
  saveRefreshToCookie,
  saveUserToCookie,
  saveCenterToCookie,
  getAccessFromCookie,
  getRefreshFromCookie,
  getUserFromCookie,
  getCenterFormCookie,
  deleteCookie
}
  