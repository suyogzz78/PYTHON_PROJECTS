
def sum(a,b,c):
    return a+b+c


def printboard(Xstate,Ostate):
    zero='X'if Xstate[0]==1 else 'O' if Ostate[0]==1 else 0
    one='X'if Xstate[1]==1 else 'O' if Ostate[1]==1 else 1
    two='X'if Xstate[2]==1 else 'O' if Ostate[2]==1 else 2
    three='X'if Xstate[3]==1 else 'O' if Ostate[3]==1 else 3
    four='X'if Xstate[4]==1 else 'O' if Ostate[4]==1 else 4
    five='X'if Xstate[5]==1 else 'O' if Ostate[5]==1 else 5
    six='X'if Xstate[6]==1 else 'O' if Ostate[6]==1 else 6
    seven='X'if Xstate[7]==1 else 'O' if Ostate[7]==1 else 7
    eight='X'if Xstate[8]==1 else 'O' if Ostate[8]==1 else 8

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")


def checkwinner(Xstate,Ostate):
    wins=[
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for i in wins:
        if(sum(Xstate[i[0]],Xstate[i[1]],Xstate[i[2]])==3):
            print("X wins")
            return 1
        if(sum(Ostate[i[0]],Ostate[i[1]],Ostate[i[2]])==3):
            print("O wins")
            return 0
    return -1    
    



def userinput():
    Xstate=[0,0,0,0,0,0,0,0,0]
    Ostate=[0,0,0,0,0,0,0,0,0]
    turn=1
    print("Tic Tac Toe")
    while True:
        printboard(Xstate,Ostate)
        if(turn ==1):
            print("X's turn")
            choice=int(input("Enter position(1-9): "))
            Xstate[choice]=1
        else:
            print("O's turn")
            choice=int(input("Enter position(1-9): "))
            Ostate[choice]=1
            
        chwin=checkwinner(Xstate,Ostate)
        
        if(chwin!=-1):
            print('match over')
            break
        turn= 1-turn
        

if __name__ == "__main__":
    
   userinput()