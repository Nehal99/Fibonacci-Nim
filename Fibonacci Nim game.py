print(" Welcome to Fibonacci Nim game! ")
    
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
         
# y is player 1

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
            print(" Player2 You Won " )
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

