
# these are explicit conversions , here we use in build functions like int() , float() , str() , bool()
# when coverting to boolean , following things gave false : 0 , 0.0 , False , "" , [] , {} , ()

"""a = 5
a = str(a)
print(type(a))"""

"""b = 'string value'
b = int(b)
print(type(b))""" #----> cannot chnage , b shud contain an numerical value 

"""c = '12'
c = int(c)
print(type(c))"""

# implicit conversions : these conversions are automatically done by python 

a = 12
print(12/3) # automatically converted in 4.0
