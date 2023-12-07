import random

comp=['S', 'W', 'G']
ran=random.choice(comp)
winList=[['S','W'], ['W','G'],['G','S']]
drawList=[['S','S'], ['W','W'],['G','G']]

def play():
    inp=input("Select S, W or G    ").capitalize()

    if inp not in ('S', 'W', 'G'):
        print("invalid input, pls", end=" ")
        play()

    else:
        ## computer value
        print("You chose", inp)
        print("Computer chose", ran)
        myList=[inp,ran]
        # print(myList)
        if myList in winList:
            print("you won")
        elif myList in drawList:
            print("draw")
        else:
            print("you lost")
    

play()
while True:
    retry=int(input("select 0 to quit, 1 to play again  "))
    if retry==1:
        play()
    else:
        break

