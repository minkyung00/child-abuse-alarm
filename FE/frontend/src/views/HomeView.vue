<template>
  <b-row class="home">

    <b-col class="wrap-banner">
      <div class="banner">
        <h1 class="banner-logo">🌱</h1>
        <h1 class="banner-title">서비스 이름</h1>
        <h5 class="banner-desc">서비스 소개</h5>
      </div>
    </b-col>

    <b-col class="wrap-form">
      <div class="login">
        <form id="login-form" @submit.prevent="submitForm">

          <b-form-input 
            id="login-id-input"
            v-model="userid"
            type="text"
            placeholder="아이디"
            required/>

          <b-form-input
            id="login-password-input"
            v-model="password"
            type="password"
            placeholder="비밀번호"
            required/>

          <button
            class="login-form-btn"
            type="submit"
          >로그인</button>

        </form>

        <div class="login-info">
          <p class="info-register"
          >아직 계정이 없으신가요?</p>
          <a class="link-register"
             href="/register"
          >회원가입하기</a>
        </div>

      </div>
    </b-col>
  </b-row>
</template>

<script>
export default {
  name: "HomeView",
  data () {
    return {
      userid: '',
      password: ''
    }
  },
  methods: {
    async submitForm () {
      try {
        const data = {
          username: this.userid,
          password: this.password
        }

        await this.$store.dispatch('Login', data)

        this.$router.push({
          name: 'UserHome'
        })
      } catch (err) {
        console.log(err)
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.row {
  --bs-gutter-x: 0rem
}

@media (max-width: 767.98px) {
  .col {
    flex: 100%;
  }
}

.wrap-banner {
  height: 100vh;
  background: $primary-color;
  color: white;
  @media (max-width: 767.98px) {
    height: 100%;
  }

  .banner {
    max-width: 500px;
    padding: 10rem 3rem;
    margin-right: auto;
    margin-left: auto;
    @media (max-width: 767.98px) {
      padding: 5rem 3rem;
    }
  }
}


.wrap-form {
  display: flex;
  padding: 1.5rem;

  .login {
    min-width: 400px;
    margin: auto;
    @media (max-width: $break-small) {
      min-width: 300px;
    }

    input {
      padding: 0.75rem 1.5rem;
      margin-bottom: 10px;
      border-radius: 30px;

      &:focus {
        border-color: $primary-color;
        outline: 0;
        box-shadow: 0 0 0 0.25rem #33d27b52;
        color: $primary-color;
      }
    }

    #login-form {
      padding: 1rem;
      @media (max-width: $break-small) {
        padding: 0;
      }
    }

    .login-form-btn {
      width: 100%;
      padding: 0.75rem;
      margin: 10px 0px;
      border-radius: 30px;
    }

    .login-info {
      display: flex;
      padding: 0rem 1rem;
    }

    .link-register {
      margin-left: 10px;
      color: $primary-color;
    }
  }
}
</style>
