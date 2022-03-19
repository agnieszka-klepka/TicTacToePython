import numpy as num
from termcolor import colored
import time
import random
from sty import fg

board = num.zeros((8,8))


M = 8
N = 8
firstCoordinate = 0
secondCoordinate = 0

# # funkcja main wyswietla kolorowy napis na terminalu
def main():
    
    print(colored("\n//         ////////    //////////  //  ///////          /////////    //           ////       //      //  ", 'blue'))
    time.sleep(0.5)
    print(colored("//         //              //         //                //      //   //          //  //       //   //    ", 'cyan'))
    time.sleep(0.5)
    print(colored("//         //////          //         ////////          ////////     //         //    //       // //     ", 'green'))
    time.sleep(0.5)
    print(colored("//         //              //               //          //           //        //////////       //       ", 'yellow'))
    time.sleep(0.5)
    print(colored("////////   /////////       //         ///////           //           //////// //        //      //       \n", 'red'))
    time.sleep(0.5)
    
    print(colored("MY FAVOURITE NUMBER - 8, SO LETS FILL THIS BOARD\n", 'cyan'))
    

if __name__ == '__main__':
    main()
    
############ PO TYM BYM CHCIAŁA, BY UZYTKOWNIK KLIKNAL ENTER DO NASTEPNEJ FAZY GRY

# funkcje generujace kolory na terminal, za pomoca funkcji random - zmieniaja sie 
def generateRGB():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red, green, blue

def generateColour(red, green, blue):
    return fg(red, green, blue)
    
red, green, blue = generateRGB()
colour = generateColour(red, green, blue)

# poczatkowy wyglad planszy
def showFirstBoard():
    for i in range(M):
        for j in range(N):
            board[i][j] = 0
    
    # board[M-1][N-1] = '7'
            
    # print(colored(board, 'blue'))  
    # print(colored('randomowe kolory', 'cyan'))
    
    print(colour, board)    #plansza zmienia kolory po kazdym wywołaniu

showFirstBoard()

# funkcja opisujaca warunek zakonczenia gry
def victoriaCondition(board):
    
    counter = 0
    for i in range(M):
        for j in range(N):
            if board[i][j] == 8:
                counter = counter + 1       
    
    if counter == 64:
        print("YOU WON")
        return             

# funkcja okreslajaca, jak zmieniaja sie wartosci na planszy w zaleznosci od wspolrzednych podanych przez uzytkownika
def gameRules(firstCoordinate, secondCoordinate):
    
    if board[firstCoordinate-1][secondCoordinate-1] == 0:   # srodkowa wspolrzedna
        board[firstCoordinate-1][secondCoordinate-1] = 8
    else:
        board[firstCoordinate-1][secondCoordinate-1] = 0
    
    if board[firstCoordinate-1][secondCoordinate-2] == 0 and secondCoordinate != 1:    # wspolrzedna na lewo
        board[firstCoordinate-1][secondCoordinate-2] = 8
    else:
        board[firstCoordinate-1][secondCoordinate-2] = 0
        
    if secondCoordinate != 8 and board[firstCoordinate-1][secondCoordinate] == 0:     # wspolrzedna na prawo
        board[firstCoordinate-1][secondCoordinate] = 8
    elif secondCoordinate != 8 and board[firstCoordinate-1][secondCoordinate] == 8:
        board[firstCoordinate-1][secondCoordinate] = 0
    
    if firstCoordinate != 8 and board[firstCoordinate][secondCoordinate-1] == 0:     # wspolrzedna dolna
        board[firstCoordinate][secondCoordinate-1] = 8
    elif firstCoordinate != 8 and board[firstCoordinate][secondCoordinate-1] == 8:
        board[firstCoordinate][secondCoordinate-1] = 0
     
    if board[firstCoordinate-2][secondCoordinate-1] == 0 and firstCoordinate != 1:       # wspolrzedna gorna
        board[firstCoordinate-2][secondCoordinate-1] = 8
    else:
        board[firstCoordinate-2][secondCoordinate-1] = 0
        
    print(board)
    victoriaCondition(board)
    getNumberFromUser()
    
############ TE FUNKCJE MOZNA ZMODYFIKOWAC, BY STRZALKAMI WYBIERAC MIEJSCE STAWIANIA KRZYZYKA

# uzytkownik podaje liczbe rzedu i kolummy, w ktorej chce postawic krzyzyk
def getNumberFromUser():
    
    firstCoordinate = int(input('choose number of rows: '))
    if(firstCoordinate < 9 and firstCoordinate > 0): 
        print(firstCoordinate)  
    else:
        print("wrong number")
        return
        
    secondCoordinate = int(input('choose number of column:'))
    if(secondCoordinate < 9 and secondCoordinate > 0): 
        print(secondCoordinate)
    else:
        print("wrong number")
        return 
    
    gameRules(firstCoordinate, secondCoordinate)   
getNumberFromUser()
