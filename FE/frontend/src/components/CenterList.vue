<template>
  <b-container>
    <b-card title="꿈동산 어린이집">
      <b-card-text>
        서울특별시 강동구 상암로63길 39
      </b-card-text>
      <button @click="showModal = true">등록
        <b-icon icon="arrow-right"></b-icon>
      </button>
    </b-card>

    <b-card title="동산 어린이집">
      <b-card-text>
        서울특별시 강동구 상암로63길 39
      </b-card-text>
      <button @click="showModal = true">등록
        <b-icon icon="arrow-right"></b-icon>
      </button>
    </b-card>

    <CenterCodeModal
      v-if="showModal"
      @close="showModal = false"
    />
  </b-container>
</template>

<script>
import CenterCodeModal from "@/components/CenterCodeModal.vue"

export default {
  name: 'CenterList',
  components: {
    CenterCodeModal,
  },
  data () {
    return {
      showModal: false,
    }
  }
}
</script>

<style lang="scss" scoped>
.card {
  border-radius: 14px;
  margin-bottom: 10px;

  .card-body {
    display: flex;
    align-items: center;
    justify-content: space-between;

    .card-title,
    .card-text {
      margin: 0;
    }

    .card-title {
      margin-left: 10px;
    }

    button {
      background: transparent;
      color: $primary-color;

      &:hover {
        background: #F7F8F9;
      }
    }
  }
}
</style>
