import { Chart, registerables } from "chart.js"
Chart.register(...registerables)
let chart

import { Doughnut } from "vue-chartjs/legacy";
export default {
  extends: Doughnut,
  props: ["chartData", "chartOptions", "weeklyData"],
  async mounted () {
    this.$nextTick(function () {
      this.createChart()
    })
  },
  methods: {
    createChart() {
      if (chart !== undefined) {
        chart.destroy()
      }
      chart = new Chart(this.$refs.doughnutChart, {
        type: 'doughnut',
        data: this.chartData,
        options: this.chartOptions
      })
      chart.data.datasets[0].data = [
        this.weeklyData.total_danger,
        this.weeklyData.total_warning,
        this.weeklyData.total_caution
      ]
      chart.update()
    },
  },
  watch: {
    weeklyData () {
      this.createChart()
    },
    deep: true
  }
}