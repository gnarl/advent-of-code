import sys

MAP = { (0, 2): '1',
        (1, 1): '2', (1, 2): '3', (1, 3): '4',
        (2, 0): '5', (2, 1): '6', (2, 2): '7', (2, 3): '8', (2, 4): '9',
        (3, 1): 'A', (3, 2): 'B', (3, 3): 'C',
        (4, 2): 'D',
        } 

MOVE = { 'U': lambda row, col: (row - 1, col),
         'D': lambda row, col: (row + 1, col),
         'L': lambda row, col: (row, col - 1),
         'R': lambda row, col: (row, col + 1)
         } 


def main():
    code = []
    cur_row = 2
    cur_col = 0
    for line in sys.stdin:
        for move in line.strip():
            row, col = MOVE[move](cur_row, cur_col) 
            if (row, col) in MAP:
                cur_row, cur_col = row, col
            
            print("{} : {}".format(cur_row, cur_col))
        code.append(MAP[(cur_row, cur_col)])
    print code



if __name__ == "__main__":
    main()
