import random
import os
import sys
clear=lambda: os.system('cls')
gamestart=None
while True:
    gamestart=input('Press Y to play the game, press X to exit the game! ')
    if gamestart.upper()=='Y':
        clear()
        special=None
        def moveto(k):
            global _next
            if k=='w':
                _next=[now[0]-1,now[1]]
            elif k=='s':
                _next=[now[0]+1,now[1]]
            elif k=='a':
                _next=[now[0],now[1]-1]
            elif k=='d':
                _next=[now[0],now[1]+1] 
        bl=None
        # if _next!= out:
        #     now=_next
        now=[0,0]   
        while True:
            out=[random.randint(0,3),random.randint(0,3)]
            if out!=now:
                break
        while True:
            key=[random.randint(0,3),random.randint(0,3)]
            if out!=key and key!=now:
                break
        while True:
            move=None
            for i in range(4):
                for j in range(4):

                    if [i,j]==now:
                        print('P',end='|')
                    elif [i,j]==key:
                        print('K',end='|')
                    elif [i,j]==out:
                        print('O',end='|')
                    else:
                        print('-',end='|')
                print()
            if now==out and bl:
                print('Out')
                break   
            if special:
                print("Can't go to the door without key")
            move=input("Move (w,a,s,d): ")
            clear()
            moveto(move)
            if _next!=out or bl:
                now=_next
            elif not bl:
                special=True
            if now==key:
                bl=True
                key=[None,None]
    elif gamestart.upper()=='X': 
        sys.exit()
    else:
        print('wrong input')
