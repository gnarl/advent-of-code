import sys 
import re
import collections

def main():

    regex = re.compile(r"([a-z,-]+)-(\d+)\[(\w+)\]")


    lines = [line.strip() for line in sys.stdin]
    data = []
    for line in lines:
        match = re.search(regex, line)
        data.append((match.group(1), match.group(2), match.group(3)))

    real = 0
    ids = 0
    for d in data:
        counts = count(d[0])
        if counts == d[2]:
            print("{}-{}").format(d[0], d[1]) 
            real += 1
            ids += int(d[1])
    print real
    print ids 


# Could have used Counter in collections but wanted to do it myself
def count(word):
    counts = {}
    for letter in word.replace('-', ''):
        counts[letter] = counts.get(letter, 0) + 1
    result = ""
    # print counts
    while len(counts) > 0:
        largest = ['z', None]
        for key in counts:
            if ((counts[key] > largest[1]) or 
               ((counts[key] == largest[1]) and (key < largest[0]))):
                largest[0] = key
                largest[1] = counts[key]
                # print("{} > {} : {} < {}".format(counts[key], largest[1], key, largest[0]))
        counts.pop(largest[0], None)
        # print counts
        # print("{} : {}".format(largest[0], largest[1]))
        result = result + str(largest[0])
    return result[0:5]

if __name__ == "__main__":
    main()
