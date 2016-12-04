import sys

def main():
    possible = 0 
    for line in sys.stdin:
        sides = sorted([int(x) for x in line.strip().split()])
        if (sides[0] + sides[1]) > sides[2]:
            possible += 1
    print possible

if __name__ == "__main__":
    main()
