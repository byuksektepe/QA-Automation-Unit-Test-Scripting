import csv
import gspread
from google.oauth2.service_account import Credentials
from tests.google_chart_api import global_variables as chart_gv


class google_sheets_api_runtime_test:

    def start(self):

        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = Credentials.from_json_keyfile_name('keys/qatestscript-f08c8552be9f.json', scope)
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
        with open()

    pass



