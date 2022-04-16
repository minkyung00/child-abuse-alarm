<template>
  <div>
    <h3>{{ centerName }}</h3>
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
    DashBoardAlarmCard
  },
  data () {
    return {
      centerName: this.$store.state.center,
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
          status: "success",
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
        const res = JSON.parse(e.data);

        if (res.data) {
          this.alarmList.push(res.data);
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
  @media (max-width: 780px) {
    display: block;
  }
}

.card {
  border: none;
  border-radius: 14px;
  box-shadow: 4px 12px 30px 6px rgb(0 0 0 / 9%);
  margin-bottom: 1rem;

  .card-title {
    margin-bottom: 1rem;
  }

  .card-body {
    padding: 1.5rem;
  }
}
</style>
