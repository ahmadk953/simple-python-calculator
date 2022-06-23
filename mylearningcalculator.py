from asyncore import ExitNow
import math
import random
doover = True
print("Welcome to the calculator!")
print("We will do all operation on numbers.")
while doover == True:
    input1 = int(input("What is the first number you want to do the operations on:"))
    input2 = int(input("What is the second number you want to do the operations on:"))
    print("Starting...")
    x = input1#random.randint(0, 600)
    y = input2#random.randint(0, 1600)
    print(f"Number 1: '{x}'")
    print(f"Number 2: '{y}'")
    print(f"Adding: '{x+y}'")
    print(f"Dividing y by x: '{y/x}'")
    print(f"Dividing '{x}' by '{y}': '{x/y}'")
    print(f"Subtracting '{y}' by '{x}': '{y-x}'")
    print(f"Subtracting '{x}' by '{y}': '{x-y}'")
    print(f"Multiplying: '{x*y}'")
    print("Do you want to do any more calculations?")
    repeat = input("Please answer yes or no:")
    if repeat == "yes":
        doover = True
    if repeat == "no":
        doover = False
        print("Setting variables back to default values...")
        x = 0
        y = 0
        print(f"x = '{x}'")
        print(f"y = '{y}'")
        print("All done! Finished.")
        ExitNow
#print("Done with round 1. Starting round 2...")
#x=random.randint(0, 120)
#y=random.randint(0, 1120)
#print(x)
#print(y)
#print(x+y)
#print(y/x)
#print(y-x)
#print(y+x)
#print(y*x)
#print("Done with round 2. Starting round 3...")
#x=random.randint(0, 19865)
#y=random.randint(0, 1000600)
#print(x)
#print(y)
#print(x+y)
#print(y/x)
#print(y-x)
#print(y+x)
#print(y*x)
#print("Done with round 3. Starting find area...")
#l=random.randint(1, 100)
#w=random.randint(1, 150)
#a=l * w
#print("The area is:", a)
#print("Finished with round 1, 2, 3, and find area. Cleaning up...")
#print("Setting variables back to default values...")
#print("The default value for all of the variables should be 1")
#x = 1
#y = 1
#l=1
#w=1
#a=1
#print(x)
#print(y)
#print(l)
#print(w)
#print(a)
#if x == y:
#    print("All done! Finished.")
#else:
#    print("Error. Default values of the variables should be 1 but the default vales are bigger/smaller than 1.")
#    print("Please contact the developer at ahmad.khan@outoforgedu.team and give them the error code listed bellow.")
#    error_code=100
#    print("error code:", error_code)
#ExitNow