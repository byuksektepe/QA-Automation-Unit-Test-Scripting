from string import Template
from datetime import date
from tests.read_in_data import read_in_data_test

class google_chart_api_test:

    def start(self):

        column_chart_data = read_in_data_test().start()
        html_string = Template("""<html>
        <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
          google.charts.load('current', {packages: ['corechart']});
          google.charts.setOnLoadCallback(drawChart);
          function drawChart () {
              var data = new google.visualization.DataTable();
              data.addColumn('string', 'Element');
              data.addColumn('number', '$labels');
              data.addRows([
                $data
              ]);
            var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
              chart.draw(data);
          }
        </script>
        </head>
        <body>
        <div id="chart_div" style="width:800; height:600"></div>
        </body>
        </html>""")

        chart_data_str = ''
        for row in column_chart_data[1:]:
            chart_data_str += '%s,\n' % row

        completed_html = html_string.substitute(labels=column_chart_data[0][1],
                                                data=chart_data_str)
        file_date = date.today()
        with open('tests/test_docs/column_chart'+str(file_date)+'.html', 'w') as f:
            f.write(completed_html)
