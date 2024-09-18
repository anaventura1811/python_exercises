import csv

def read(path):
  with open(path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
  return [row for row in reader]
  