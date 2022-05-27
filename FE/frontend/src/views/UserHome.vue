<template>
  <b-row>
    <UserHomeNav></UserHomeNav>
    <router-view />
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
  justify-content: center;
}

.col-9 {
  background-color: #f9fafb;
  @media (max-width: $break-large) {
    width: 100%;
  }
}
</style>
