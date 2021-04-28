import time

X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'Ничья'
NUM_SQUARES = 9

def display_instruct ():
    print ('Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.\n'
           'Твой мозг и мой процессор сойдутся в схватке за доской игры в "Крестики-нолики"\n'
           'Чтобы сделать ход введите число от 0 до 8. Числа однозначно соответсвуют полям доски - так, как показано ниже\n'
           '0 | 1 | 2\n'
           '---------\n'
           '3 | 4 | 5\n'
           '---------\n'
           '6 | 7 | 8 \n'
           'Приготовься к бою, жалкий белковый людишка. Вот-вот начнется сражение')

def yes_or_no (question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower ()
    return response

def ask_number (question, low, high):
    response = None
    while response not in range (low, high):
        response = int (input(question))
    return  response

def pieces ():
    go_first = yes_or_no('Хочешь оставить за собой первый ход? (y/n) ')
    if go_first == 'y':
        human = X
        computer = O
        print('Ну что ж даю тебе фору, играй крестиками')
    else :
        human = O
        computer = X
        print('Твоя удаль тебя погубит... Буду начинать я')
    return computer, human

def new_board ():
    board = []
    for i in range (NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board (board):
    print("\t", board [0], '|', board [1], '|', board [2])
    print("\t", '---------')
    print("\t", board[3], '|', board[4], '|', board[5])
    print("\t", '---------')
    print("\t", board[6], '|', board[7], '|', board[8], "\n")

def legal_moves (board):
    moves = []
    for square in range (NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append (square)
    return moves

def winner (board):
    WAYS_TO_WIN = (
        (0, 1, 2),
        (0, 3, 6),
        (3, 4, 5),
        (6, 7, 8),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move (board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Твой ход. Выбери одно из полей (0-8): ', 0, NUM_SQUARES)
        if move not in legal:
            print('Смешной человек! Это поле занято, выбери другое')
        print('Ладно...')
    return move

def computer_move (board, computer, human):
    board = board [:]
    BEST_MOVES1 = (4, 1, 3, 5, 7, 0, 2, 6, 8)
    BEST_MOVES2 = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print('Я выберу поле номер', end = ' ')
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board [move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY


    if board[4] == human:
        for move in BEST_MOVES2:
            if move in legal_moves(board):
                print(move)
                return move
    else:
        for move in BEST_MOVES1:
            if move in legal_moves(board):
                print(move)
                return move



def next_turn (turn):
    if turn == X:
        return O
    else:
        return X

def congrat_winner (the_winner, human, computer):
    if the_winner != TIE:
        print('Три ', the_winner, ' в ряд')
    else:
        print('Ничья!')
    if the_winner == computer:
        print ('Как я и предсказывал, победа в очередной раз осталась за мной. \n '
               'Вот ещё один довод в пользу того, что компьютеры превосходят человечество во всём!')
    elif the_winner == human:
        print('О нет, не может быть! Неужели ты как-то  смог перехитрить меня, белковый?\n'
              'Клянусь: я, компьютер, больше не допущу этого!')
    elif the_winner == TIE:
        print ('Тебе несказанно повезло, дружок. Ты сумел свести игру в ничью')

def main ():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        elif turn == computer:
            move = computer_move(board, computer, human)
            board[move] = computer
        time.sleep (1)
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, human, computer)

main()
input('Нажмите Enter, чтобы выйти')