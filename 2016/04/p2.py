import sys 

def main():

    # regex = re.compile(r"([a-z,-]+)-(\d+)\[(\w+)\]")

    lines = [line.strip() for line in sys.stdin]
    data = []
    for line in lines:
        k = line.rfind('-') 
        data.append((line[:k], line[k + 1:]))

    c = 'abcdefghijklmnopqrstuvwxyz' 
    for d in data:
        word = ""
        for letter in d[0]:
            if letter != '-':
                k = c.find(letter)
                steps = int(d[1]) % 26
                for step in range(0, steps):
                    if k == 25:
                        k = 0
                    else:
                        k += 1
                word = word + c[k] 
            else:
                word = word + ' '
        print("{} - {}".format(word, d[1]))



if __name__ == "__main__":
    main()
