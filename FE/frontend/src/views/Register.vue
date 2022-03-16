<template>
  <b-container>
    <header>
      <h1>🌱</h1>
      <h1>회원가입</h1>
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

</style>