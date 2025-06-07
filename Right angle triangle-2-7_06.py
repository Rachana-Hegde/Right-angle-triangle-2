a=int(input())
for row in range(1,a+1):
    for col in range(a):
        if row+col==a-1:
            print("* " * row, end=" ")
        elif row == a:
            print("+", end=" ")
    print("")