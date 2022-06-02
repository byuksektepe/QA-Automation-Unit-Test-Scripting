import csv
import gspread
from datetime import date
from google.oauth2.service_account import Credentials
from tests.google_chart_api import global_variables as chart_gv


class google_sheets_api_runtime_test:

    def start(self):

        scope = ['https://spreadsheets.google.com/feeds']
        creds = Credentials.from_service_account_file('tests/keys/qatestscript-f08c8552be9f.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open('QATestData').sheet1

        spreadsheet_data = sheet.get_all_values()

        run_times = []

        for row in spreadsheet_data:

            del row[0]
            del row[1]

            run_times.append(row)

        # read csv data
        csv_data = []
        with open('./tests/test_docs/LatestTestRunData.csv') as csv_file:
            file_read = csv.reader(csv_file)
            for row in file_read:
                csv_data.append(row)
        run_date = csv_data[1][2]

        run_date = csv_data[1][2]
        spreadsheet_header_row = run_times[0]
        spreadsheet_header_row.append(run_date)
        del spreadsheet_header_row[0]
        # add the data from each run to the end of the same row in the spreadsheet data
        for spreadsheet_row, csv_row in zip(run_times[1:], csv_data[1:]):
            new_value = csv_row[1]  # second column in the csv data is the new run time
            spreadsheet_row.append(new_value)
            del spreadsheet_row[0]

        # write the new spreadsheet data back into the spreadsheet
        for row_index, row in enumerate(run_times):
            for col_index, cell in enumerate(row):
                sheet.update_cell(row_index + 1, col_index + 3, cell)

        # create a chart

        avg_data = sheet.col_values(2)

        chart_data = [["Test Name", "Diff From Avg"]]
        for avg, current in zip(avg_data[1:], csv_data[1:]):
            diff = float(avg) - float(current[1])
            chart_data.append([current[0], diff])

        chart_data_str = ''
        for row in chart_data[1:]:
            chart_data_str += '%s,\n' % row

        completed_html = chart_gv.html_string.substitute(labels=chart_data[0], data=chart_data_str)

        file_date = date.today()
        with open('tests/test_docs/charts/runtime_sheets_chart_' + str(file_date) + '.html', 'w') as f:
            f.write(completed_html)

    pass



