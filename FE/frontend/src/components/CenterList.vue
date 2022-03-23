<template>
  <b-container>
    <b-card v-for="center in centers"
            :key="center"
            :title="center.name">
      <b-card-text>
        {{ center.address }}
      </b-card-text>
      <button @click="handleClickButton(center.id)">등록
        <b-icon icon="arrow-right"></b-icon>
      </button>
    </b-card>
  
    <CenterCodeModal
      v-if="showModal"
      @close="showModal = false"
      :centerID="selectedID"
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
  props: ['centers'],
  data () {
    return {
      showModal: false,
      selectedID: ''
    }
  },
  methods: {
    handleClickButton (id) {
      this.showModal = true
      this.selectedID = id
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
