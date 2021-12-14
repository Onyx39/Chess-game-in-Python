

import chess

if 'name' == '__main__' :

    board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
    print(board)
    numero_tour_joueur = 0
    coup_joueur_blanc = None
    coup_joueur_noir = None


    while board.is_checkmate() == False :
    
        if numero_tour_joueur%2 == 0 :
            print("C'est au tour des blancs")
            input(coup_joueur_blanc)
            board.push(coup_joueur_blanc)
        else : 
            print("C'est au tour des noir")
            input(coup_joueur_noir)
            board.push(coup_joueur_noir)

        i = i+1

    if i % 2 == 1 :
        print('victoire du joueur noir')
    else  :
        print('victoire du joueur blanc')



    
