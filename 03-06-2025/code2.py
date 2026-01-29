#write a program to check whether the input is a digit or a number
num=int(input("Enter the integer value:"))
result="digit" if(num>9 and num<=9) else "number"
print(f"{num} is a {result}")