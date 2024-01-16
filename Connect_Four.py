# #Connect Four
import pygame 
import sys
import math

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)



row_count = 6
col_count = 7

def board_setup():
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    return board

def display_board(board):
    print("  1  2  3  4  5  6  7")
    for i in range(7):
        print(str(i + 1) + " " + board[i][0]+ " |" + board[i][1] + " |" + board[i][2] + " |" + board[i][3] + " |" + board[i][4]+ " |" + board[i][5] + " |" + board[i][6] + " |" + board[i][6]+ " |")
        if i < 7:
            print (" ----------------------")

board = board_setup()


def insert_number(board, number, col):
    for row in range(len(board)-1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = number
            return board
    return board

def check_win(board):
    # check horizontal
    for row in board:
        for i in range(len(row) - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] != ' ':
                return True
    # check vertical
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != ' ':
                return True
    # check diagonal
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != ' ':
                return True
    # check other diagonal
    for row in range(len(board) - 3):
        for col in range(3, len(board[0])):
            if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] != ' ':
                return True
    return False
 
def check_full(board):
    for row in board:
        for i in range(len(row)):
            if row[i] == ' ':
                return False
    return True

def draw_board(board):
    for col in range(col_count):
        for row in range(row_count+1):
            pygame.draw.rect(screen, BLUE, (col* SQUARESIZE, row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE)) 
    for col in range(col_count):
            for row in range(1, row_count+1):
                pygame.draw.circle(screen, BLACK, (int(col*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE/2)), radius)
    for col in range(col_count):
        for row in range(row_count+1):
            if board[row][col] == "0":
                pygame.draw.circle(screen, RED, (int(col*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE/2)), radius)
            elif board[row][col] == "1":
                pygame.draw.circle(screen, YELLOW, (int(col*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE/2)), radius)
    pygame.display.update()

            




game_over = False
turn = 0

pygame.init()
SQUARESIZE = 100
width = col_count * SQUARESIZE
height = (row_count+1) * SQUARESIZE
radius = int(SQUARESIZE/2 - 5)
size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 75)




draw_board(board)
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK,(0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED,(posx, int(SQUARESIZE/2)), radius)
            else:
                pygame.draw.circle(screen, YELLOW,(posx, int(SQUARESIZE/2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK,(0,0, width, SQUARESIZE))

            if turn == 0:
                player = "0"
                posx = event.pos[0]   

                col = int(math.floor(posx/SQUARESIZE))
                insert_number(board, player, col)
                display_board(board)
                if check_win(board) == True:
                    label = myfont.render("Red wins!",1, RED)

                    screen.blit(label, (160,20))

                    game_over = True
            else: 
                player = "1"
                posx = event.pos[0]   

                col = int(math.floor(posx/SQUARESIZE))
                insert_number(board, player, col)
                display_board(board)
                if check_win(board) == True:
                    label = myfont.render("Yellow wins!",1, YELLOW)

                    screen.blit(label, (100,20))

                    game_over = True
                

            turn += 1
            turn = turn % 2
            draw_board(board)
            if game_over == True:
                pygame.time.wait(9000)




