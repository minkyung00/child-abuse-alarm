<template>
  <b-row>
    <UserHomeNav class="col-3"></UserHomeNav>
    <router-view class="col-9 p-5"/>
  </b-row>
</template>

<script>
import UserHomeNav from "@/components/Nav/UserHomeNav.vue"

export default {
  name: "UserHome",
  components: {
    UserHomeNav
  }
}
</script>

<style lang="scss" scoped>
.row {
  --bs-gutter-x: 0;
}

.col-9 {
  background-color: #f9fafb;
  @media (max-width: $break-large) {
    width: 100%;
  }
}
</style>
