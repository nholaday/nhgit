testlist = ['a','b','c','d','']
dic = {}
testlist.remove('')
print testlist
print dic

for l in testlist:
    dic[l] = ["yo"]

print dic

for l2 in testlist:
    dic[l2].append('hi')

print dic

for d in dic:
    print d, dic[d]
