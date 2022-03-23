import Vue from "vue";
import Vuex from "vuex";

import { loginUser } from '@/api/auth';
import { refreshAccessToken, logoutUser } from '@/api/users';

import {
  getAccessFromCookie,
  getRefreshFromCookie,
  getUserFromCookie,
  saveAccessToCookie,
  saveRefreshToCookie,
  saveUserToCookie,
  deleteCookie
} from '@/utils/cookies'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userid: getUserFromCookie() || '',
    accessToken: getAccessFromCookie() || '',
    refreshToken: getRefreshFromCookie() || ''
  },
  getters: {
    isLogin (state) {
      return !!state.accessToken && !!state.refreshToken
    }
  },
  mutations: {
    setUserid (state, userid) {
      state.userid = userid
    },
    clearUserid (state) {
      state.userid = ''
    },
    setAccessToken (state, accessToken) {
      state.accessToken = accessToken
    },
    setRefreshToken (state, refreshToken) {
      state.refreshToken = refreshToken
    },
    clearToken (state) {
      state.accessToken = ''
      state.refreshToken = ''
    }
  },
  actions: {
    async Login ({ commit, dispatch }, data) {
      try {
        const res = await loginUser (data)

        commit('setAccessToken', res.data.access)
        commit('setRefreshToken', res.data.refresh)
        commit('setUserid', data.username)

        saveAccessToCookie(res.data.access)
        saveRefreshToCookie(res.data.refresh)
        saveUserToCookie(data.username)
      } catch (error) {
        return error.response.status
      }
    },
    async Logout ({ state, commit }) {
      try {
        await logoutUser({
          refresh: state.refreshToken
        })
        commit('clearUserid')
        commit('clearToken')
        commit('clearUserInfo')

        deleteCookie('til_user')
        deleteCookie('til_access')
        deleteCookie('til_refresh')
      } catch (err) {
        console.log('Logout error: ', err)
      }
    },
    async refreshAccessToken ({ commit }) {
      try {
        const res = await refreshAccessToken({
          refresh: this.state.refreshToken
        })
        commit('setAccessToken', res.data.access)
        saveAccessToCookie(res.data.access)
      } catch (err) {
        console.log('refreshAccessToken error: ', err)
      }
    }
  },
  modules: {},
});
