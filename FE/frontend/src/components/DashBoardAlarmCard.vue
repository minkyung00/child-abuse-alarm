<template>
  <b-card>
    <header class="alarm-card-title">
      <b-card-title>
        때리기 발생
      </b-card-title>
      <div class="alarm-badge">
        <b-badge pill variant="danger">Danger</b-badge>
      </div>
    </header>
    <b-card-text>
      날짜: 2022-03-20
    </b-card-text>
  </b-card>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translate3d(0, 100%, 0);
  }
  to {
    opacity: 1;
    transform: translateZ(0);
  }
}

.card {
  background-color: rgba(255, 0, 0, 25%);
  position: relative;
  animation: fadeInUp 0.8s ease-in-out;

  .card-body {
    padding: 1.5rem;
  }
}

.alarm-card-title {
  display: flex;
  align-items: center;
  margin-bottom: 10px;

  h4.card-title {
    font-size: calc(1rem + 0.3vw);
    margin-right: 10px;
    margin-bottom: 0px;
  }

  .badge-danger {
    background-color: red;
  }
}
</style>
