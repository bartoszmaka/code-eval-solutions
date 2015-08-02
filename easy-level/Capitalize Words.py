__author__ = 'Monek'

file = open("Capitalize Words.txt")
for line in file:
    words = line.split()
    words = [list(word) for word in words]

    for i in range(len(words)):
        words[i][0] = (words[i][0].upper())
        print("".join(words[i]), end=" ")
    else:
        print()
file.close()
