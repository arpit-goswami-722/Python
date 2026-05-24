
# a = int(input("enter your number :-"))

# try:                                              # try wrap the block of code that might cause an exception , and only run when except is there 
#     print(10/a)
# except Exception as err:                          # except handles the exception if occurs
#     print(f"sorry there is an error as {err}")
# else :                                            # runs when except block dont run
#     print("there is no exception") 
# finally : 
#     print("it will run no matter what")
# print("ok i have done the division")


age = int(input("enter your age :-"))
try :
    if age<10 or age>18:
        raise ValueError("your age must be between 10 and 18")
    else : 
        print("welcome to the club")
except Exception as err:
    print(f"an error ocurred as {err}")

print("the club will strt soon")