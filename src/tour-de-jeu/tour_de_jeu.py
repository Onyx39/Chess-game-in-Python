

import chess
#code tour de jeu


if __name__ == '__main__' :

    board = chess.Board()
    print(board)
    numero_tour_joueur = 0
    coup_joueur_blanc = None
    coup_joueur_noir = None
    mode_jcj = 0
    joueur_est_blanc = 1
    coup_joueur = None
    choix_mode = None
    i = 0

    while choix_mode != 'y' and choix_mode != 'n' :
        print('Etes vous deux joueurs ? y/n')
        choix_mode = input()
        if choix_mode == 'y' :
            mode_jcj = 1 
        elif choix_mode == 'n' : 
            mode_jcj = 0



    if mode_jcj == 1 :
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
            print('victoire du joueur blanc')
        else  :
            print('victoire du joueur noir')

    else :
        if joueur_est_blanc == 1 :
            
            while board.is_checkmate() == False :
    
                if numero_tour_joueur%2 == 0 :
                    print("A votre tour")
                    input(coup_joueur)
                    board.push(coup_joueur)
                else : 
                    pass
                    #coup IA a completer
                

                i = i+1

            if i % 2 == 1 :
                print('victoire du joueur blanc')
            else  :
                print('victoire du joueur noir')
        else :
            while board.is_checkmate() == False :

                if numero_tour_joueur%2 == 1 :
                    print ("A votre tour")
                    input(coup_joueur)
                    board.push(coup_joueur)
                else :
                    pass
                    # coup IA à compléter

        



    
