import store from '@/store'
import axios from 'axios'

export function setInterceptors (instance) {
  instance.interceptors.request.use(function (config) {
    config.headers['Content-Type'] = 'application/json'
    config.headers.Authorization = store.state.accessToken ? `Bearer ${store.state.accessToken}` : store.state.accessToken
    config.headers.get['Cache-Control'] = 'no-cache'
    return config
  },
  function (error) {
    return Promise.reject(error)
  })

  instance.interceptors.response.use(function (response) {
    return response
  },
  async function (error) {
    try {
      const errorAPI = error.response.config
      if (error.response.status === 401 && errorAPI.retry === undefined && store.state.refreshToken !== '') {
        errorAPI.retry = true
        await store.dispatch('refreshAccessToken')
        return await axios(errorAPI)
      }
    } catch (err) {
      console.log('axios.interceptors.response error: ', err)
    }
    return Promise.reject(error)
  })
  return instance
}
