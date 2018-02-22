from __future__ import print_function
import unittest

TRACE=True
count = 0

moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

def is_safe(width, height, new_x, new_y, placed):
    if [new_x, new_y] in placed:
        return False
    if new_x > width or new_x < 1:
        return False
    if new_y > height or new_y < 1:
        return False
    return True


def solve(width, height, row, column, placed):
    global count
    if TRACE: print('width:', width)
    if TRACE: print('height:', height)
    if TRACE: print('row:', row)
    if TRACE: print('column:', column)
    if TRACE: print('placed:', placed)
    # print(count)
    count += 1

    # if this is the last one, we know it's safe so just add it and return
    if len(placed) == width*height-1:
        return placed + [[row, column]]

    for move in moves:
        new_x = row+move[0]
        new_y = column+move[1]
        if is_safe(width, height, new_x, new_y, placed):
            tmp = solve(width, height, new_x, new_y, placed + [[row, column]])
            if tmp:
                return tmp

    return []

if __name__ == "__main__":
    # 3x4, 4x5,
    width = 5
    height = 5
    for i in range(1, width+1):
        for j in range(1, height+1):
            solution = solve(width, height, i, j, [])
            if solution:
                print (count)
                print(solution)