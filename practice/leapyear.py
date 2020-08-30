def leapyear(year):
    if year % 400 == 0:
        return True
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    return False

if __name__ == "__main__":
    print(leapyear(1990))
    print(leapyear(1800))
    print(leapyear(2000))
    print(leapyear(2500))
