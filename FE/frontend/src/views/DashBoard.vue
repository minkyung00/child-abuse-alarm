<template>
  <div>
    <!-- <h3>{{ centerName }}</h3> -->
    <b-row>
      <b-col cols="3">
        <b-card>
          <b-card-title>
            <img src="https://t1.kakaocdn.net/kakaocorp/kakaocorp/admin/6562f7bc017800001.png?type=thumb&amp;opt=C72x72" width="36" height="36" alt="" class="ico_cate">  알람
          </b-card-title>
          <DashBoardAlarmCard :alarmList=alarmList />
        </b-card>
      </b-col>

      <b-col cols="6">
        <WeeklyDoghnutChart
          :weeklyData="weekly"
        />
        <!-- <b-card>
          <b-card-title>
            <img src="https://www.kakaocorp.com/page/ico_stock.png" width="36" height="36" alt="" class="ico_cate">  이번 달
          </b-card-title>
        </b-card> -->
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { getWeeklyNotification } from "@/api/notification"

import DashBoardAlarmCard from "@/components/DashBoard/AlarmCard.vue"
import WeeklyDoghnutChart from "@/components/DashBoard/WeeklyDoghnutChart.vue"

const socket = new WebSocket(
  'ws://'
  + '127.0.0.1:8000'
  + '/ws/notification/'
  + 'center_name'
  + '/'
);

export default {
  name: "DashBoard",
  components: {
    DashBoardAlarmCard,
    WeeklyDoghnutChart
  },
  data () {
    return {
      // centerName: this.$store.state.center,
      centerName: '천호어린이집',
      alarmList: [],
      result: '',
      weekly: ''
    }
  },
  created () {
    this.connect()
    this.getNotification()
    this.getWeeklyNotification()
  },
  methods: {
    connect () {
      socket.onopen = function(e) {
        console.log('서버와 연결되었습니다.')
      };
    },
    getNotification() {
      socket.onmessage = (e) => {
        const alarms = JSON.parse(e.data).data;

        if (alarms) {
          for (let alarm of alarms) {
            alarm.created_time = this.changeTimeFormat(alarm.created_time)
            this.alarmList.push(alarm);
          }
        }
      };
    },
    async getWeeklyNotification () {
      try {
        const res = await getWeeklyNotification()
        this.weekly = res.data
        this.setWeeklyPercent()
      } catch (err) {
        console.log(err)
      }
    },
    changeTimeFormat (now) {
      let date = now.slice(0, 10)
      let time = now.slice(11, 19)
      return `${date} ${time}`
    },
    setWeeklyPercent () {
      let total = this.weekly.total_danger + this.weekly.total_warning + this.weekly.total_caution

      this.weekly.percentDanger = ((this.weekly.total_danger / total).toFixed(3)) * 100
      this.weekly.percentWarning = ((this.weekly.total_warning / total).toFixed(3)) * 100
      this.weekly.percentCaution = ((this.weekly.total_caution / total).toFixed(3)) * 100
    }
  }
}
</script>

<style lang="scss" scoped>
h3 {
  padding: 1rem;
}

.row {
  justify-content: center;
  margin-top: -20px;
}

.col-6 {
  @media (max-width: $break-xlarge) {
    width: 60%;
  }
}

.col-3,
.col-6 {
  @media (max-width: $break-large) {
    width: 90%;
  }
}

</style>
