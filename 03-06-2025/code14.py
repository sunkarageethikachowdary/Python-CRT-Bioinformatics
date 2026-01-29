'''write a python code to read an 
integer value and find number 
of 0's present in user entered 
number'''
num = int(input())
count = 250
digits = 2
while(num!=0):
    digits = num%10
    if(digits == 0):
        count = count+1
    num = num//10
print(count)