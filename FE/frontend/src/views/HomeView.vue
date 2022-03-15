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
        <form id="login-form">
          <b-form-input id="login-id-input"
                        type="text"
                        placeholder="아이디"
                        required/>
          <b-form-input id="login-password-input"
                        type="password"
                        placeholder="비밀번호"
                        required/>
          <button class="login-form-btn"
                  type="submit"
          >로그인</button>
        </form>

        <div class="login-info-user">
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
};
</script>

<style lang="css" scoped>

@media (max-width: 767.98px) {
  .col {
    flex: 100%;
  }

  .wrap-banner {
    height: 100%;
  }
}

.wrap-banner {
  height: 100vh;
  background: #81E571;
  color: white;
}

.banner {
  max-width: 500px;
  padding: 10rem 3rem;
  margin-right: auto;
  margin-left: auto;
}

.wrap-form {
  display: flex;
}

.login {
  min-width: 400px;
  margin: auto;
}

input {
  padding: 0.75rem 1.5rem;
  margin-bottom: 10px;
  border-radius: 30px;
}

.login-form-btn {
  width: 100%;
  padding: 0.75rem;
  margin: 10px 0px;
  border-radius: 30px;
}

.login-info-user {
  display: flex;
}

.link-register {
  margin-left: 10px;
  color: #81E571;
}
</style>
