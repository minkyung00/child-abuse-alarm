<template>
  <b-row>
    <UserHomeNav></UserHomeNav>
    <router-view />
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

</style>
