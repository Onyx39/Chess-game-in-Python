#code tour de jeu
import chess


def tourJeu(PolyBoard, ia):

    numero_tour_joueur = 0
    askAgain = False

    if PolyBoard.mode == True:
        if not PolyBoard.isGameFinished():      
            if PolyBoard.getTurn() == PolyBoard.WHITE:
                print("C'est au tour des blancs")
                PolyBoard.askMovePieceAndMoveIt()

            else:
                print("C'est au tour des noirs")
                PolyBoard.askMovePieceAndMoveIt()

    else : 
        if not PolyBoard.isGameFinished():
            if PolyBoard.getTurn() == PolyBoard.WHITE:
                PolyBoard.askMovePieceAndMoveIt()
            else:
                ia.playMove(PolyBoard)
