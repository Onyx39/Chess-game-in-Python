#code tour de jeu

import chess

from affichagePiecesPrises.affichage_prises import AffichagePiecesPrises, TransformationenMatrice


def tourJeu(board, pieces_noires_prises, pieces_blanches_prises):

    numero_tour_joueur = 0
    askAgain = False

    if board.mode == True:
        if not board.isGameFinished():      
            if board.getTurn() == board.WHITE:
                print("C'est au tour des blancs")
                board.move_piece(pieces_noires_prises, pieces_blanches_prises)

            else:
                print("C'est au tour des noirs")
                board.move_piece(pieces_noires_prises, pieces_blanches_prises)

    else : 
        if board.getTurn() == board.WHITE:
            if board.isGameFinished() == False:
                board.move_piece(pieces_noires_prises, pieces_blanches_prises)
            else:
                pass
                    #coup IA a completer


        else :
            if board.isGameFinished() == False:
                if board.getTurn() == board.BLACK:
                    board.move_piece(pieces_noires_prises, pieces_blanches_prises)
                else :
                    pass
                    # coup IA à compléter
    '''
    p = AffichagePiecesPrises(board, coup, TransformationenMatrice(board), board.getTurn())
    print(p)
    if p != None :
        if board.getTurn() == board.WHITE:
            print("les blancs ont prit une piece")
        elif board.getTurn() == board.BLACK:
            print("les noirs ont prit une piece")
    '''