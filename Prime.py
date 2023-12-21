# 5
# 1 2 3 4 5 


num = 5
checkPrime = True
for i in range(2,num):
    if(num%i==0):
        checkPrime = False
        break


if(checkPrime==True):
    print("Prime NUmber")
else:
    print("Not Prime")


