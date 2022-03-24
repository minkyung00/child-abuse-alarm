<template>
  <b-nav pills>
    <div>
      <h1 class="userhome-logo" @click="handleRoute('HomeView')">🌱</h1>
      <div>
        <b-avatar variant="light" badge badge-left size="60px"></b-avatar>
        <span class="username">{{ `${username}님` }}</span>
        <button class="logout-button" @click="logout">
          <b-icon icon="power" aria-hidden="true"></b-icon> 로그아웃
        </button>
      </div>

      <b-nav-item active @click="handleRoute('DashBoard')">
        <b-icon icon="display"></b-icon>
        <span class="nav-link-text">대시보드</span>
      </b-nav-item>
      <b-nav-item>
        <b-icon icon="bar-chart-fill"></b-icon>
        <span class="nav-link-text">분석 시스템</span>
      </b-nav-item>
      <b-nav-item>
        <b-icon icon="patch-exclamation-fill"></b-icon>
        <span class="nav-link-text">아동학대 신고</span>
      </b-nav-item>
    </div>
    <button class="logout-button" @click="logout">
      <b-icon icon="power" aria-hidden="true"></b-icon> 로그아웃
    </button>
  </b-nav>
</template>

<script>
export default {
  name: "UserHomeNav",
  data () {
    return {
      username: this.$store.state.userid
    }
  },
  methods: {
    handleRoute (route) {
      this.$router.push({
        name: route
      })
    },
    async logout () {
      try {
        this.$store.dispatch('Logout')
        this.$router.push({
          name: 'HomeView'
        })
      } catch (err) {
        console.log(err)
      }
    },
  }
}
</script>

<style lang="scss" scoped>
.nav {
  flex-direction: column;
  padding: 1rem 1.5rem;
  max-width: 250px;
  height: 100vh;
  justify-content: space-between;
  // background-color: #f9fafb;
  @media (max-width: 920px) {
    flex-direction: row;
    width: 100%;
    max-width: 100vw;
  }

  .userhome-logo {
    padding: 1rem 0rem;
    text-align: center;
  }

  .username {
    font-weight: 700;
  }
  
  .nav-item {
    margin: 10px 5px;

    .nav-link {
      padding: 1rem 1.25rem;
      border-radius: 30px !important;
      color: $primary-color;
      font-size: 16px;
      font-weight: 400;

      &:hover,
      &:focus {
        background-color: $primary-color;
        color: white;
        font-weight: bold;
      }
    }

    .nav-link.active {
      background-color: $primary-color !important;
      color: white;
      font-weight: bold;
    }

    .nav-link-text {
      margin-left: 20px;
    }
  }

  .logout-button {
    color: #4e5968;
    background-color: transparent;

    &:hover {
      background: #F7F8F9;
    }
  }
}
</style>
