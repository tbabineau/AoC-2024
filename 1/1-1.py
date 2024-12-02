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

    totDist = 0
    for i in range(len(list1)):
        dist = list1[i] - list2[i]
        if(dist < 0):
            dist *= -1
        totDist += dist
    
    print(totDist)