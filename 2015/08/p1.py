import sys

def main():
    lines = [line.strip() for line in sys.stdin]

    total_chars = 0
    total_real = 0 
    for line in lines:
        total_chars += len(line)
        i = 0
        while i < len(line) - 1:
            if line[i] == '\\':
                if line[i+1] == 'x':
                    i += 3 
                else:
                    i += 1
                total_real += 1
            elif line[i] != '"':
                total_real += 1
            i += 1
    print total_chars - total_real

if __name__ == '__main__':
    main()
