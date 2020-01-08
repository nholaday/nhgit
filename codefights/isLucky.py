def isLucky(n):
    # Create list of digits
    digits = map(int,list(str(n)))
    return sum(digits[:len(digits)/2]) == sum(digits[len(digits)/2:])
    
def python3isLucky(n):
    # map is different.  
    # len(digits)/2 gives a float, use len(digits)//2
    digits = list(map(int,list(str(n))))
    midway = int(len(digits) / 2)
    return sum(digits[:midway]) == sum(digits[midway:])
    
print(isLucky(423045))