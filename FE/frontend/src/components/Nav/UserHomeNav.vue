<template>
  <b-navbar toggleable>
    <div class="userhome-nav">

      <!-- <b-navbar-brand
        class="userhome-logo"
        @click="handleRoute('HomeView')"
      >🌱</b-navbar-brand> -->

      <div class="userhome-profile">
        <h3 class="center-name">{{ centerName }}</h3>
        <span class="username">
          {{ `${username}님, 안녕하세요` }} 
        </span>
        <button class="logout-button" @click="logout">
          로그아웃
        </button>
      </div>

      <div class="userhome-calendar">
        <b-icon icon="chevron-left" />
        <div class="date">
          <p class="month">5월</p>
          <p class="day">21일</p>
          <p class="dayweek">토요일</p>
        </div>
        <b-icon icon="chevron-right" />
      </div>

      <NavbarItem class="desktop-navbar" />
    </div>

    <!-- <b-collapse
      id="nav-collapse"
      is-nav>
      <NavbarItem class="mobile-navbar" />
    </b-collapse> -->

  </b-navbar>
</template>

<script>
import NavbarItem from '@/components/Nav/NavbarItem'

export default {
  name: "UserHomeNav",
  components: {
    NavbarItem
  },
  data () {
    return {
      username: this.$store.state.userid,
      centerName: '천호어린이집'
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
.navbar {
  // flex-direction: column;
  padding: 2rem 1.5rem;
  width: 100%;
  // max-width: 250px;
  // height: 100vh;
  justify-content: space-between;
  background-color: $color-nav-green;
  // @media (max-width: $break-large) {
  //   height: 100%;
  //   flex-direction: row;
  //   width: 100%;
  //   max-width: 100vw;
  //   justify-content: space-around;
  // }

  .userhome-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    // @media (max-width: $break-large) {
    //   display: flex;
    //   width: 100%;
    //   justify-content: space-between;
    //   align-items: center;
    // }
    @media (max-width: $break-medium) {
      display: block;
    }
  }

  .userhome-logo {
    // font-size: calc(1.375rem + 1.5vw);
    font-size: 36px;
    padding: 1rem 0rem;
    text-align: center;
  }

  .userhome-profile {
    // display: flex;
    align-items: center;
    color: white;
    @media (max-width: $break-large) {
      justify-content: space-between;
    }

    .center-name {
      font-weight: $font-weight-extrabold;
    }

    .username {
      display: block;
      font-size: 18px;
      font-weight: $font-weight-bold;
    }

    .logout-button {
      // float: right;
      padding: 4px 12px;
      font-size: 14px;
      color: white;
      border: 1px solid white;
      background-color: transparent;
      // margin-right: 10px;

      &:hover {
        background-color: #F7F8F9;
        color: $color-nav-green;
      }
    }
  }

  .userhome-calendar {
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;

    .b-icon {
      width: 2rem;
      height: 2rem;
    }

    .date {
      margin: 0 40px;
      text-align: center;
    }

    .month {
      margin: 0;
      font-size: 32px;
      font-weight: $font-weight-bold;
    }

    .day {
      margin: 0;
      font-size: 60px;
      font-weight: $font-weight-extrabold;
    }

    .dayweek {
      font-size: 24px;
      font-weight: $font-weight-semibold;
    }
  }
}
</style>
