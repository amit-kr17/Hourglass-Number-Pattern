n = int(input("enter the value here for printing Pattern : "))
for i in range(n-1):
    print(" " * i, end="")
    for j in range(n-i,0,-1):
        print(j, end=" ")
    print()
print(" " * (n-1)+"1")
for i in range(n-1):
    print(" " * (n-i-2), end="")
    for j in range(2+i,0,-1):
        print(j, end=" ")
    print() 



    
    

