#!/usr/bin/python3

import matrix as sudoku_matrix
from os import system, name
from time import sleep
import colorama

class Sudoku:


    def __init__(self, matrix):
        self.matrix = matrix
        self.str_matrix = [self.replaced(list(map(str, x)), "0", " ") for x in matrix]

    def clone(self, matrix):
        return [x.copy() for x in matrix]

    def clear(self):
        if name == 'nt': 
            system('cls') 
        else: 
            system('clear') 


    def check(self, matrix, x, y, n):
        if matrix[x][y] != 0:
            return False

        for i in range(9):
            # print("i:", i, ", x:", x, ", y:", y, ", n:", n, ", result:", matrix[i][y] == n or matrix[x][i] == n)
            if matrix[i][y] == n or matrix[x][i] == n:
                    return False

        x = x//3
        y = y//3

        for ax in range(3):
            for ay in range(3):
                # print("i:", i, ", x:", x, ", ax", ax, ", y:", y, ", ay", ay, ", n:", n, ", result:", matrix[x*3+ax][y*3+ay] == n)
                if matrix[x*3+ax][y*3+ay] == n:
                    return False
        return True


    def get_all_options(self, matrix, x, y):
        return [n for n in range(1,10) if self.check(matrix, x, y, n)]

    def solve_one(self, matrix, display=False):
        cloned_matrix = self.clone(matrix)
        flag = True
        while flag:
            flag = False
            for x in range(9):
                for y in range(9):
                    opts = self.get_all_options(cloned_matrix, x, y)
                    if len(opts) == 1:
                        flag = True
                        cloned_matrix[x][y] = opts[0]
                        self.str_matrix[x][y] = colorama.Fore.GREEN + str(opts[0]) + colorama.Style.RESET_ALL

                        if display:
                            self.show(self.str_matrix, 0.2)
        return cloned_matrix

    def show(self, matrix, time=0):
        self.clear()
        self.print_matrix(matrix)
        if time > 0:
            sleep(time)


    def solve_brute(self, matrix, display=False):
        cloned_matrix = self.clone(matrix)
        for x in range(9):
            for y in range(9):
                if cloned_matrix[x][y] == 0:
                    for n in self.get_all_options(matrix, x ,y):
                        cloned_matrix[x][y] = n
                        self.str_matrix[x][y] = colorama.Fore.YELLOW + str(n) + colorama.Style.RESET_ALL
                        if display:
                            self.show(self.str_matrix, 0.01)
                        # print(x, y)
                        result = self.solve_brute(cloned_matrix, display)
                        if self.check_done(result):
                            return result
                        cloned_matrix[x][y] = 0
                        self.str_matrix[x][y] = " "
        return cloned_matrix

    def solve_sudoku(self, matrix, display=False):
        return self.solve_brute(self.solve_one(matrix, display), display)


    def solve(self, display=False):
        cloned_matrix = self.clone(self.matrix)
        return self.solve_sudoku(cloned_matrix, display)

    def replaced(self, arr, original, changed):
        arr = arr.copy()
        for i, n in enumerate(arr):
            if n == original:
                arr[i] = changed
        return arr

    def print_matrix(self, matrix):
        n=35
        line_end = "\n " + "-"*n + " \n"
        line_middle = "\n|" + "-"*n + "|\n"
        print(line_end + line_middle.join(["| " + " | ".join(map(str, self.replaced(x, 0, " "))) + " |" for x in matrix]) + line_end)


def main():
    sudoku = Sudoku(sudoku_matrix.matrix3)
    sudoku.show(sudoku.matrix, 2)
    solved = sudoku.solve(True)
    sleep(2)
    sudoku.clear()
    print("original:\n\n")
    sudoku.print_matrix(sudoku.matrix)
    print("\n\nsolved:\n\n")
    sudoku.print_matrix(solved)
    # print("variable:\n\n")
    # print_matrix(mt)

if __name__ == "__main__":
    main()
