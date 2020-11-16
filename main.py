# Python Program to find Factors of a Number #

Number = int(input("Please Enter any Number: "))

value = 1;
print("Factors of A given Number {0} are :",format (Number))

while(value <= Number):
    if(Number % value == 0):
        print("{0}",format(value))
    value = value +1