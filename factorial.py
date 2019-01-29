#FACTORIAL

number=int(input("enter the number to calculate its factorial: "))
fact=1
for i in range (number,1,-1):
    fact=fact*i
print("the factorial is:",fact)
