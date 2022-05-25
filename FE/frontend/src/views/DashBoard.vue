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
        <WeeklyDoghnutChart />
        <b-card>
          <b-card-title>
            <img src="https://www.kakaocorp.com/page/ico_stock.png" width="36" height="36" alt="" class="ico_cate">  이번 달
          </b-card-title>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
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
      alarmList: [
        {
          id: 1,
          title: "때리기 발생",
          status: "danger",
          date: "2022-03-20"
        },
        {
          id: 2,
          title: "밀치기 발생",
          status: "warning",
          date: "2022-03-21"
        },
      ],
      result: ''
    }
  },
  created () {
    this.connect()
    this.getNotification()
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
          for (const alarm of alarms) {
            this.alarmList.push(alarm);
          }
        }
      };
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
  margin-top: -40px;
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
