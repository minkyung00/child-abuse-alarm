<template>
  <b-row>
    <UserHomeNav class="col-3"></UserHomeNav>
    <router-view class="col-9 p-5"/>
  </b-row>
</template>

<script>
import UserHomeNav from "@/components/UserHomeNav.vue"

export default {
  name: "UserHome",
  components: {
    UserHomeNav
  }
}
</script>

<style lang="scss" scoped>
.col-9 {
  background-color: #f9fafb;
  @media (max-width: 920px) {
    width: 100%;
  }
}
</style>
