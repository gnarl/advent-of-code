import sys
from collections import defaultdict

def main():

    
    lines = [line.strip() for line in sys.stdin]
    columns = [defaultdict(int) for x in range(0, len(lines[0]))]

    for line in lines:
        for i, c in enumerate(line):
            columns[i][c] += 1
                 
    text = ''
    for c in columns:
        # Use max for part 1 of the puzzle
        m = min(c, key=c.get)
        text += m
    print text


if __name__ == '__main__':
    main()
