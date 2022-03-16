<template>
  <b-container class="register">

    <header class="register-header">
      <h1 class="register-logo">🌱</h1>
      <h1 class="register-title">회원가입</h1>
    </header>

    <form id="register-form">
      <b-form-input id="register-id-input"
                  type="text"
                  placeholder="아이디"
                  required/>
      <b-form-input id="register-name-input"
                  type="text"
                  placeholder="이름"
                  required/>
      <b-form-input id="register-email-input"
                  type="email"
                  placeholder="이메일"
                  required/>
      <b-form-input id="register-password-input"
                  type="password"
                  placeholder="비밀번호"
                  required/>
      <b-form-input id="register-password-again-input"
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
export default {
  name: "Register",
}
</script>

<style lang="css" scoped>
.register {
  max-width: 600px;
}

header {
  text-align: center;
  padding: 3rem 0rem;
}

input {
  padding: 0.75rem 1.5rem;
  margin-bottom: 20px;
  border-radius: 30px;
}

.register-form-btn {
  width: 100%;
  padding: 0.75rem;
  margin: 10px 0px;
  border-radius: 30px;
}

</style>