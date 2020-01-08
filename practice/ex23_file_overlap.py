import urllib

text1 = urllib.urlopen("http://www.practicepython.org/assets/primenumbers.txt")
primes = []
for word in text1.readlines():
    primes.append(word.strip())

text2 = urllib.urlopen("http://www.practicepython.org/assets/happynumbers.txt")
happy = []
for word in text2.readlines():
    happy.append(word.strip())

# print primes
# print happy

print list(set(primes) & set(happy))
