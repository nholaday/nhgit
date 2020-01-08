import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def Main():
    parser = argparse.ArgumentParser()
    
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("-v","--verbose", action="store_true")
    group1.add_argument("-q","--quiet", action="store_true")

    parser.add_argument("num", help="The Fibonacci number "
                        "you wish to calculate", type=int)
    parser.add_argument("-o","--output", help="Output the " 
                        "result to file", action="store_true")
    args = parser.parse_args()

    result = fib(args.num)
    if args.verbose:
        print("The {}th fib number is: {}".format(args.num, result))
    elif args.quiet:
        print(result)
    else:
        print("Fib({}) = {}".format(args.num, result))
    if args.output:
        f = open("fibonacci.txt", "a")
        f.write(str(result) + "\n")
        f.close()

if __name__ == "__main__":
    Main()
