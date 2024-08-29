#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    starts=10
    while starts>0:
        print(starts)
        starts-=1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    pass
    return [num**2 for num in int_list]
    

def fizzbuzz():
    # code goes here!
    pass
    nums=1
    while nums<=100:
        if(nums%3==0 and nums%5==0):
            print("FizzBuzz")
        elif(nums%5==0):
            print("Buzz")
        elif(nums%3==0):
            print("Fizz")
        else:
            print(nums)
        nums+=1

