import csv
import gspread
from google.oauth2.service_account import Credentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_json_keyfile_name('keys/qatestscript-f08c8552be9f.json', scope)
client = gspread.authorize(creds)

sheet = client.open('QATestData').sheet1

spreadsheet_data = sheet.get_all_values()

run_times = []

