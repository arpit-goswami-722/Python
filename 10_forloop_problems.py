#1 : hello world print
# n = int(input("enter n :"))
# for i in range(1,n+1,1):
#     print("Hello world")

#2 : print n numbers
# n = int(input("enter n :"))
# for i in range(1,n+1,1):
#     print(i)

#3 : print reverse
# n = int(input("enter n :"))
# for i in range(n,0,-1):
#     print(i)

#4 : table 
# n = int(input("enter n :"))
# for i in range(1,11,1):
#     print(i*n)

#5 : sum of n numbers
# sum = 0
# n = int(input("enter n :"))
# for i in range(1,n+1,1):
#     sum = sum + i
# print(f"sum is {sum}")

#6 : factorial 
# fact = 1 
# n = int(input("enter n :"))
# if n<0:
#   print("facotrial doesn't exist for negative numbers")
# elif n== 0:
#   print(f"facotrial of 0 is {fact}")
# else:
#   for i in range(1,n+1,1):
#    fact = fact*i
#   print(f"factorial of {n} is {fact}")
# 

#7 : odd and even numbers sum from n numbers
# odd_sum = 0
# even_sum =0
# n = int(input("enter n :"))
# for i in range(1,n+1,1):
#      if i%2==0:
#         even_sum = i + even_sum
#      else :
#         odd_sum = odd_sum +i
    
# print(f"even sum is {even_sum} and odd sum is {odd_sum}")

#8 : factors print
# n = int(input("enter your number to find factors :"))
# for i in range(1,n+1,1):
#     if n%i == 0:
#      print(f"{i} is a factor of {n}")

#9 : perfect number check 

# n = int(input("enter your number to check perfect number :"))
# sum = 0
# for i in range(1,n,1):
#     if n%i ==0 :
#         sum = sum+i

# if sum == n :
#     print("yes , it's a perfect number")
# else :
#     print("no , it's not a perfect number")

#10 : prime number check 

# is_prime = 1 
# n = int(input("enter the number to check prime :"))
# if n ==1 :
#  print("1 is not a prime number")
# elif n<1:
#  print("enter a number greater than 0")
# else :
#   for i in range(2,n,1):
#      if n%i == 0:
#         is_prime = 0
#         break 

#   if is_prime == 1:
#     print("yes it's a prime number")
   
#   else : print("no , it's not a prime number)

#11 : reverse strings without using in build function 
# a = "Python"
# empty_string = ""
# for i in range(len(a)-1,-1,-1):
#     empty_string = empty_string + a[i]
# print(empty_string)

#12 : check string is pallindrome or not 

# a = input("enter your string :")
# empty_string = ""
# for i in range(len(a)-1,-1,-1):
#     empty_string = empty_string + a[i]

# if empty_string == a :
#     print("yes it's a palindrome string")

# else :
#     print("no it's not a string")

#13 : count all letters , digits , and special symbols from given string 
# a = input("enter your string here :")
# alp = 0
# spchar = 0
# digits = 0
# for i in a :
#     if i.isdigit():
#         digits +=1
#     elif i.isalpha():
#         alp += 1
#     else:
#         spchar +=1 
# print(f"total alphabets are {alp}\n,special characters are {spchar}\n and total digits are {digits} in {a}")
