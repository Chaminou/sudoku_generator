
import numpy as np
import os
import random
import time
import argparse

class Board :
    def __init__(self, board) :
        self.board = board

    def print(self) :
        os.system("clear")
        for i in range(9) :
            line = ""
            for j in range(9) :
                line += str(self.board[i][j])
                if (j+1)%3 == 0 and j != 8:
                    line += " | "
                else :
                    line += " "
            print(line)
            if (i+1)%3 == 0 and i != 8:
                print("------+-------+------")
        print()

    def row_set(self, row) :
        my_set = set()
        for i in range(9) :
            current_nb = self.board[row][i]
            if current_nb != 0 :
                my_set.add(current_nb)
        return my_set

    def column_set(self, column) :
        my_set = set()
        for i in range(9) :
            current_nb = self.board[i][column]
            if current_nb != 0 :
                my_set.add(current_nb)
        return my_set

    def square_set(self, row, column) :
        my_set = set()
        n = row//3
        m = column//3
        for i in range(n*3, n*3 + 3) :
            for j in range(m*3, m*3 + 3) :
                current_nb = self.board[i][j]
                if current_nb != 0 :
                    my_set.add(current_nb)
        return my_set

    def possibilities(self, row, column) :
        return set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - (self.square_set(row, column) | self.column_set(column) | self.row_set(row))

    def element_generator(self, indice) : # 0 <= indice <= 80
        if indice <= 80 :
            row = indice // 9
            column = indice % 9
            self.board[row][column] = random.sample(self.possibilities(row, column), 1)[0]
            self.element_generator(indice+1)


if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description='Generate random sudokus')
    parser.add_argument('-s', dest='seed', default=None, help='a string seed')
    arg = parser.parse_args()

    if arg.seed == None :
        random.seed(time.time())
    else :
        random.seed(arg.seed)

    grille = np.zeros((9, 9), dtype=int)
    while True :
        try :
            board = Board(grille.copy())
            board.element_generator(0)
            board.print()
            break
        except :
            pass
