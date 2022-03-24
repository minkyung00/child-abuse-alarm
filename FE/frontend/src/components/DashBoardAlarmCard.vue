<template>
  <div>
    <b-card v-for="alarm in alarmList"
            :key="alarm"
            :class="`alarm-card-${alarm.status}`">
      <header class="alarm-card-title">
        <b-card-title>
          {{ alarm.title }}
        </b-card-title>
        <div class="alarm-badge">
          <b-badge pill :variant="alarm.status">{{ alarm.status }}</b-badge>
        </div>
      </header>

      <main>
        <b-card-text>
          {{ `날짜: ${alarm.date}` }}
        </b-card-text>
        <button class="more-button">자세히보기</button>
      </main>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "DashBoardAlarmCard",
  props: {
    alarmList: Array
  }
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
  position: relative;
  animation: fadeInUp 0.8s ease-in-out;
  margin-bottom: 20px;
  border-radius: 30px;

  .card-body {
    padding: 1.75rem;
  }
}

.alarm-card-danger {
  background-color: $light-red;
}

.alarm-card-success {
  background-color: $light-green;
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

  .badge-success {
    background-color: green;
  }
}

main {
  display: flex;
  justify-content: space-between;
  align-items: center;

  .card-text {
    margin: 0;
  }

  .more-button {
    background-color: rgb(255, 255, 255, 0.5);
    border: 1px solid transparent;
    // border-color: black;
    // padding: 8px 20px;
    // border-radius: 30px;
  }
}
</style>
