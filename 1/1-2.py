if __name__ == '__main__':
    fname = "input.txt"
    list1 = []
    list2 = []

    file = open(fname)
    for line in file:
        line = line.strip().split(" ")
        toAdd1 = int(line[0])
        toAdd2 = int(line[3])
        
        if(len(list1) == 0):
            list1.append(int(toAdd1))
            list2.append(int(toAdd2))

        else:
            if(list1[len(list1) - 1] < toAdd1):
                list1.append(toAdd1)
            else:
                added = False
                for i in range(len(list1)):
                    if(not added):
                        if(list1[i] >= toAdd1):
                            list1.append(0)
                            for j in range(len(list1) - 2, i-1, -1):
                                list1[j+1] = list1[j]
                            list1[i] = toAdd1
                            added = True
            
            if(list2[len(list2) - 1] < toAdd2):
                list2.append(toAdd2)
            else:
                added = False
                for i in range(len(list2)):
                    if(not added):
                        if(list2[i] >= toAdd2):
                            list2.append(0)
                            for j in range(len(list2) - 2, i-1, -1):
                                list2[j+1] = list2[j]
                            list2[i] = toAdd2
                            added = True
    score = 0
    pointer = 0
    count = 0
    for i in range(len(list1)):
        if(i > 0 and list1[i] == list1[i-1]):
            score += list1[i] * count
        else:
            count = 0
            while(pointer < len(list2) and list2[pointer] <= list1[i]):
                if(list2[pointer] == list1[i]):
                    count += 1
                pointer += 1
            score += list1[i] * count

    print(score)