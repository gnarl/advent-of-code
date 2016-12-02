import sys

MAP = [range(1, 4), range(4, 7), range(7, 10)]

MOVE = { 'U': lambda row, col: (value(row, row - 1), col),
         'D': lambda row, col: (value(row, row + 1), col),
         'L': lambda row, col: (row, value(col, col - 1)),
         'R': lambda row, col: (row, value(col, col + 1))
         } 

def value(pre, post):
  if 0 <= post <= 2:
      return post
  return pre

def main():
    code = []
    row = 1
    col = 1
    for line in sys.stdin:
        for move in line.strip():
            row, col = MOVE[move](row, col) 
            print("{} : {}".format(row, col))
        code.append(MAP[row][col])
    print code



if __name__ == "__main__":
    main()
