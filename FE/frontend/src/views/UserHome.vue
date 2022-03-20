<template>
  <b-row>
    <UserHomeNav class="col-3"></UserHomeNav>
    <router-view class="col-9 py-5"/>
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
