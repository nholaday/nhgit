# for i in range(1,31):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             print("fizzbuzz")
#         else:
#             print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)

# for i in range(1,31):
#     if i % 3 == i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)

for i in range(1,32):
    st = ""
    if i % 3 == 0:
        st += "fizz"
    if i % 5 == 0:
        st += "buzz"
    if st == "":
        st = i
    print(st)
