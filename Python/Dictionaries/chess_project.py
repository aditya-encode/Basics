import copy,sys
starting_pieces={'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

board_template="""
  a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = '||'
BLACK_SQUARE = '  '

def chess_board(board):
    square=[]
    is_white_square=True
    for y in "87654321":
        for x in "abcdefgh":
            if x+y in board.keys():
                square.append(board[x+y])
            else:
                if is_white_square:
                    square.append(WHITE_SQUARE)
                else:
                    square.append(BLACK_SQUARE)
            is_white_square=not is_white_square
        is_white_square= not is_white_square
    print(board_template.format(*square))
  
def isValidChessBoard(board):
    black_king=0
    white_king=0

    white_pawns=0
    black_pawns=0

    white_pieces=0
    black_pieces=0

    for i,j in board.items():
        if i[0] not in 'abcdefgh' or i[1] not in '12345678':
            return False   
        if  j[0] not in ['w','b'] or j[1] not in ['R','Q','K','P','B','N']:
            return False
        if j[0]=='w':
            white_pieces +=1
        if j[0]=='b':
            black_pieces+=1
        
        if j[0]=='w' and j[1]=="K":
            white_king +=1
        
        if j[0]=='b' and j[1]=="K":
            black_king +=1
        
        if j[0]=='w' and j[1]=="P":
            white_pawns +=1
        if j[0]=='b' and j[1]=="P":
            black_pawns +=1

    if white_king!=1 or black_king!=1:
            return False
    if white_pieces>16 or black_pieces>16:
            return False
    
    if white_pawns>8 or black_pawns>8:
            return False
    return True




def p_help():
    print('Interactive Chess Board')
    print('by Al Sweigart al@inventwithpython.com')
    print()
    print('Pieces:')
    print('  w - White, b - Black')
    print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
    print('Commands:')
    print('  move e2 e4 - Moves the piece at e2 to e4.')
    print('  remove e2 - Removes the piece at e2.')
    print('  set e2 wP - Sets square e2 to a white pawn.')
    print('  reset - Reset pieces back to their starting squares.')
    print('  clear - Clear the entire board.')
    print('  fill wP - Fill entire board with white pawns.')
    print('  help - Show this help information.')
    print('  quit - Quits the program.')

main_board=copy.copy(starting_pieces)
p_help()
while True:
    chess_board(main_board)
    response=input(">>>").split()
    if len(response) == 0:
        continue
    print(isValidChessBoard(main_board))

    if response[0]=="move":
        main_board[response[2]]=main_board[response[1]]
        del main_board[response[1]]
    elif response[0]=='remove':
        del main_board[response[1]]
    elif response[0]=='set':
        main_board[response[1]]=response[2] 
    elif response[0]=='reset':
        main_board=copy.copy(starting_pieces) 
    elif response[0]=="clear":
        main_board={}
    elif response[0]== "fill":
        for y in "87654321": 
            for x in "abcdefgh":
                main_board[x+y]=response[1]
    elif response[0]=="help":
        p_help()
    elif response[0]=="quit":
        sys.exit()