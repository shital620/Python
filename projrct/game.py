import random
r=random.randint(1,20)
while(True):
    inp=int(input())
    if(inp<r):
        print("wrong guess ,try a greather number ")
        
    elif(inp>r):
        print("wwrong guess, try a small number ")
    else:
        print("congrates ,you have guessed the number")
        break;
    