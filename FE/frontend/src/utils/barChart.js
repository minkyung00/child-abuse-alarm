import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

import { Bar } from "vue-chartjs/legacy";
export default {
  extends: Bar,
  props: ["chartData", "options"],
  mounted () {
    this.renderChart(this.chartData, this.options);
  }
}
