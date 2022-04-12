<template>
  <transition name="modal" data-backdrop="static">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <form class="modal-container" @submit.prevent="submitForm">
          <div class="modal-header">
            <img src="https://t1.kakaocdn.net/kakaocorp/kakaocorp/admin/6562f7bc017800001.png?type=thumb&amp;opt=C72x72" width="36" height="36" alt="" class="ico_cate">
            <h5>코드 등록</h5>
            <button
              type="button"
              class="btn-close"
              @click="$emit('close')"
            ></button>
          </div>

          <div class="modal-body">
            <b-form-input
              v-model="code"
              type="text"
              placeholder="코드를 입력하세요"/>
          </div>

          <div class="modal-footer">
            <button 
              class="submit-btn"
              type="submit"
            >등록</button>
          </div>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
import { applyCenterCode } from "@/api/center.js"
export default {
  name: "CenterCodeModal",
  props: {
    centerID: Number
  },
  data () {
    return {
      code: ''
    }
  },
  methods: {
    async submitForm () {
      try {
        const data = {
          username: this.$store.state.userid,
          code: this.code
        }
        const res = await applyCenterCode(this.centerID, data)

        alert(`${res.data.center_name}이 등록되었습니다!`)
        this.$router.push({
          name: 'UserHome'
        })
      } catch (err) {
        alert(err.response.data.error)
        this.$router.go(this.$router.currentRoute)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.modal-header {
  img {
    margin-right: 8px;
  }
}
input {
  padding: 0.75rem 1.5rem;
  border-radius: 30px;
}

h5 {
  margin: 0;
}

.submit-btn {
  width: 5rem;
}
</style>