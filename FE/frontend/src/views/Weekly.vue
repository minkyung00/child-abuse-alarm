<template>
  <div class="weekly">
    <WeeklyDoghnutChart
      :weeklyData="weekly"
    />
    <WeeklyBarChart
      :weeklyData="weekly"
    />
  </div>
</template>

<script>
import { getWeeklyNotification } from "@/api/notification"
import WeeklyDoghnutChart from "@/components/DashBoard/WeeklyDoghnutChart.vue"
import WeeklyBarChart from "@/components/DashBoard/WeeklyBarChart.vue"

export default {
  name: 'Weekly',
  components: {
    WeeklyDoghnutChart,
    WeeklyBarChart
  },
  data() {
    return {
      weekly: ''
    }
  },
  created () {
    this.getWeeklyNotification()
  },
  methods: {
    async getWeeklyNotification () {
      try {
        const res = await getWeeklyNotification()
        this.weekly = res.data
        this.setWeeklyPercent()
      } catch (err) {
        console.log(err)
      }
    },
    setWeeklyPercent () {
      let total = this.weekly.total_danger + this.weekly.total_warning + this.weekly.total_caution
      
      this.weekly.percentDanger = ((this.weekly.total_danger / total).toFixed(3)) * 100
      this.weekly.percentWarning = ((this.weekly.total_warning / total).toFixed(3)) * 100
      this.weekly.percentCaution = ((this.weekly.total_caution / total).toFixed(3)) * 100
    }
  },
}
</script>

<style lang="scss" scoped>
.weekly {
  // display: flex;
  width: 70%;
  min-width: 350px;
  // flex-direction: column;
  // justify-content: center;
  // align-items: center;
}
</style>