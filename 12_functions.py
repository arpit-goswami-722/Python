# def greet():
#     print("hello")

# greet() 

#sum function: ---> positional arguement 
# def sum(a,b):
#     print(f"sum is {a+b}")

# sum(45,67)

# example for keyword arguement 
# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")
# hello(age=21 , name = "arpit")

#example for default arguement 

# def sum(a,b=43):
#     print(f"sum is {a+b}")
# sum(34) # here b = 43 is a default parameter and if b new value is provided then it will be called default arguement

# function for pallindrome
# def pallindrome(st):
#     rev = "" 
#     for i in range(len(st)-1,-1,-1):
#      rev = rev + st[i]
#     if rev == st:
#        print("pallindrome")
#     else :
#        print("Not a pallindrome")
# pallindrome("naman")
# pallindrome("mouse")

# return vs print 

# def greet():
#     return "hello"
# print(greet()) # in return we have to print function 