# Armstrong number

num = 153

digit = len(str(num))

t1 = num
sum = 0
while(t1>0):
    multiply = 1
    rem = t1%10
    multiply = rem**digit
    sum+=multiply
    t1//=10

if(sum==num):
    print("Armstrong")
else:
    print("Not Armstrong")