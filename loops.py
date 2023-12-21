# for 

# while
# infinite loop
# num = 10
# while(num>0):
#     print(num)#
#     num = num - 1

# for
# initialize, condition , skip
# start , stop, skip
# for i in range(10,0,-1):
#     print(i)

# Question
# Factorial of any number n
# Sum of number

# num = int(input("Enter the number for factorial : "))#4

# fact = 1
# for i in range(1,num+1):
#     fact = fact * i

# print("The factorial of ", num , "is : ",fact)



# Prime Number
# Check if a number is prime number

# 1 2 3 4 5 6 7
# sum = 0
# count = 0
# for j in range(1,101):
#     num = j
#     chk = True
#     for i in range(2,num):
#         if(num%i==0):
#             chk = False
    
#     if chk==True:
#         print(num)
#         sum= sum+num
#         count = count + 1

# print("Sum of nums : ", sum)
# print("Count of nums : ", count)


for i in range(1,6):
    for j in range(1,i+1):
        print("*" , end="")
    print()

