count  = 0
for i in range(100,10001):
    num = i
# Count the number of digits
    digit = 0 #4
    t1 = num #1634
    while(t1>0):#0
        t1//=10 
        digit+=1

    # multiply individual digit to the number of total digits 
    t2 = num #0
    sum = 0 #1634
    while(t2>0): #
        rem = t2%10 #1
        product = 1 #1
        for i in range(1,digit+1):
    #                   1*1    
            product = product*rem

    # add the products
        sum = sum+product
        t2//=10

    # compare the sum to the original number
    if(num==sum):
        print(num)
        count+=1
    
print()   