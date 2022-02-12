import random
import numpy as np
import os
from time import sleep

# Waiting for 1 seconds to clear the screen
sleep(1)

# Clearing the Screen
# posix is os name for linux or mac
if(os.name == 'posix'):
   os.system('clear')
# else screen will be cleared for windows
else:
   os.system('cls')

#Sets up the board with zeros and the no of rows and column's to be n
n = 3
l = np.zeros(shape=(n,n),dtype = int)

print(''' 
1 | 2| 3
__ __ __
4 | 5| 6
__ __ __
7 | 8| 9''')

#Sets the initial state of game to running
game = True

#Sets intial turn to be the algorithms
turn_of_alg = True
turn = 0 

#Check's if the game has ended
def state(x):
    global game
    if (x[0][0] == x[1][1]) and (x[1][1] == x[2][2]) and x[0][0]!=0: ##Checks prependiculars
        #print("Hell")
        game = False
        return x[0][1]

    if x[0][2] == x[1][1] and x[1][1] == x[2][0] and x[2][0]!=0:
        #print("Naw")
        game = False
        return x[0][1]
    
    for k in range(n):
        if (x[k][0] == x[k][1] and x[k][2] == x[k][1]) and x[k][0]!=0:
            game = False
            return x[k][k]
            #print("Hi")
        elif (x[0][k] == x[1][k] and x[2][k] == x[1][k]) and x[0][k]!=0:
            game = False
            return x[k][k]
            #print("Hello")

    return None

def out(x):
    global turn_of_alg
    if turn_of_alg is False:
        print('_________')
        print()
        for na in range(5):
            if (na%2==0):
                z = int(na / 2)
                for ma in range(5):
                    if (ma%2==0):
                            k = int(ma / 2)
                            print(x[z][k],end =' ')
                    else:
                        print('|',end=' ')
                print()
            else:
                print('__ __ __')
        print()
        print('_________')


#Algorithm to win 
def check(x,y,play,do = True):
    if l[x][y] != 0:
        if do == True:
            print("Invalid move by player:",play)
        if l[x][y] == play:
            return [False,True]
        else:
            return [False,False]
    else:
        if do == True:
            l[x][y] = play
        return [True,False]

corn = True
def alg(l):
    global turn_of_alg,turn,corn
    print("The current alg turn is:",turn)
    print("the corner is",corn)
    if turn == 0:
        x , y = 0,0
    elif turn == 1:
        if check(2,2,1,False)[0] is True:
            x,y = 2,2
        else:
            corn = False
            x,y = 2,0
    elif turn == 2:
        if corn == True:
            if check(1,1,1,False)[0] is True:
                x,y = 1,1
            elif check(2,0,1,False)[0] is True:
                x,y = 2,0
            elif check(0,2,1,False)[0] is True:
                x,y = 0,2
        else:
            if check(1,0,1,False)[0] is True:
                x,y = 1,0
            elif check(0,2,1,False)[0] is True:
                x,y = 0,2
    elif turn == 3:
        if corn == True:
            if check(0,2,1,False)[0] is True:
                x,y = 0,2
            elif check(1,2,1,False)[0] is True:
                x,y = 1,2
            elif check(2,1,1,False)[0] is True:
                x,y = 2,1
        else:
            if check(0,2,1,False)[0] is True:
                x,y = 0,2
            elif check(1,1,1,False)[0] is True:
                x,y = 1,1
    elif turn == 4:
        if check(0,1,1,False)[0] is True:
            x,y = 0,1
        elif check(1,1,1,False) is True:
            x,y = 1,1
    turn += 1
    return [x,y]

#Takes input from user

def inp(l):
    global turn_of_alg,turn   
    if turn_of_alg == True:
        za = alg(l)
        x,y = za[0],za[1]
        if check(x,y,1)[0] is False:
            inp(l) 
        turn_of_alg = False
    else:
        a = input("Please enter the cell number:")
        if a == "q":
            quit()
        xaw = int(a)
        x,y = 0,0
        if xaw == 1:
            x,y = 0,0
        elif xaw == 2:
            x,y = 0,1
        elif xaw == 3:
            x,y = 0,2
        elif xaw == 4:
            x,y = 1,0
        elif xaw == 5:
            x,y = 1,1
        elif xaw == 6:
            x,y = 1,2
        elif xaw == 7:
            x,y = 2,0
        elif xaw == 8:
            x,y = 2,1
        elif xaw == 9:
            x,y = 2,2
        if check(x,y,2)[0] is True:
            turn_of_alg = True
    
#Main Game loop


while game == True:
    inp(l)
    out(l)
    z = state(l)
    print(z)
out(l)
print("And the winner is:",state(l))