import Vue from "vue";
import VueRouter from "vue-router";

import HomeView from "@/views/HomeView.vue";
import Register from "@/views/Register.vue"

import ApplyCenter from "@/views/ApplyCenter.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/apply-center",
    name: "ApplyCenter",
    component: ApplyCenter
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
