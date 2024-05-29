# print("hello")
rows = int(input())
for i in range(1,rows+1):
    print("" * (rows-i),end="")
    print("*" * i)

# for s in range(3):
#     for q in range(4):
#         print("*" ,end= "")
#     print()