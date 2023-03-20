<template>
  <div>
    <b-card
      v-for="alarm in alarmList"
      :key="alarm.id"
      :class="`alarm-card-${alarm.status}`">

      <header class="alarm-card-title">
        <!-- <img src="../assets/alert-1.png" alt="" width="36" height="36"> -->
        <div class="alarm-badge">
          <b-badge
            pill
            :variant="alarm.status"
          >{{ alarm.status }}</b-badge>
        </div>
        <b-card-title>
          {{ alarm.title }}
        </b-card-title>
      </header>

      <main>
        <b-card-text>
          {{ `${alarm.created_time}` }}
        </b-card-text>
        <button
          class="more-button"
          @click="showAlarmModal(alarm)"
        >자세히보기</button>
      </main>
    </b-card>
    <AlarmModal
      v-if="showModal"
      @close="showModal = false"
      :notificationID="selectedID"
      :notification="notification"
    />
  </div>
</template>

<script>
import AlarmModal from "@/components/DashBoard/AlarmModal.vue"
export default {
  name: "DashBoardAlarmCard",
  components: {
    AlarmModal
  },
  props: {
    alarmList: Array,
  },
  data () {
    return {
      showModal: false,
      selectedID: '',
      notification: ''
    }
  },
  methods: {
    showAlarmModal (alarm) {
      this.showModal = true
      this.selectedID = alarm.id
      this.notification = alarm
    },
  }
}
</script>

<style lang="scss" scoped>
@import '../../styles/_mixin.scss';

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
  border: none;
  border-radius: 30px;
  box-shadow: rgb(0 0 0 / 4%) 0px 4px 16px 0px;
  transition: box-shadow 0.25s ease-in 0s, transform 0.25s ease-in 0s;
  &:hover {
    box-shadow: 0px 4px 24px 0px rgb(0 0 0 / 10%);
    transform: translateY(-10px);
  }

  .card-body {
    padding: 1.75rem;
    @media (max-width: 780px) {
      padding: 1.5rem;
    }
  }
}

.alarm-card-danger {
  color: $color-text-danger;
  background-color: $color-bg-danger;
}

.alarm-card-warning {
  color: $color-text-warning;
  background-color: $color-bg-warning;
}

.alarm-card-title {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  @media (max-width: $break-xlarge) {
    display: block;
  }

  h4.card-title {
    @include ellipse;
    margin-bottom: 0px;
    font-size: calc(1rem + 0.3vw);
  }
}

main {
  display: flex;
  justify-content: space-between;
  align-items: center;
  @media (max-width: $break-xlarge) {
    display: block;
  }

  .card-text {
    @include ellipse;
    margin: 0;
    color: $color-grey-700;
    font-size: calc(0.7rem + 0.3vw);
    font-weight: $font-weight-semibold;
  }

  .more-button {
    @include ellipse;
    color: $color-grey-800;
    background-color: rgb(255, 255, 255, 0.5);
    border: 1px solid transparent;
    font-size: calc(0.7rem + 0.3vw);
    @media (max-width: $break-xlarge) {
      float: right;
    }
  }
}
</style>
