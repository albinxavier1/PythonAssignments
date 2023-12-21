num = 345
t1 = num
rev = 0 #321

while(t1>0): #0
    digit = t1%10 #1
    rev = rev*10+digit 
    t1//=10

if(num==rev):
    print("Palindrome")
else:
    print("Not Palindrome")


# 121
# 1+20+100
# 121

# 123
# 3+20+100
# 321