# list functions map and filter can run a function for all items in a list

def triple(x):
    return x*3

nums = [4,7,9,14,17,19]
print nums

trips = list(map(triple,nums))
print trips

# can also do it using lambda
print list(map(lambda x:x*3,nums))

# filter takes out all non matching items
odds = list(filter(lambda x: x % 2 == 1,nums))
print odds
