<template>
  <b-container class="apply">
    <header id="apply-header">
      <h1 class="apply-logo">🌱</h1>
      <h1 class="apply-title">어린이집 등록</h1>
      <p class="apply-desc">어린이집 등록 후 서비스 이용이 가능합니다.</p>
    </header>

    <div class="search-bar">
      <b-icon class="search-icon" icon="search" scale="2"></b-icon>
      <b-form-input v-model="keyword"
                    type="search"
                    placeholder="어린이집명을 입력해주세요." />
    </div>
    <CenterList :centers="centerList" />
  </b-container>
</template>

<script>
import { getCenterList } from '@/api/center'
import CenterList from '@/components/CenterList.vue'

export default {
  name: "ApplyCenter",
  components: {
    CenterList,
  },
  data () {
    return {
      centerList: '',
      keyword: ''
    }
  },
  methods: {
    async getCenterList () {
      try {
        const res = await getCenterList(this.keyword)
        this.centerList = res.data
      } catch (err) {
        console.log(err)
      }
    }
  },
  watch: {
    keyword () {
      this.getCenterList()
    }
  }
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

.search-bar {
  position: relative;
  text-align: center;

  .search-icon {
    position: absolute;
    left: 25px;
    top: 20px;
    margin: 0;
    color: white;
  }
}

input {
  padding: 0.75rem 4rem;
  margin-bottom: 20px;
  border-radius: 30px;
  border: 2.5px solid $primary-color;
  background-color: $primary-color;
  font-weight: bold;
  font-size: 20px;

  &::placeholder {
    color: white;
    font-weight: bold;
  }

  &:focus {
    border-color: $primary-color;
    outline: 0;
    box-shadow: 0 0 0 0.25rem #33d27b52;
    color: $primary-color;
  }
}

</style>
