thickness_readings = [0.009,0.0085,0.0082, 0.0081,0.0071]
reading_dates = ["2014-02-27","2015-03-17","2016-02-10","2017-05-13","2018-08-13"]
tmin = 0.004
predict_x = ['2017-05-13', '2026-08-11']
predict_y = [0.0081, 0.00170616]

console.log(reading_dates[0])
console.log(predict_x[predict_x.length-1])

var trace1 = {
  x: reading_dates,
  y: thickness_readings,
  type: 'scatter'
}

var layout = {
  title: 'TML Corrosion Rate',
  yaxis: {
    rangemode:'tozero'

  },
  shapes: [
    {
    type: 'line',
    x0: reading_dates[0],
    y0: tmin,
    x1: predict_x[predict_x.length-1],
    y1: tmin,
    line: {
      color: 'red',
      width: 4
    }
    },
    {
      type: 'line',
    x0: predict_x[0],
    y0: predict_y[0],
    x1: predict_x[predict_x.length-1],
    y1: predict_y[1],
    line: {
      color: 'green',
      width: 1,
      dash: 'dot'
    }
    }
  ]
}

var data = [trace1]

//psi_graph = document.getElementById('psiGraph');

Plotly.newPlot('psiGraph', data, layout)
