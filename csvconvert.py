import csv
import json
from pprint import pprint

with open('Tag Template Example.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)

    csvlist = []
    for line in reader:
        csvlist.append(line)

pprint(csvlist)
print(json.dumps(csvlist))
