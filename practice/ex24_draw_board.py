# This creates the board using for loops
# def create_board(size):
#     for i in range(1,size+1):
#         print "",
#         for j in range(1,size+1):
#             print "---",
#         print ""
#         for k in range(1,size+1):
#             print "|  ",
#         print "|"
#     print "",
#     for j in range(1,size+1):
#         print "---",


def create_board(size):
    for i in range(size):
        print (" ---" * size)
        print ("|   " * size + "|")
    print (" ---" * size)
    
siz = int(raw_input("What size board: "))
create_board(siz)
