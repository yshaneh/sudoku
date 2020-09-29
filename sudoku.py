#!/usr/bin/python3

import matrix as sudoku_matrix
from os import system, name
from time import sleep


def clone(matrix):
    return [x.copy() for x in matrix]

def clear():
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 


def check(matrix, x, y, n):
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


def get_all_options(matrix, x, y):
    return [n for n in range(1,10) if check(matrix, x, y, n)]

def check_done(matrix):
    for arr in matrix:
        if 0 in arr:
            return False
    return True


def show(matrix, time=0):
    clear()
    print_matrix(matrix)
    if time > 0:
        sleep(time)

def solve_one(matrix, display=False):
    matrix = clone(matrix)
    flag = True
    while flag:
        flag = False
        for x in range(9):
            for y in range(9):
                opts = get_all_options(matrix, x, y)
                if len(opts) == 1:
                    flag = True
                    matrix[x][y] = opts[0]
                    show(matrix, 0.2)
                    
    return matrix


def solve_brute(matrix, display=False):
    matrix = clone(matrix)
    for x in range(9):
        for y in range(9):
            if matrix[x][y] == 0:
                for n in get_all_options(matrix, x ,y):
                    matrix[x][y] = n
                    show(matrix)
                    # print(x, y)
                    result = solve(matrix)
                    if check_done(result):
                        return result
                    matrix[x][y] = 0
    return matrix


def solve(matrix, display=False):
    matrix = clone(matrix)
    return solve_brute(solve_one(matrix, display), display)

def replaced(arr, original, changed):
    arr = arr.copy()
    for i, n in enumerate(arr):
        if n == original:
            arr[i] = changed
    return arr

def print_matrix(matrix):
    n=35
    line_end = "\n " + "-"*n + " \n"
    line_middle = "\n|" + "-"*n + "|\n"
    print(line_end + line_middle.join(["| " + " | ".join(map(str, replaced(x, 0, " "))) + " |" for x in matrix]) + line_end)


def main():
    mt = sudoku_matrix.matrix3
    show(mt, 2)
    solved = solve(mt)
    sleep(0.3)
    clear()
    print("original:\n\n")
    print_matrix(mt)
    print("\n\nsolved:\n\n")
    print_matrix(solved)
    # print("variable:\n\n")
    # print_matrix(mt)

if __name__ == "__main__":
    main()
