if __name__ == '__main__':
    fname = "test.txt"
    #fname = "input.txt"
    file = open(fname)

    counter = 0
    guardX = 0
    guardY = 0
    dir = 'N'
    map = []
    for line in file:
        temp = []
        for i in range(len(line)):
            if(line[i] != '\n'):
                temp.append(line[i])
                if line[i] == "^":
                    (guardX, guardY) = (i, counter)
        map.append(temp)

        counter += 1
    for line in map:
        print(line)

    print("\n\n")

    map[guardY][guardX] = 'X'
    done = False
    counter = 1
    while(not done):
        if(dir == 'N'):
            if(guardY == 0):
                done = True
            else:
                if(map[guardY - 1][guardX] == '#'):
                    dir = 'E'
                else:
                    guardY -= 1
        elif(dir == 'E'):
            if(guardX == len(map[0]) - 1):
                done = True
            else:
                if(map[guardY][guardX + 1] == '#'):
                    dir = 'S'
                else:
                    guardX += 1
                    if(map[guardY][guardX] != 'X'):
                        counter += 1
                        map[guardY][guardX] = 'X'
        elif(dir == 'S'):
            if(guardY == len(map) - 1):
                done = True
            else:
                if(map[guardY + 1][guardX] == '#'):
                    dir = 'W'
                else:
                    guardY += 1
        elif(dir == 'W'):
            if(guardX == 0):
                done = True
            else:
                if(map[guardY][guardX-1] == '#'):
                    dir = 'N'
                else:
                    guardX -= 1

        if(map[guardY][guardX] != 'X'):
            counter += 1
            map[guardY][guardX] = 'X'

    for line in map:
        print(line)
    print(f"\n{counter}")
    