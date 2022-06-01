from string import Template
from tests.read_in_data import read_in_data_test

class google_chart_api_test:

    def start(self):

        column_chart_data = read_in_data_test().start()
        html_string = Template("""
        <html>
        <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
          google.charts.load('current', {packages: ['corechart']});
          google.charts.setOnLoadCallback(drawChart);
          function drawChart () {
              var data = google.visualization.arrayToDataTable([
               $labels,
               $data
              ],
              false); // 'false' means that the first row contains labels, not data.
            var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
              chart.draw(data);
          }
        </script>
        </head>
        <body>
        <div id="chart_div" style="width:800; height:600"></div>
        </body>
        </html>""")

        chart_data_str = ""
