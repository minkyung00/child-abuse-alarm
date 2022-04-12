<template>
  <b-navbar toggleable>
    <div class="userhome-nav">

      <b-navbar-brand
        class="userhome-logo"
        @click="handleRoute('HomeView')"
      >🌱</b-navbar-brand>

      <div class="userhome-profile">
        <b-avatar
          variant="light"
          badge
          badge-left
          size="50px"
        />
        <span class="username">
          {{ `${username}님` }}
        </span>
        <button class="logout-button" @click="logout">
          <b-icon
            icon="power"
            aria-hidden="true"
          /> 로그아웃
        </button>
      </div>

      <NavbarItem class="desktop-navbar" />

      <!--Toggler-->
      <b-navbar-toggle
        target="nav-collapse"
      >
        <template #default="{ expanded }">
          <b-icon
            v-if="expanded"
            icon="chevron-bar-up"
          />
          <b-icon
            v-else
            icon="chevron-bar-down"
          />
        </template>
      </b-navbar-toggle>
    </div>

    <b-collapse
      id="nav-collapse"
      is-nav>
      <NavbarItem class="mobile-navbar" />
    </b-collapse>

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
.navbar {
  flex-direction: column;
  padding: 1rem 1.5rem;
  max-width: 250px;
  height: 100vh;
  justify-content: space-between;
  // background-color: #f9fafb;
  @media (max-width: $break-large) {
    height: 100%;
    flex-direction: row;
    width: 100%;
    max-width: 100vw;
    justify-content: space-around;
  }

  .userhome-nav {
    @media (max-width: $break-large) {
      display: flex;
      width: 100%;
      justify-content: space-between;
      align-items: center;
    }
  }

  .userhome-logo {
    font-size: calc(1.375rem + 1.5vw);
    padding: 1rem 0rem;
    text-align: center;
  }

  .userhome-profile {
    display: flex;
    align-items: center;
    @media (max-width: $break-large) {
      width: 100%;
      justify-content: space-between;
    }

    .b-avatar {
      @media (max-width: $break-large) {
        display: none;
      }
    }

    .username {
      font-weight: 700;
      width: 60px;
      display: block;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      @media (max-width: $break-large) {
        width: 60%;
      }
    }

    .logout-button {
      padding: 0;
      color: #4e5968;
      background-color: transparent;
      margin-right: 10px;

      &:hover {
        background: #F7F8F9;
      }
    }
  }

  .navbar-toggler {
    display: none;
  }

  @media (max-width: $break-large) {
    .navbar-toggler {
      display: block;
    }
    .desktop-navbar {
      display: none;
    }
  }
}
</style>
