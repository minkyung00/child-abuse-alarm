<template>
  <div>
    <b-card>
      <b-card-title>
        <img src="https://www.kakaocorp.com/page/ico_stock.png" width="36" height="36" alt="" class="ico_cate">  이번 주 폭력행위별 추이
      </b-card-title>
      <b-card-text>
        <BarChart
          ref="weeklyChart"
          :chartData="chart.data"
          :options="chart.options"
          id="chart-container"
        />
      </b-card-text>
      <button class="detail-button">상세히 보러가기</button>
    </b-card>
  </div>
</template>

<script>
import BarChart from "@/utils/barChart.js"
const data = {
  labels: ['월', '화', '수', '목', '금', '토', '일'],
  datasets: [
    {
      label: '때리기',
      data: [5, 3, 2, 1, 6, 2, 4],
      borderColor: '#15c07d',
      backgroundColor: '#15c07d'
    },
    {
      label: '발차기',
      data: [6, 5, 0, 1, 3, 5, 0],
      borderColor: '#bcf5d5',
      backgroundColor: '#bcf5d5'
    },
  ]
}
export default {
  name: "WeeklyBarChart",
  components: {
    BarChart
  },
  data () {
    return {
      chart: {
        type: 'bar',
        data: data,
        // data: {
        //   labels: ['월', '화', '수', '목', '금', '토', '일'],
        //   datasets: [{
        //     backgroundColor: [
        //       'rgba(255, 99, 132)',
        //       'rgba(255, 159, 64)',
        //       'rgba(255, 205, 86)',
        //       'rgba(75, 192, 192)',
        //       'rgba(54, 162, 235)',
        //       'rgba(153, 102, 255)',
        //       'rgba(201, 203, 207)'
        //     ],
        //     // borderColor: [
        //     //   "rgba(255, 99, 132, 1)",
        //     //   "rgba(255, 159, 64, 1)"
        //     // ],
        //     data: [65, 59, 80, 81, 56, 55, 40],
        //     borderWidth: 1,
        //     hoverOffset: 4,
        //   }]
        // },
        options: {
          plugins: {
            title: {
              display: true,
              text: '이번주 어린이집 내 폭력행위별 추이'
            },
            legend: {
              display: true,
              position: "bottom",
              labels: {
                font: {
                  // size: 20
                }
              },
              tooltip: {
                boxWidth: 15,
                bodyFont: {
                  size: 16
                }
              },
              layout: {
                padding: 20
              },
              // responsive: false,
              maintainAspectRatio: false,
            }
          },
          scales: {
            y: {
              min: 0,
              max: 10,
              ticks: {
                // forces step size to be 50 units
                stepSize: 1
              }
            },
          }
          // indexAxis: 'y'
        }
      },
    }
  }
}
</script>

<style lang="scss" scoped>
.card-text {
  justify-content: center;
  @media (max-width: $break-small) {
    display: block !important;
  }
}

#chart-container {
  // position: relative;
  // width: calc(120px + 60vw);
  // height: calc(120px + 60vw);
  width: 70%;
  height: 70%;
  min-width: 300px;
  min-height: 300px;
}

.chart-description {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  padding: 1rem 1.5rem;


  .chart-title {
    margin-bottom: 40px;
  }

  .chart-legend {
    // margin: 1.5rem 0;

    &::after {
      content: '';
      display: block;
      height: 1px;
      margin: 1.5rem 0;
      background-color: $color-grey-300;
    }

    .chart-legend__info {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .chart-legend__label {
      display: flex;
      align-items: center;
    }

    p {
      margin: 0;
      font-weight: $font-weight-semibold;
    }

    .percent {
      font-size: 18px;
      @media (max-width: $break-xlarge) {
        display: none;
      }
      @media (max-width: $break-large) {
        display: block;
      }
    }

    .total {
      flex-shrink: 0;
      font-size: calc(0.75rem + 0.7vw);
    }
  }
}



.badge {
  padding: 0.5em 2em;
  margin: 0 1.5rem;
  border-radius: 1rem;
  color: white;
  font-size: calc(0.5rem + 0.4vw);
}

.kick-badge {
  background-color: $color-text-warning;
}

.hit-badge {
  background-color: $color-text-danger;
}

.detail-button {
  float: right;
  background-color: transparent;
  color: $color-nav-green;
}
</style>