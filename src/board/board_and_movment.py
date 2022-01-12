import chess
from choixMode.choixMode import choixMode
<<<<<<< HEAD
=======
from evalBar.evalBar import Eval
>>>>>>> main
import tourDeJeu.tourDeJeu as tdj

class PolyBoard:

    def __init__(self):
        self.board = chess.Board()
        #board de base : chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        self.printBanner()
        self.mode = choixMode()
        self.WHITE = chess.WHITE
        self.BLACK = chess.BLACK
<<<<<<< HEAD
=======

        self.eval = Eval()
>>>>>>> main


    def traduction(self, string): #pas besoin de str-ify une str
        if string == "1" :
            return str('.')
        if string == "2" :
            return str('. .')
        if string == "3" :
            return str('. . .')
        if string == "4" :
            return str('. . . .')
        if string == "5" :
            return str('. . . . .')
        if string == "6" :
            return str('. . . . . .')
        if string == "7" :
            return str('. . . . . . .')
        if string == "8" :
            return str('. . . . . . . .')
        else : return string


    def affichage_plateau(self):
        copie = self.board.epd()
        compteur = 0
        ch = ""
        #print("    A B C D E F G H ")
        print("   ___________________")
        print("  |                   |")
        for j in copie :
            if j != "/" :
                ch += self.traduction(j) + " "
            else : 
                print(8 - compteur, '| ', ch, '|', 8 - compteur)
                compteur += 1
                ch = ""
        print("1", '| ', ch[0:16], '|', "1")
        print("  |___________________|")
        print("     A B C D E F G H")
      

    def detect_echec(self):
        if self.board.is_checkmate() == False and self.board.is_check() == True:
            print('Echec')
            return self.endGame()
        elif self.board.is_checkmate() == True:
            print('Echec et Mat')
            return self.endGame()
        elif self.board.is_stalemate():
            print('Pat !')
            return self.endGame()

                 
    def ask_move_piece(self):
        #ask to move a piece and returns it once the move is legal
        print("enter a move, please (undo to undo)")
        askAgain = False
        coup = "0000"
        try:
            while(chess.Move.from_uci(coup) not in self.board.legal_moves): #NOTE maybe put it in another func, moveDetect ?
                if askAgain: 
                    print("Ce coup n'est pas valide ! \n les coups valides sont : ")
                    print(self.board.legal_moves)
                coup = input()
                askAgain = True
                if coup == "undo" and self.board.fullmove_number > 1: return "undo"
        except ValueError: #hacky way to do things, but it works
            print("Ce coup n'est pas valide ! \n recommencez : ")
            return self.ask_move_piece()
        return coup


    def move_piece(self):
        #x est du type "'case de départ' 'case d'arrivée'" (ex: 'e2e3' bouge la piece de e2 à e3)
        #pour roque, il suffit de bouger le roi sur la case ou est presente une tou 
        coup = self.ask_move_piece()
        if coup == "undo": self.coup_precedent()
        self.board.push_san(coup)
        self.detect_echec()


    def coup_precedent(self):
        self.board.pop()
        print(self.affichage_plateau())
        self.detect_echec()

           
    def endGame(self):
        term = self.board.outcome().winner
        if term: term = "blancs"
        elif term: term = "noirs"
        elif term == None: return print("Pat ! GG WP !")
        return print(f"Les {term} ont gagnés ! GGWP !")


    def getTurn(self):
        return self.board.turn

    def printBoard(self):
        self.affichage_plateau()

    def isGameFinished(self): 
        if self.board.outcome() == None: return False
        return True

    def playGame(self):
        while not self.isGameFinished():
            assert self.board.is_valid()
            self.affichage_plateau()
            tdj.tourJeu(self)
            self.printBoard()
            tdj.tourJeu(self)
            self.eval.update(self.board)


    def printBanner(self):
        print("")
        print("     ██████╗  ██████╗ ██╗     ██╗   ██╗ ██████╗██╗  ██╗███████╗███████╗███████╗")
        print("     ██╔══██╗██╔═══██╗██║     ╚██╗ ██╔╝██╔════╝██║  ██║██╔════╝██╔════╝██╔════╝")
        print("     ██████╔╝██║   ██║██║      ╚████╔╝ ██║     ███████║█████╗  ███████╗███████╗")
        print("     ██╔═══╝ ██║   ██║██║       ╚██╔╝  ██║     ██╔══██║██╔══╝  ╚════██║╚════██║")
        print("     ██║     ╚██████╔╝███████╗   ██║   ╚██████╗██║  ██║███████╗███████║███████║")
        print("     ╚═╝      ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝")
        print("Bienvenue !")
            

    '''def mvt_possible(self, str):
        self.board.find_move(from_square: chess.str)
        print(affichage_plateau(self.board))
        detect_echec()'''
