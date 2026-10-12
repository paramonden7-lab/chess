board = [['.' for x in range(8)] for j in range(8)]
letter_field = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
what_white = {"\u265C", "\u265E", "\u265D", "\u265B", "\u265A", '\u265F'}
what_black = {'\u2656', '\u2658', '\u2657', '\u2655', '\u2654', '\u2659'}
xod = True
letters_map = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
letters_map2 = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
chess_white = ["\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"] # шахматы ладья и тд
chess_black = ['\u2656', '\u2658', '\u2657', '\u2655', '\u2654', '\u2657', '\u2658', '\u2656'] # шахматы ладья и тд
board[1] = ['\u2659' for i in range(8)]# пешки черные
board[6] = ['\u265F' for i in range(8)]# пешки белые 
board[0] = chess_black
board[7] = chess_white
while True: 
    print('  a b c d e f g h')
    for row in range(len(board)):
        print(row + 1, end=' ')
        for cell in range(8):
            if (row + cell + 2) % 2 == 0 and board[row][cell] == '.':
                print('.', end= ' ')
            elif board[row][cell] == '.':
                print('#', end=' ')
            else:
                print(board[row][cell], end=' ')
        print()
    if xod == True:
        turn = input('\n\n Ход белых \n Укажите адрес ячейки для выбора фигуры\n> ')
        x, y = turn[0], turn[1]
        cell = letters_map.get(x)
        row = int(y) - 1
        if board[row][cell] not in what_white:
            print('ti lox')
        else:
            xodi = {}
            match board[row][cell]:
                case '\u265F': # пешка
                    if row == 6 and board[4][cell] not in what_white and board[4][cell] not in what_black:
                        xodi.update({f'{x}{row - 1}':[cell, row - 2], f'{x}{row}':[cell, row - 1]})
                    elif board[row - 1][cell] not in what_white and board[row - 1][cell] not in what_black:
                        xodi.update({f'{x}{row}':[cell, row - 1]})
                    else:
                        print('Нет доступных ходов')
                        continue
                case "\u265C": # ладья
                    for j in range(row - 1, - 1, - 1):
                        if board[j][cell] in what_white:
                            break
                        elif board[j][cell] in what_black:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                            break
                        else:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                    for j in range(row + 1, 8, 1):
                        if board[j][cell] in what_white:
                            break
                        elif board[j][cell] in what_black:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                            break
                        else:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                    for i in range(cell - 1, -1, -1):
                        if board[row][i] in what_white:
                                break
                        elif board[row][i] in what_black:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                            
                            break
                        else:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                    for i in range(cell + 1, 8, 1):
                        if board[row][i] in what_white:
                            break
                        elif board[row][i] in what_black:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                            break
                        else:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                case '\u265D': # СЛОН
                    i, j = row - 1, cell - 1
                    while i > -1 and j > -1:
                        if board[i][j] in what_white:
                            break
                        elif board[i][j] in what_black:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                            break
                        else:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                        i -= 1
                        j -= 1
                    i, j = row + 1, cell + 1
                    while i < 8 and j < 8:
                        if board[i][j] in what_white:
                            break
                        elif board[i][j] in what_black:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                            break
                        else:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                        i += 1
                        j += 1
                    i, j = row - 1, cell + 1
                    while i > -1 and j < 8:
                        if board[i][j] in what_white:
                            break
                        elif board[i][j] in what_black:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                            break
                        else:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                        i -= 1
                        j += 1
                    i, j = row + 1, cell - 1
                    while i < 8 and j > -1:
                        if board[i][j] in what_white:
                            break
                        elif board[i][j] in what_black:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                            break
                        else:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                        i += 1
                        j -= 1
                case '\u265E': # коняра
                    xodi_kon = [
                        (-2, -1),
                        (-2, 1),
                        (2, -1),
                        (2, 1),
                        (-1, -2),
                        (-1, 2),
                        (1, -2),
                        (1, 2),
                    ]
                    for u in xodi_kon:
                        i, j = row + u[0], cell + u[1]
                        if - 1 >= i or - 1 >= j or 8 <= i or 8 <= j:
                            continue
                        if board[i][j] in what_white:
                            continue
                        else:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                case '\u265B': # ферзила
                    for j in range(row - 1, - 1, - 1):
                        if board[j][cell] in what_white:
                            break
                        elif board[j][cell] in what_black:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                            break
                        else:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                    for j in range(row + 1, 8, 1):
                        if board[j][cell] in what_white:
                            break
                        elif board[j][cell] in what_black:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                            break
                        else:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                    for i in range(cell - 1, -1, -1):
                        if board[row][i] in what_white:
                                break
                        elif board[row][i] in what_black:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})  
                            break
                        else:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                    for i in range(cell + 1, 8, 1):
                        if board[row][i] in what_white:
                            break
                        elif board[row][i] in what_black:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                            break
                        else:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                    i, j = row - 1, cell - 1
                    while i > -1 and j > -1:
                        if board[i][j] in what_white:
                            break
                        elif board[i][j] in what_black:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                            break
                        else:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                        i -= 1
                        j -= 1
                    i, j = row + 1, cell + 1
                    while i < 8 and j < 8:
                        if board[i][j] in what_white:
                            break
                        elif board[i][j] in what_black:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                            break
                        else:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                        i += 1
                        j += 1
                    i, j = row - 1, cell + 1
                    while i > -1 and j < 8:
                        if board[i][j] in what_white:
                            break
                        elif board[i][j] in what_black:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                            break
                        else:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                        i -= 1
                        j += 1
                    i, j = row + 1, cell - 1
                    while i < 8 and j > -1:
                        if board[i][j] in what_white:
                            break
                        elif board[i][j] in what_black:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                            break
                        else:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})
                        i += 1
                        j -= 1
                case '\u265A': # oldking
                    xodi_kon = [
                        (0, -1),
                        (-1, 0),
                        (1, 0),
                        (0, 1),
                        (-1, -1),
                        (-1, 1),
                        (1, -1),
                        (1, 1),
                    ]
                    for u in xodi_kon:
                        i, j = row + u[0], cell + u[1]
                        if - 1 >= i or - 1 >= j or 8 <= i or 8 <= j:
                            continue
                        if board[i][j] in what_white:
                            continue
                        else:
                            xodi.update({f'{letters_map2[j]}{i + 1}':[j, i]})   
    # if m in xodi:
    #         xod = False
    # else:
    #         print("ход черных")
        if len(xodi) == 0:
            print('Ходов нет')
            continue
        numbers = 1
        for k in xodi:
            print(f'{numbers}. {k}')
            numbers += 1
        m = input('Ваш ход: ')
        if m not in xodi:
            while True:
                m = input('Неправильно введи еще раз: ')
                if m in xodi:
                    break
        p = xodi.get(m)
        board[p[1]][p[0]] = board[row][cell]
        board[row][cell] = '.'
        if m in xodi:
            xod = False
    if xod == False:
        turn = input('\n\n Ход черных \n Укажите адрес ячейки для выбора фигуры\n> ')
        x, y = turn[0], turn[1]
        cell = letters_map.get(x)
        row = int(y) - 1
        if board[row][cell] not in what_black:
            print('ti lox')
        else:
            xodi = {}
            match board[row][cell]:
                case '\u2659': # пешка
                    if row == 1 and board[3][cell] not in what_black and board[3][cell] not in what_white:
                        xodi.update({f'{x}{row + 1}':[cell, row + 2], f'{x}{row}':[cell, row + 1]})
                    elif board[row + 1][cell] not in what_white and board[row + 1][cell] not in what_black:
                        xodi.update({f'{x}{row}':[cell, row + 1]})
                    else:
                        print('Нет доступных ходов')
                        continue
                case "\u265C": # ладья
                    for j in range(row - 1, - 1, - 1):
                        if board[j][cell] in what_white:
                            break
                        elif board[j][cell] in what_black:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                            break
                        else:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                    for j in range(row + 1, 8, 1):
                        if board[j][cell] in what_white:
                            break
                        elif board[j][cell] in what_black:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                            break
                        else:
                            xodi.update({f'{x}{j + 1}':[cell, j]})
                    for i in range(cell - 1, -1, -1):
                        if board[row][i] in what_white:
                                break
                        elif board[row][i] in what_black:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                            
                            break
                        else:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                    for i in range(cell + 1, 8, 1):
                        if board[row][i] in what_white:
                            break
                        elif board[row][i] in what_black:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                            break
                        else:
                            xodi.update({f'{letters_map2[i]}{y}':[i, row]})
                        if len(xodi) == 0:
                            print('Ходов нет')
                            continue
        numbers = 1
        for k in xodi:
            print(f'{numbers}. {k}')
            numbers += 1
        m = input('Ваш ход: ')
        if m not in xodi:
            while True:
                m = input('Неправильно введи еще раз: ')
                if m in xodi:
                    break
        p = xodi.get(m)
        board[p[1]][p[0]] = board[row][cell]
        board[row][cell] = '.'


        xod == True








        # 1. каждая шашечка ходит по своему: пешка ходит только прямо на одну клетку, когда делает первый ход на 2 клетки. 
        # 2. ладья ходит по горизонтали и вертикали на любое расстояние
        # 3. слоняра ходит по диагонали на любое расстояние
        # 4. конь ходит на 2 клетки вперед/назад/влево/право и на 1 вправо/влево/вверх/вниз, перепрыгивает через фигуры
        # 5. король ходит на одну клетку в любую сторону
        # 6. ферзь ходит на любое расстояние по вертикали горизонтали и диагонали
        # 7. фигуры не могут выйти за рамки
        # 8.ход начинается с белых, и далее по очереди
        # 9. пешка бьет по диагонали
