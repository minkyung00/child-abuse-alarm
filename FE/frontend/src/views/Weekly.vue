<template>
  <div class="weekly">
    <WeeklyDoghnutChart />
    <WeeklyBarChart />
  </div>
</template>

<script>
import WeeklyDoghnutChart from "@/components/DashBoard/WeeklyDoghnutChart.vue"
import WeeklyBarChart from "@/components/DashBoard/WeeklyBarChart.vue"

export default {
  name: 'Weekly',
  components: {
    WeeklyDoghnutChart,
    WeeklyBarChart
  }
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