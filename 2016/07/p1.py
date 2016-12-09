import sys

def check(line, i):
    if (line[i] == line[i+3] and
        line[i+1] == line[i+2] and
        line[i] != line[i+1]):
        print(line[i:(i+4)]) 
        return True
    return False


def main():

    lines = [line.strip() for line in sys.stdin]
    support_tls = 0
    for line in lines:
        i = 0
        line_len = len(line)
        fence = False
        supported = False
        while i < line_len:
            if (i + 3) < line_len:
                found = check(line, i)
                if found and fence:
                    supported = False
                    print("False: {}".format(line[i:(i+4)])) 
                    break
                elif found:
                    supported = True
                    print("True: {}".format(line[i:(i+4)])) 

            if line[i] == '[':
                fence = True
            elif line[i] == ']':
                fence = False 


            i += 1
        print("supported: {}".format(supported))
        if supported:
            support_tls += 1

    print support_tls

        




if __name__ == '__main__':
    main()
