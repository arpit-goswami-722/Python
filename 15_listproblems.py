# #1 : print positve and negative elements of a list
# l = [1,-2,3,0,5.6,-6.7]
# print("positive elements are :")
# for i in l :
#     if i >= 0:
#         print(i)
# print("negative elements are :")   
# for i in l :
#     if i < 0:
#         print(i)

# #2 : mean of list elements :
# l = [1, 2, -4 , 7.7 , 5]
# sum = 0
# for i in l :
#     sum = sum + i
# mean = sum/len(l)
# print(f"mean is {mean}")

#3 : find the greatest element and print its index too :
# l = [12,35,65,-78,67.4,678,9,789]
# comp = l[0]
# second_greatest = l[0]
# index = 0
# for i in range(len(l)) :
#     if comp < l[i]:
#         second_greatest = comp
#         comp = l[i]
#         index = i
#     elif second_greatest <i :
#         second_greatest = i
# print(f"greatest element is {comp} and index is {index}")
# print(f"second greatest is {second_greatest}")

#4 : check if the list is sorted or not :
# l = [1,2,3,4,5]
# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else :
#         print("list is not sorted")
#         break
# else : print("your list is sorted")    
