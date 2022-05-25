import Vue from "vue";
import VueRouter from "vue-router";

import HomeView from "@/views/HomeView.vue";
import Register from "@/views/Register.vue"

import ApplyCenter from "@/views/ApplyCenter.vue"

import UserHome from "@/views/UserHome.vue"
import DashBoard from "@/views/DashBoard.vue"
import VideoView from "@/views/VideoView.vue"
import Weekly from "@/views/Weekly.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "HomeView",
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
  },
  {
    path: "/user-home",
    name: "UserHome",
    component: UserHome,
    children: [
      {
        path: "dashboard",
        name: "DashBoard",
        component: DashBoard,
      },
      {
        path: "video",
        name: "VideoView",
        component: VideoView,
      },
      {
        path: "weekly",
        name: "Weekly",
        component: Weekly
      }
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
