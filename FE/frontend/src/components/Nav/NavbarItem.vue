<template>
<div class="userhome-navbar" id="navbarNav">
  <b-nav-item active @click="handleRoute('DashBoard')">
    <b-icon icon="bell-fill" />
    <!-- <span class="nav-link-text">대시보드</span> -->
  </b-nav-item>


  <b-nav-item @click="handleRoute('Weekly')">
    <b-icon icon="bar-chart-fill" />
    <!-- <span class="nav-link-text">아동학대 신고</span> -->
  </b-nav-item>
</div>
</template>

<script>
export default {
  name: 'NavbarItem',
  methods: {
    handleRoute (route) {
      this.$router.push({
        name: route
      }).catch(() => {});
    }
  }
}
</script>

<style lang="scss" scoped>
.userhome-navbar {
  display: flex;
  justify-content: center;
}

.nav-item {
  margin: 10px 5px;
  list-style: none;

  .nav-link {
    padding: 1rem 1.25rem;
    border-radius: 30px !important;
    // color: $primary-color;
    color: white;
    font-size: 16px;
    font-weight: 400;
    opacity: 0.7;

    &:hover,
    &:focus {
      background-color: $color-opacity-25;
      color: white;
      font-weight: bold;
      opacity: 1;
    }
  }

  .nav-link.active {
    background-color: $color-opacity-25;
    // background-color: $primary-color !important;
    color: white;
    font-weight: bold;
    opacity: 1;
  }

  .nav-link-text {
    margin-left: 20px;
  }
}
</style>