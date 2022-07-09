import csv
from modify_input import modify_rows


file = "Input_1.csv"

fields = []
rows = []

with open(file, 'r') as csvfile:
    #creating csv reader object
    csvreader = csv.reader(csvfile)

    #extracting fields names
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)


modified_rows = modify_rows(rows,fields)


output_filename = "output.csv"
output_fields = ['Name', 'Username', 'Chapter Tag', 'Test_Name', 'answered', 'correct', 'score', 'skipped', 'time-taken (seconds)', 'wrong']

with open(output_filename,'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(output_fields)
    csvwriter.writerows(modified_rows)