number = [1,3,2,5,72,21]
number.append(10) #add 10 to the end
number.insert(3,15) #insert 15 at index 3
number.extend([3,2,5.5]) #add multiple numbers at the end 
number.remove(3) #remove 3 , first one will be removed
popped_item = number.pop(3) #number removed from index 3 and will be stored in the popped_item variable
print(popped_item)
count_5 = number.count(2) #counts occurence of an element 
print(count_5)
number.sort() #sorts in ascending order 
print(number)
number.reverse() # reverse the list elements 
print(number)
new_numbers = number.copy() # creates a copy of the list
print(new_numbers)
number.clear() # removes all the elements of the list 
print(number)
