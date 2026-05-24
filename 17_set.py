# mutable , not a duplicate , unordered , semi heterogenous (can store some data types like string , numbers , tuples but not everything)

s = {1,2,4.5,True,"ok",'hello'}
# print(s)

# b = hash("ok who are you")
# print(b) # hash value , diff everytime that's why no correct index availcable

# # traversing in set :
for i in s:
    print(i)

# # set methods :
# s.add(4) # add an element
# print(s)
# s.remove("hello") # removes an element (error if not found)
# print(s)
# s.discard(4) # removes an element (no error if not found)
# print(s)
# popped_element = s.pop() # removes a random element 
# print(popped_element)
# print(s)
# s.clear() # removes all elements
# print(s)

#some set operations :
# a = {1,2,3,4,5,6}
# b = {1,2,5,7,9,8,4}
# union_set = a.union(b)
# u = a | b
# print(u)
# intersection_set = a.intersection(b)
# i = a&b
# print(i)
# difference_set = a.difference(b)
# d = a-b
# print(d)
# symmetric_diff = a.symmetric_difference(b)
# sd = a^b
# print(sd)