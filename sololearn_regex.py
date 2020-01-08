import re

def checkregex(pattern, terms):
    for term in terms:
        if re.match(pattern, term):
            print term
    print ""

pattern = "poke"
string = "poke the pokemon with that pole dude!"
terms = string.split(" ")

# checkregex(pattern, terms)
# 
# # '.' matches any character
# pattern = "po.e"
# checkregex(pattern,terms)
# 
# # ^ and $ mark the beginning and end of a word respectively
# pattern = "^po.e$"
# checkregex(pattern,terms)

# [a-y] matches letters a-y. use [^a-y] to match everything but a-y


# For everything that matches "^BINARY OUTPUT (\\d+)":
#     Metadata/Extra/Whatever = "room capture $1"
# Python uses mat.group(1) or "\1" instead of "$1"
csv_import = [{"Enabled": "TRUE", "Metadata/Extra/NewTag": "room flatscreen", "Point regex": "^ANALOG INPUT 0$", "Device regex": "SimpleS"}, {"Enabled": "FALSE", "Metadata/Extra/NewTag": "room ratatat poster", "Point regex": "^BINARY INPUT", "Device regex": "SimpleS"}, {"Enabled": "FALSE", "Metadata/Extra/NewTag": "cooling setpoint offset", "Point regex": "Cooling SP Offset", "Device regex": "SimpleS"}, {"Enabled": "None", "Metadata/Extra/NewTag": "room damper output", "Point regex": "ANALOG OUTPUT 2", "Device regex": "SimpleS"}, {"Enabled": "", "Metadata/Extra/NewTag": "room temperature", "Point regex": "^ANALOG INPUT 1$", "Device regex": "SVAV"}, {"Enabled": "FALSE", "Metadata/Extra/NewTag": "room capture $1", "Point regex": "^BINARY OUTPUT (\\d+)$", "Device regex": "SimpleS"}]

row = csv_import[-1]

print row['Point regex']
print row['Metadata/Extra/NewTag'].replace('$','\\')
print "^BINARY OUTPUT (\d+)"
MetadataBACnetName = "BINARY OUTPUT 8" #obj.tags.get('

newtag = row['Metadata/Extra/NewTag'][:-1].replace('$','\\') + row['Metadata/Extra/NewTag'][-1]
print newtag
mat = re.match(row['Point regex'], MetadataBACnetName)
newstring = re.sub(row['Point regex'], newtag, MetadataBACnetName)
newstring = re.sub("^BINARY OUTPUT (\d+)$", "room capture \\1$", "BINARY OUTPUT 8")
print newstring
# print mat.group(1)
