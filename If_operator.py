## name = input("What is your name: ")
#if len(name) < 3:
 #   print("name must be atleast 3 characters")
#elif len(name) > 50:
 #   print("name should not increase 50 characters")
#else:
 #   print("cool")
#print(len(name))

import main


Weight= int(input("weight: "))
units= input("(l)bs or (k)gs: ")
if units.upper() == "L":
    print ( f" you are {Weight / 2.25}kgs")
elif units.upper() == "K":
    print ( f" you are {Weight * 2.25}lbs")

if __name__ == '__main__':
    main.W_in_pounds = 90
    print (main.result)