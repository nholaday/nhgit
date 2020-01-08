magnus = [(1,2),(3,3),(4,5),(6,6)]

print magnus

for listitem in magnus:
    print listitem
    if listitem[0] == listitem[1]:
        print("Match!")
    else:
        print("No Match :(")