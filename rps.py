import random
x = int(input("how many times you want to play"))
cc=0
uc=0
while x>0:
    v = input("choose for ROCK(R/r) or PAPER(P/p) or sCISSIORS(S/s)")
    if v == 'R' or v == 'r':
        u = 1
    elif v == 'P' or v == 'p':
        u = 2
    elif v == 'S' or v == 's':
        u = 3
    else:
        print("invalid input")
        continue
    c = random.randint(1,3)
    if (u,c) == (3,1) or (u,c) == (1,2) or (u,c) == (2,3):
        cc = cc + 1
        print("I WON! this round, my throw is ", c, " your throw is ", u )
    elif (u,c) == (1,3) or (u,c) == (2,1) or (u,c) == (3,2):
        uc = uc + 1
        print("YOU WON! this round, my throw is ", c, " your throw is ", u )
    else:
        print("this round is a DRAW!, my throw is ", c, " your throw is ", u )
    x = x - 1
if cc > uc:
    print("I WON THE MATCH by " + str(cc-uc) + "points")
elif uc > cc:
    print(" YO!! YOU WON THE MATCH by " + str(uc-cc) + "points")
else:
    print("DRAW MATCH, " + str(uc) + "scored by both")
