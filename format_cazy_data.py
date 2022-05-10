#format the cazy_data.txt

import sys
import csv

input_file = sys.argv[1]
output_file = input_file.replace(".txt", "_formatted.csv")

rows = []
for line in open(input_file, 'r'):
    fields = line.strip().split("\t")
    rows.append(fields)

header = ["CAZY","SUPERKINGDOM", "NAME", "ACCESSION"]
with open(output_file, 'wt', newline='') as f:
    csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

    csv_writer.writerow(header) # write header

    csv_writer.writerows(rows)