<template>
  <div>
    <h3>꿈동산 어린이집</h3>
    <b-row>
      <b-col>
        <b-card>
          <b-card-title>
            <img src="https://t1.kakaocdn.net/kakaocorp/kakaocorp/admin/6562f7bc017800001.png?type=thumb&amp;opt=C72x72" width="36" height="36" alt="" class="ico_cate">  알람
          </b-card-title>
          <DashBoardAlarmCard :alarmList=alarmList />
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
  </div>
</template>

<script>
import DashBoardAlarmCard from "@/components/DashBoardAlarmCard.vue"
export default {
  name: "DashBoard",
  components: {
    DashBoardAlarmCard
  },
  data () {
    return {
      alarmList: [
        {
          title: "때리기 발생",
          status: "danger",
          date: "2022-03-20"
        },
        {
          title: "밀치기 발생",
          status: "success",
          date: "2022-03-21"
        },
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
h3 {
  padding: 1rem;
}

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
