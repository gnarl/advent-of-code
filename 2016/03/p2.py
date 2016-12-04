import sys

def main():
    possible = 0 
    sides = []
    for line in sys.stdin:
        sides.append([int(x) for x in line.strip().split()])


    for index in range(0, len(sides) - 1, 3):
        triangles = [sorted(x) for x in zip(sides[index], sides[index+1], sides[index+2])] 
        for triangle in triangles:
            if (triangle[0] + triangle[1]) > triangle[2]:
                possible += 1

    print possible

if __name__ == "__main__":
    main()
