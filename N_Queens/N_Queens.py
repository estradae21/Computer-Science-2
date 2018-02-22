from __future__ import print_function

import sys
import unittest

'''
    Ernesto Estrada
    Received help: Roach and stackoverflow 
    Given the location of two queens, find if they are safe
    from each other.
'''


def safe(one, two):
    if one[0] == two[0]:
        return False
    if one[1] == two[1]:
        return False
    if abs(two[0] - one[0]) == abs(two[1] - one[1]):
        return False
    return True


def print_solution(size, placed):
    print("for:", size)
    print(placed)
    if not placed:
        print("no solution found")
        return
    print('-' * size)

    for i in range(size):
        for j in range(size):
            if (i, j) in placed:
                sys.stdout.write("Q")
            else:
                sys.stdout.write(".")
        print()

    print('-' * size)
    print('\n Queens are safe on a board of size', size, 'X', size, 'at:\n', placed, '\n')


def safe_check(row, col, placed):
    queens_list = len(placed)
    for x in range(queens_list):
        if not safe((row, col), placed[x]):
            return False
    return True


def solve_queens(size, row, placed):
    #print("Board of size", size, ", In Row", row, ", Queens at", placed)
    if row >= size:
        #print("We're done")
        return placed

    for col in range(size):
        if safe_check(row, col, placed):
            tmp = placed + [(row, col)]
            if solve_queens(size, (row + 1), tmp,):
                return solve_queens(size, (row + 1), tmp,)
    return []


class test_queen(unittest.TestCase):
    def test_same(self):
        print("Test One")
        self.assertFalse(safe((1, 1), (1, 1)))
        if True:
            print("Passed")

    def test_same_row(self):
        print("Test Two")
        self.assertFalse(safe((1, 1), (1, 2)))
        if True:
            print("Passed")

    def test_same_column(self):
        print("Test Three")
        self.assertFalse(safe((1, 1), (2, 1)))
        if True:
            print("Passed")

    def test_same_diagonal(self):
        print("Test Four")
        self.assertFalse(safe((1, 1), (5, 5)))
        if True:
            print("Passed")

    def test_no_solution(self):
        print("Test Five")
        self.assertEqual(solve_queens(0, 0, []), [])
        self.assertEqual(solve_queens(2, 0, []), [])
        self.assertEqual(solve_queens(3, 0, []), [])
        if True:
            print("Passed")

    def test_one(self):
        print("Test Six")
        self.assertEqual(solve_queens(1, 0, []), [(0, 0)])
        if True:
            print("Passed")

    def test_four(self):
        print("Test Seven")
        self.assertEqual(solve_queens(4, 0, []), [(0, 1), (1, 3), (2, 0), (3, 2)])
        if True:
            print("Passed")

    def test_eight(self):
        print("Test Eight")
        self.assertEqual(solve_queens(8, 0, []), [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)])
        if True:
            print("Passed")

#unittest.main()

if __name__ == "__main__":
    solution = solve_queens(8, 0, [])
    print_solution(8, solution)
