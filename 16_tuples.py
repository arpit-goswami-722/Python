# immutable : cannot change value of tuple
#duplicates : can have duplicate values 
# ordered : can access them through index value 
# hetrogenous : can have diff types of data

t = (1,2,3,5.5 ,True ,5,4)
# print(t)
# print(t[4])

# # traversing :
# for i in t :
#     print(i)
# for i in range(len(t)):
#     print(t[i])

#methods :
index = t.index(5.5) # for finding index 
print(index)

count_5 = t.count(5)
print(count_5) #for finding number of occurrence of an element