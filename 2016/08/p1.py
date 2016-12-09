import sys
import re

LENGTH = 50
HEIGHT = 6

def display(dis):
    for row in dis:
        print ''.join(row)
    print '_' * LENGTH

def rect(dis, wide, tall):
    for i in range(wide):
        for k in range(tall):
            dis[k][i] = '#'
    return dis

def rotate_row(dis, row_num, shifts):
    new_row = [dis[row_num][(i - shifts) % LENGTH] for i in range(LENGTH)] 
    dis[row_num] = new_row
    return dis

def rotate_column(dis, col_num, shifts):
    new_col = [dis[(i - shifts) % HEIGHT][col_num] for i in range(HEIGHT)]

    for i, x in enumerate(new_col):
        dis[i][col_num] = x 
    return dis


def main():
    dis = [['.' for _ in range(LENGTH)] for _ in range(HEIGHT)]
    
    for line in sys.stdin:

      if line.startswith('rect'):
          match = re.match(r'rect\s(\d+)x(\d+)', line.strip()) 
          dis = rect(dis, int(match.group(1)), int(match.group(2)))
      else:
          match = re.match(r'rotate\s(\w+).*=(\d+)\sby\s(\d+)', line.strip())
          dis = globals()['rotate_' + match.group(1)](dis, int(match.group(2)), int(match.group(3)))

      display(dis) 

    pix = 0
    for i in dis:
        for k in i:
            if k == '#':
                pix += 1
    print("pix: {}".format(pix))


if __name__ == '__main__':
    main()
