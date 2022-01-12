def choixMode(): # a faire ici ? 
    choix_mode = ''
    while choix_mode != 'y' and choix_mode != 'n' :
        print('Etes vous deux joueurs ? y/n')
        choix_mode = input()
        clearConsole = lambda: print('\n' * 25)
        clearConsole()
        if choix_mode == 'y' :
            mode_jcj = True 
        elif choix_mode == 'n' : 
            mode_jcj = False
    return mode_jcj
