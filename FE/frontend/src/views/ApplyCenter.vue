<template>
  <b-container class="apply">
    <header id="apply-header">
      <h1 class="apply-logo">🌱</h1>
      <h1 class="apply-title">어린이집 등록</h1>
      <p class="apply-desc">최초 등록된 어린이집으로만 이용 가능합니다.</p>
    </header>
    
    <b-form-input type="text"
                  placeholder="어린이집명을 입력해주세요." />
  </b-container>
</template>

<script>
export default {
  name: "ApplyCenter"
}
</script>

<style lang="scss" scoped>
.apply {
  max-width: 800px;
}

#apply-header {
  text-align: center;
  padding: 3rem 0rem;

  .apply-desc {
    color: $primary-color;
    font-weight: bold;
  }
}

input {
  padding: 0.75rem 1.5rem;
  margin-bottom: 20px;
  border-radius: 30px;
  border: 2.5px solid $primary-color;

  &:focus {
    border-color: $primary-color;
    outline: 0;
    box-shadow: 0 0 0 0.25rem #33d27b52;
  }
}

</style>
