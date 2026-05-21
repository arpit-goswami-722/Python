#1 : seperate each digit of a number and print it on the new line .

# a = int(input("enter your number here :"))
# while a>0:
#     print(a%10)
#     a = a//10

#2 accept a number and print its inverse 
# a = int(input("enter your number :"))
# rev = 0
# while a>0:
#     temp = a % 10
#     rev = rev*10 + temp
#     a = a//10

# print(f"reverse is {rev}")

#3 : check if a number is pallindromic number 
# a = int(input("Enter your number here :"))
# orig_num = a
# rev = 0
# while a>0:
#     temp = a%10
#     rev = rev*10 + temp
#     a = a//10
# if orig_num == rev:
#     print("Yes , it's a pallindromic number")
# else : print("No , it's not a pallindromic number")

#4 : create a random number guessing game with python

# import random
# num = random.randint(1,10)
# tries = 0
# while True:
#     guess = int(input("Enter your guess here :"))
    
#     if num == guess :
#         tries +=1
#         print("You won")
#         break
#     elif num< guess :
#         tries +=1
#         print("winning number was lower than your guess, try again")
        
#     elif num >guess :
#         tries +=1 
#         print("winning number was higer than your guess, try again")
#     else :
#         tries +=1 
#         print("sorry you are wrong , please try again")
# print(f"total guess were {tries}")

