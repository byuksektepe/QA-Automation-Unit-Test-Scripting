import csv

class read_in_data_test:
    timing_data = []
    def start(self):

        with open("test_docs/TestTimingData.csv") as test_csv_file:
            file_read = csv.reader(test_csv_file)

            for row in file_read:
                self.timing_data.append(row)

