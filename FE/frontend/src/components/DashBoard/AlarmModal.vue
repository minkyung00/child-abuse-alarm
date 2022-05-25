<template>
  <transition name="modal" data-backdrop="static">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <form class="modal-container"
              @submit.prevent="submitForm">

          <div class="modal-header">
            <div class="alarm-badge">
              <b-badge
                pill
                :variant="notification.status"
                :class="`badge-${notification.status}`"
              >{{ notification.status }}</b-badge>
            </div>
            <h5 class="alarm-title">{{ notification.title }}</h5>
            <p class="alarm-date">{{ notification.date }}</p>
            <button
              type="button"
              class="btn-close"
              @click="$emit('close')"
            ></button>
          </div>

          <div class="modal-body">
            <video controls>
              <source
                :src="notification.content"
                type="video/mp4"
              >
            </video>
            <!-- <b-form-input
              v-model="code"
              type="text"
              placeholder="코드를 입력하세요"/> -->
          </div>

          <div class="modal-footer">
            <button 
              class="submit-btn"
              type="submit"
            >확인</button>
          </div>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "AlarmModal",
  props: {
    notificationID: Number,
    notification: Object
  },
  data () {
    return {
      code: ''
    }
  },
  methods: {
  }
}
</script>

<style lang="scss" scoped>
video {
  width: 100%;
}

h5 {
  margin: 0;
}

.alarm-date {
  margin-left: 10px;
  color: $color-grey-700;
  font-size: 14px;
}

.submit-btn {
  width: 5rem;
}
</style>