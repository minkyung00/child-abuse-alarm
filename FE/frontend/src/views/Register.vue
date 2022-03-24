<template>
  <b-container class="register">

    <header id="register-header">
      <h1 class="register-logo">🌱</h1>
      <h1 class="register-title">회원가입</h1>
    </header>

    <form id="register-form" @submit.prevent="submitForm">
      <b-form-input id="register-id-input"
                    v-model="userid"
                    type="text"
                    placeholder="아이디"
                    required/>
      <b-form-input id="register-name-input"
                    v-model="username"
                    type="text"
                    placeholder="이름"
                    required/>
      <b-form-input id="register-email-input"
                    v-model="email"
                    type="email"
                    placeholder="이메일"
                    required/>
      <b-form-input id="register-password-input"
                    v-model="password"
                    type="password"
                    placeholder="비밀번호"
                    required/>
      <b-form-input id="register-password-again-input"
                    v-model="passwordAgain"
                    type="password"
                    placeholder="비밀번호 확인"
                    required/>
      <button class="register-form-btn"
              type="submit"
      >가입하기</button>
    </form>
  </b-container>
</template>

<script>
import { registerUser } from '@/api/auth';

export default {
  name: "Register",
  data () {
    return {
      userid: '',
      username: '',
      email: '',
      password: '',
      passwordAgain: ''
    }
  },
  methods: {
    async submitForm () {
      try {
        const data = {
          username: this.userid,
          name: this.username,
          email: this.email,
          password: this.password,
          password2: this.passwordAgain
        }

        await registerUser(data)

        alert('회원가입이 완료되었습니다!')
        this.$router.push({
          name: 'ApplyCenter'
        })
      } catch (err) {
        console.log(err)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.register {
  max-width: 600px;


  #register-header {
    text-align: center;
    padding: 3rem 0rem;
  }


  #register-form {
    input {
      padding: 0.75rem 1.5rem;
      margin-bottom: 20px;
      border-radius: 30px;

      &:focus {
        border-color: $primary-color;
        outline: 0;
        box-shadow: 0 0 0 0.25rem #33d27b52;
        color: $primary-color;
      }
    }

    .register-form-btn {
      width: 100%;
      padding: 0.75rem;
      margin: 10px 0px;
      border-radius: 30px;
    }
  }
}

</style>