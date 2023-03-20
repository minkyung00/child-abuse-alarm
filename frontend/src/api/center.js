import { instance } from './index'

function getCenterList (keyword) {
  const params = {}
  if (keyword) {
    params.keyword = keyword
  }
  return instance.get('/api/center/', {
    params: params
  })
}

function applyCenterCode (centerID, data) {
  return instance.post(`/api/center/${centerID}/code/`, data)
}

export {
  getCenterList,
  applyCenterCode
};
