# Guessing Number

x= 20
y=0
while y is not x:
    y = int(input("Enter a number from 1-20 to guess :"))
    if(y < x):
        print("Enter a larger number")
    elif (y > x):
        print("Enter a Smaller number") 
     
print("you won!!")