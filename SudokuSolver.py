row, col = 9, 9
inf = 10**9

board = [0 for _ in range(row)]


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y


start = [[Pair(-1, -1) for _ in range(row)] for _ in range(col)]


def calulate_start_cells():
    for i in range(0, row, 3):
        for j in range(0, col, 3):
            for k in range(i, i + 3, 1):
                for l in range(j, j + 3, 1):
                    start[k][l] = Pair(i, j)


def get_available_options(cr, cc):
    cnt = {}
    options = []
    for i in range(row):
        cnt[board[i][cc]] = cnt.get(board[i][cc], 0) + 1
    for i in range(col):
        cnt[board[cr][i]] = cnt.get(board[cr][i], 0) + 1

    p = start[cr][cc]

    for k in range(p.x, p.x + 3, 1):
        for l in range(p.y, p.y + 3, 1):
            cnt[board[k][l]] = cnt.get(board[k][l], 0) + 1

    for val in range(1, 10, 1):
        if cnt.get(val, 0) == 0:
            options.append(val)
    return options


def is_conflict():
    for i in range(row):
        cnt = {}
        for j in range(col):
            cnt[board[i][j]] = cnt.get(board[i][j], 0) + 1
            if board[i][j] != 0 and cnt.get(board[i][j], 0) > 1:
                return True
    for i in range(col):
        cnt.clear()
        for j in range(row):
            cnt[board[j][i]] = cnt.get(board[j][i], 0) + 1
            if board[j][i] != 0 and cnt.get(board[j][i], 0) > 1:
                return True
    for i in range(0, row, 3):
        for j in range(0, col, 3):
            cnt.clear()
            for k in range(i, i + 3, 1):
                for l in range(j, j + 3, 1):
                    cnt[board[k][l]] = cnt.get(board[k][l], 0) + 1
                    if board[k][l] != 0 and cnt.get(board[k][l], 0) > 1:
                        return True
    return False


def get_the_best_cell():
    p = Pair(-1, -1)
    mn = inf
    for i in range(row):
        for j in range(col):
            if board[i][j] != 0:
                continue
            options = get_available_options(i, j)
            if len(options) < mn:
                mn = len(options)
                p = Pair(i, j)
    return p


def can_solve_sudoku(empty_cell):
    if empty_cell == 0:
        return is_conflict() == False

    can = False

    p = get_the_best_cell()
    if p.x == -1 and p.y == -1:
        return True

    if board[p.x][p.y] != 0:
        can |= can_solve_sudoku(empty_cell)
    else:
        options = get_available_options(p.x, p.y)
        for val in options:
            board[p.x][p.y] = val
            can |= can_solve_sudoku(empty_cell - 1)
            if can == True:
                break
            else:
                board[p.x][p.y] = 0
    return can


def main():
    calulate_start_cells()
    for i in range(row):
        board[i] = input().split()

    empty_cell = 0
    for i in range(row):
        for j in range(col):
            board[i][j] = int(board[i][j])
            if board[i][j] == 0:
                empty_cell += 1

    if can_solve_sudoku(empty_cell):
        print('Solution Exists!')
        for i in range(row):
            for j in range(col):
                print(board[i][j], end=' ' if j != col - 1 else ' ')
            print()
    else:
        print('No Solution')


if __name__ == '__main__':
    main()