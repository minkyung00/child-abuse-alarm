<template>
  <b-container class="register">

    <header id="register-header">
      <h1 class="register-logo">🌱</h1>
      <h1 class="register-title">회원가입</h1>
    </header>

    <form id="register-form" @submit.prevent="submitForm">
      <b-form-group id="input-group-id">
        <label for="input-id">아이디</label>
        <b-form-input
          id="input-id"
          v-model="userid"
          type="text"
          placeholder="아이디"
          required />
      </b-form-group>

      <b-form-group id="input-group-username">
        <label for="input-username">이름</label>
        <b-form-input 
          id="input-username"
          v-model="username"
          type="text"
          placeholder="이름"
          required />
      </b-form-group>

      <b-form-group id="input-group-email">
        <label for="input-email">이메일</label>
        <b-form-input
          id="input-email"
          v-model="email"
          type="email"
          placeholder="이메일"
          required />
      </b-form-group>

      <b-form-group id="input-group-password">
        <label for="input-password">비밀번호</label>
        <b-form-input
          id="input-password"
          v-model="password"
          type="password"
          placeholder="비밀번호"
          required />
      </b-form-group>

      <b-form-group id="input-group-password-again">
        <label for="input-password-again">비밀번호 확인</label>
        <b-form-input
          id="input-password-again"
          v-model="passwordAgain"
          type="password"
          placeholder="비밀번호 확인"
          required />
      </b-form-group>

      <button
        class="register-form-btn"
        type="submit"
      >가입하기</button>
    </form>

    <p class="info-login">
      이미 아이디가 있으신가요?
      <a class="link-login"
          href="/"
      >로그인</a>
    </p>
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
    padding: 2.5rem 0rem;
  }


  #register-form {
    margin-bottom: 20px;
  
    .form-group {
      margin-bottom: 10px;
    }

    label {
      font-size: 16px;
      font-weight: bold;
      margin: 0px 0px 8px 10px;
    }
    
    input {
      padding: 0.75rem 1.5rem;
      margin-bottom: 15px;
      border-radius: 30px;

      &:focus {
        border-color: $primary-color;
        outline: 0;
        box-shadow: 0 0 0 0.25rem #33d27b52;
        color: $primary-color;
      }
    }
  }
}

</style>