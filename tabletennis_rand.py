import csv
import random

cola, colb = [], []
with open('Table_Tennis_Teams.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        cola.append(row[0])
        colb.append(row[1])

random.shuffle(cola)
random.shuffle(colb)

teams = ["{}, {}".format(a,b) for a,b in zip(cola, colb)]

print ""
for item in teams:
    print item
print ""


# To create bracket: https://brackets.commoninja.com/app

# Or use the code below to create a bracket in the shell
# from bracket import bracket
# brac = bracket.Bracket(teams)
# brac.show()
