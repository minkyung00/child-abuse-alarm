<template>
  <b-row>
    <h3>꿈동산 어린이집</h3>
    <b-col>
      <!-- <h3>꿈동산 어린이집</h3> -->
      <b-card>
        <b-card-title>
          <img src="https://t1.kakaocdn.net/kakaocorp/kakaocorp/admin/6562f7bc017800001.png?type=thumb&amp;opt=C72x72" width="36" height="36" alt="" class="ico_cate">  알람
        </b-card-title>
        <DashBoardAlarmCard />
      </b-card>
    </b-col>
    <b-col>
      <b-card>
        <b-card-title>
          <img src="https://www.kakaocorp.com/page/ico_stock.png" width="36" height="36" alt="" class="ico_cate">  현황
        </b-card-title>
      </b-card>
    </b-col>
  </b-row>
</template>

<script>
import DashBoardAlarmCard from "@/components/DashBoardAlarmCard.vue"
export default {
  name: "DashBoard",
  components: {
    DashBoardAlarmCard
  }
}
</script>

<style lang="scss" scoped>
.card {
  border: none;
  border-radius: 14px;
  box-shadow: 4px 12px 30px 6px rgb(0 0 0 / 9%);

  .card-title {
    margin-bottom: 1rem;
  }

  .card-body {
    padding: 1.5rem;
  }
}
</style>
