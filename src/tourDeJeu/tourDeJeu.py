#code tour de jeu

def tourJeu(board):

    numero_tour_joueur = 0
    joueur_est_blanc = True
    askAgain = False

    if board.mode == True:
        if not board.isGameFinished():
            if board.getTurn() == board.WHITE:
                print("C'est au tour des blancs")
                board.move_piece()

            else:
                print("C'est au tour des noir")
                board.move_piece()

    else : 
        if joueur_est_blanc == True:
            if board.isGameFinished() == False:
                if board.getTurn() == PolyBoard.WHITE:
                    board.move_piece()
                else:
                    pass
                    #coup IA a completer


        else :
            if board.isGameFinished() == False:
                if board.getTurn() == PolyBoard.BLACK:
                    board.move_piece()
                else :
                    pass
                    # coup IA à compléter
