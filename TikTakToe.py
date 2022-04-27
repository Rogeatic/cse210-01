def main():
    startList = [1,2,3,4,5,6,7,8,9]
    moves_list = [1,2,3,4,5,6,7,8,9]
    playerPicker = True
    gameOver = False

    printTikTac(moves_list)

#TRYS UNTIL SOMEONE WINS OR FULL
    while(not gameOver):
        #SWITCHES BETWEEN PLAYERS
        if(playerPicker):
            playerXO = 'X'
        else:
            playerXO = 'O'
        #GETS THE INPUT FROM THE PLAYER AND CHANGES LIST VALUE ENTERED TO PLAYER NAME X or O
        getIn = int(input(f"{playerXO}'s turn to choose a square (1-9): "))
        moves_list[getIn - 1] = playerXO
        #PRINTS THE NEW TIK TAC TOE BOARD
        printTikTac(moves_list)
        
        #CHECKS IF ANYONE GOT A ROW AND WON
        if(
            #HORIZONTAL
            moves_list[0] == moves_list[1] == moves_list[2] or 
            moves_list[3] == moves_list[4] == moves_list[5] or 
            moves_list[6] == moves_list[7] == moves_list[8] or 
            #VERTICAL
            moves_list[0] == moves_list[3] == moves_list[6] or 
            moves_list[1] == moves_list[4] == moves_list[7] or 
            moves_list[2] == moves_list[5] == moves_list[8] or 
            #DIAGONAL
            moves_list[0] == moves_list[4] == moves_list[8] or 
            moves_list[2] == moves_list[4] == moves_list[6] 
            ): 
            gameOver = True
            print(f"GOOD JOB {playerXO}, YOU WON!")
            
        #ENDS THE GAME IF ANY VALUE IS NOT AN INT
        else:
            gameOver = True
            for num in moves_list:
                if num in startList:
                    gameOver = False
            if(gameOver):
                print("CAT'S GAME, NOBODY WON!")

        #SWITCHES PLAYER
        playerPicker = not playerPicker
        
def printTikTac(moves_list):
    #PRINTS THE NEW TIK TAC TOE BOARD
    print(f"\n{moves_list[0]}|{moves_list[1]}|{moves_list[2]}\n-+-+-\n\
{moves_list[3]}|{moves_list[4]}|{moves_list[5]}\n-+-+-\n\
{moves_list[6]}|{moves_list[7]}|{moves_list[8]}")





main()
