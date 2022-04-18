import os
import csv


class CSV_Dataset:
    def __init__(self, file):
        self.file = file
        self.headers = []
        self.read()

    def read(self):
        self.dataset = []
        with open(os.path.join("datasets", self.file + ".csv"), "r") as csv_file:
            reader = csv.DictReader(csv_file)
            self.headers = reader.fieldnames
            for row in reader:
                self.dataset.append(row)

    def write(self):
        with open(os.path.join("datasets", self.file + ".csv"), "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.headers)
            writer.writeheader()
            for row in self.dataset:
                writer.writerow(row)
