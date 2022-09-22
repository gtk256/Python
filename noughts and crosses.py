while True:
    choice=input("Would you like to start? \n Type 'y' or 'n':  ")
    if choice=='y':
        player='cross'
        marker='x'
        nmarker='o'
        break
    elif choice=='n':
        player='nought'
        marker='o'
        nmarker='x'
        break 
    else:
        print("Incorrect input, please try again")

moves=[1, 2, 3, 4, 5, 6, 7, 8, 9]
human=[]
comp=[]

s1 = "                                    " '\n'
s2 = "  ----------------------------------" '\n'
s3 = "  |          |          |          |" '\n'
s4 = "  |     1    |    2     |     3    |" '\n'
s5 = "  |          |          |          |" '\n'
s6 = "  ----------------------------------" '\n'
s7 = "  |          |          |          |" '\n'
s8 = "  |     4    |    5     |     6    |" '\n'
s9 = "  |          |          |          |" '\n'
s10 = "  ----------------------------------" '\n'
s11 = "  |          |          |          |" '\n'
s12 = "  |     7    |    8     |     9    |" '\n'
s13 = "  |          |          |          |" '\n'
s14 = "  ----------------------------------" '\n'
print(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14)



def grid(board):
    global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14
    p1 = "                                    " '\n'
    p2 = "  ----------------------------------" '\n'
    p3 = "  |          |          |          |" '\n'
    p4 = "  |      "+board[1]+"   |    "+board[2]+"     |     "+board[3]+"    |" '\n'
    p5 = "  |          |          |          |" '\n'
    p6 = "  ----------------------------------" '\n'
    p7 = "  |          |          |          |" '\n'
    p8 = "  |      "+board[4]+"   |    "+board[5]+"     |     "+board[6]+"    |" '\n'
    p9 = "  |          |          |          |" '\n'
    p10 = "  ----------------------------------" '\n'
    p11 = "  |          |          |          |" '\n'
    p12 = "  |      "+board[7]+"   |    "+board[8]+"     |     "+board[9]+"    |" '\n'
    p13 = "  |          |          |          |" '\n'
    p14 = "  ----------------------------------" '\n'
    print(p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14)

testing_board=[" "]*10


def handle_turn_player(board,marker,position):
    board[position]=marker


if player=='nought':
    print("Computer's first move:")
    handle_turn_player(testing_board,"x",5)
    grid(testing_board)
    moves.remove(5)
    comp.append(5)
def turn():
    print("Where would you like your " + player + "?")
    go=int(input("Enter position: "+ str(moves) + ": "))
    if go in moves:
        handle_turn_player(testing_board,marker,int(go))
        grid(testing_board)
        moves.remove(go)
        human.append(go)
        h1=[1,2,3]
        h2=[4,5,6]
        h3=[7,8,9]
        h4=[1,4,7]
        h5=[2,5,8]
        h6=[3,6,9]
        h7=[1,5,9]
        h8=[3,5,7]
        if (all(i in human for i in h1)):
            print("THE HUMAN HAS WON! :(")
            exit()
        if (all(i in human for i in h2)):
            print("THE HUMAN HAS WON! :(")
            exit()
        if (all(i in human for i in h3)):
            print("THE HUMAN HAS WON! :(")
            exit()
        if (all(i in human for i in h4)):
            print("THE HUMAN HAS WON! :(")
            exit()
        if (all(i in human for i in h5)):
            print("THE HUMAN HAS WON! :(")
            exit()
        if (all(i in human for i in h6)):
            print("THE HUMAN HAS WON! :(")
            exit()
        if (all(i in human for i in h7)):
            print("THE HUMAN HAS WON! :(")
            exit()
        if (all(i in human for i in h8)):
            print("THE HUMAN HAS WON! :(")
            exit()

        
def comp_turn():
    import random 
    comp_go=random.choice(moves)
    print(comp_go)
    if comp_go in moves:
        handle_turn_player(testing_board,nmarker,int(comp_go))
        grid(testing_board)
        moves.remove(comp_go)
        comp.append(comp_go)
        c1=[1,2,3]
        c2=[4,5,6]
        c3=[7,8,9]
        c4=[1,4,7]
        c5=[2,5,8]
        c6=[3,6,9]
        c7=[1,5,9]
        c8=[3,5,7]
        if (all(i in comp for i in c1)):
            print("THIS DAY BELONGS TO THE MACHINE!")
            exit()
        if (all(i in comp for i in c2)):
            print("THIS DAY BELONGS TO THE MACHINE!")
            exit()
        if (all(i in comp for i in c3)):
            print("THIS DAY BELONGS TO THE MACHINE!")
            exit()
        if (all(i in comp for i in c4)):
            print("THIS DAY BELONGS TO THE MACHINE!")
            exit()
        if (all(i in comp for i in c5)):
            print("THIS DAY BELONGS TO THE MACHINE!")
            exit()
        if (all(i in comp for i in c6)):
            print("THIS DAY BELONGS TO THE MACHINE!")
            exit()
        if (all(i in comp for i in c7)):
            print("THIS DAY BELONGS TO THE MACHINE!")
            exit()
        if (all(i in comp for i in c8)):
            print("THIS DAY BELONGS TO THE MACHINE!")
            exit()
    




turn()
comp_turn()
turn()
comp_turn()
turn()
comp_turn()
turn()
comp_turn()
turn()


    
