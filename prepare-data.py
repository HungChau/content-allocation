import csv

units = {}
with open("data/andrew.examples_with_concepts.aggregated.csv","r") as f:
    csvReader = csv.reader(f)
    list_concept = set()
    for row in csvReader:
        row[2] = row[2].replace('[', '')
        row[2] = row[2].replace(']', '')
        row[2] = row[2].replace("'", "")
        row[2] = row[2].replace(' ', '')
        list_concept = list_concept.union(set(row[2].split(",")))
        units[row[0]] = list_concept

with open("data/andrew.problems_with_concepts.csv","r") as f:
    csvReader = csv.reader(f)
    list_concept = set()
    for row in csvReader:
        print(row[3],row[4])



# print(units["1"])
