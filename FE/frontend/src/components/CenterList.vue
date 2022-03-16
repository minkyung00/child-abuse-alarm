<template>
  <b-container>
    <b-card title="꿈동산 어린이집">
      <b-card-text>
        서울특별시 강동구 상암로63길 39
      </b-card-text>
      <button>등록</button>
    </b-card>

    <b-card title="동산 어린이집">
      <b-card-text>
        서울특별시 강동구 상암로63길 39
      </b-card-text>
      <button>등록</button>
    </b-card>
  </b-container>
</template>

<script>
export default {
  name: 'CenterList'
}
</script>

<style lang="scss" scoped>
.card-body {
  display: flex;
  align-items: center;
  justify-content: space-between;

  .card-title,
  .card-text {
    margin: 0;
  }

  button {
    width: 5rem;
  }
}
</style>
