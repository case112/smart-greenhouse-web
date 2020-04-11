$(function () {
        
    var $temperatureToday = $("#temp-today");
    $.ajax({
      url: $temperatureToday.data("url"),
      success: function (data) {

        var ctx = $temperatureToday[0].getContext("2d");

        new Chart(ctx, {
          type: 'line',
          data: {
            labels: data.time,
            datasets: [{
              label: "Temperature",
              lineTension: 0.3,
              backgroundColor: "rgba(16, 177, 65, 0.05)",
              borderColor: "rgba(16, 177, 65, 1)",
              pointRadius: 3,
              pointBackgroundColor: "rgba(16, 177, 65, 1)",
              pointBorderColor: "rgba(16, 177, 65, 1)",
              pointHoverRadius: 3,
              pointHoverBackgroundColor: "rgba(16, 177, 65, 1)",
              pointHoverBorderColor: "rgbargba(16, 177, 65, 1)",
              pointHitRadius: 10,
              pointBorderWidth: 2,
              data: data.data
            }]          
          },
          options: {
            maintainAspectRatio: false,
            layout: {
              padding: {
                left: 10,
                right: 25,
                top: 25,
                bottom: 0
              }
            },
            scales: {
              xAxes: [{
                time: {
                  unit: 'date'
                },
                gridLines: {
                  display: false,
                  drawBorder: false
                },
                ticks: {
                  maxTicksLimit: 7
                }
              }],
              yAxes: [{
                ticks: {
                  maxTicksLimit: 5,
                  padding: 10,
                  // Include a degree sign in the ticks
                  callback: function(value, index, values) {
                    return number_format(value) + '°C';
                  }
                },
                gridLines: {
                  color: "rgb(234, 244, 235)",
                  zeroLineColor: "rgb(234, 236, 244)",
                  drawBorder: false,
                  borderDash: [2],
                  zeroLineBorderDash: [2]
                }
              }],
            },
            legend: {
              display: false
            },
            tooltips: {
              backgroundColor: "rgb(255,255,255)",
              bodyFontColor: "#858796",
              titleMarginBottom: 10,
              titleFontColor: '#6e707e',
              titleFontSize: 14,
              borderColor: '#dddfeb',
              borderWidth: 1,
              xPadding: 15,
              yPadding: 15,
              displayColors: false,
              intersect: false,
              mode: 'index',
              caretPadding: 10,
              callbacks: {
                label: function(tooltipItem, chart) {
                  var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                  return datasetLabel + ': ' + number_format(tooltipItem.yLabel) + '°C';
                }
              }
            }
          }
        });

      }
    });

  });