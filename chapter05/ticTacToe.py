
the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    print_board(the_board)
    print(turn + 'の番です。どこに打つ？')
    move = input()  # プレイヤーが駒を打つ場所を取得する。 ex) mid-L, low-M...
    the_board[move] = turn  # ゲームボードを更新する。 ex) mid-Lと入力したらそのキーに対応する値にX or 0 を入力する
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'

print_board(the_board)
