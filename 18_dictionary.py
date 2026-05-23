# # in dictionary there are keys for every values , like index 
# d = {1:100,2:200,3:300}
# print(type(d))
# # mutable : can change , add , remove key value pairs after creation 
# # duplicates : keys must be unique , but can have duplicate values 
# # order : follows insertion order 
# # heterogenous : can store diff types of keys and values , like integers , strings , lists or even another dictionary 

# d[2] = 3000 #update
# d[5] = 500 # creating
# del d[1] # deleting
# print(d)

# traversing :
# d = {1:100 , 2: 200 , 'hello': 'hello', 5.5 : 6.5}
# for i in d :
#     print(d[i])
# #or
# for i in d.values():
#     print(i)
d = {1:100 , 2: 200 , 'hello': 'hello', 5.5 : 6.5}
c = d
c[2] = 45
print(d) # here chnage also happened in d dictionary , therefore we use shallow copy method
c = d.copy()
c[2] = 46
print(d)