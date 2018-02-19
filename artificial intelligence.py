import random
import math

print(" Welcome to Fibonacci Nim game!")

print(" Enter 1 for One player , Enter 2 for two players " )
# a is the user choice
while True:
    try:
        a=int(input("Your Choice : " ))
    except Exception as e:
        print (" Please Choose 1 or 2 ")
        continue
    break

# x is the number of coins

while True:
    try:
        x=int(input("Enter coins number : " ))
    except Exception as e:
        print (" You should choose an integer number ")
        continue
    break

while x<=1:
    print(" You should choose a number greater than 1 ")
    while True:
        try:
            x=int(input("Please enter another coins number : " ))
        except Exception as e:
            print (" You should choose an integer number ")
            continue
        break
if a==1:
    
# y is player 

    while True:
        try:
            y=int(input("Choose a number: "))
        except Exception as e:
            print (" You should choose an integer number ")
            continue
        break

    while y>= x or y<=0 :
                print(" you should choose less than coins number but not zero or negative! ")
                while True:
                    try:
                        y=int(input("Please choose another number: "))
                    except Exception as e:
                        print (" You should choose an integer number ")
                        continue
                    break          
    x-=y
    print(" New coins number = " ,x)

    while x>0:
    # Computer's turn
            def fib(x):
                if x == 1:
                    return 1
                else:
                    return fib(x-1) + fib(x-2)
            z=random.randrange(1 ,((2*y)+1))
            
            while z>x : 
                z=random.randrange(z<x ,((2*y)+1))
            
            print(" Computer Choose Number: ",z)
                
            x-=z
            print(" New coins number = ",x)
            if x==0: 
                print(" Computer is Won " )
                break                          
            
            while True:
                try:
                    y=int(input("Player1 please choose a number: "))
                except Exception as e:
                    print (" You should choose an integer number ")
                    continue
                break
        
            while y>(2*z )or y>x or y<=0:
                print(" You should choose a number with max player2's double and less than new coins number but not zero or negative!")

                while True:
                    try:
                        y=int(input("Player1 please choose a number: "))
                    except Exception as e:
                        print (" You should choose an integer number ")
                        continue
                    break
        
            x-=y
            print( " New coins number = ",x)
            
            if x==0:
                print(" Player1 You Won ")
                break
    print (" End Game ")
if a==2:
    while True:
        try:
            y=int(input("Player1 please choose a number: "))
        except Exception as e:
            print (" You should choose an integer number ")
            continue
        break

    while y>= x or y<=0 :
        print(" you should choose less than coins number but not zero or negative! ")
        while True:
            try:
                y=int(input("Player1 please choose another number: "))
            except Exception as e:
                print (" You should choose an integer number ")
                continue
            break          
    x-=y
    print(" New coins number = " ,x)
    # z is player 2 
    while x>0:
        while True:
            try:
                 z=int(input("Player2 please choose a number: "))
            except Exception as e:
                 print (" You should choose an integer number")
                 continue
            break
       
        
        while z>(2*y )or z>x or z<=0 :
            print(" You should choose a number with max player1's double and less than new coins number but not zero or negative!")

            while True:
                try:
                     z=int(input("Player2 please choose a number: "))
                except Exception as e:
                     print (" You should choose an integer number")
                     continue
                break
                          
        x-=z
        
        print(" New coins number = ",x)
        if x==0: 
            print("Player2 You Won " )
            break
        
        while True:
            try:
                y=int(input("Player1 please choose a number: "))
            except Exception as e:
                print (" You should choose an integer number ")
                continue
            break
    
        while y>(2*z )or y>x or y<=0:
            print(" You should choose a number with max player2's double and less than new coins number but not zero or negative!")

            while True:
                try:
                    y=int(input("Player1 please choose a number: "))
                except Exception as e:
                    print (" You should choose an integer number ")
                    continue
                break
    
        x-=y
        print( " New coins number = ",x)
        
        if x==0:
            print("Player1 You Won ")
            break
    print (" End Game ")
