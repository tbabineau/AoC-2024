def checkLine(line, first):
    delta = int(line[0]) - int(line[1])
    if(delta < 0):
        delta *= -1
    if(delta < 1 or delta > 3):
        if(first):
            line1 = line.copy()
            line1.remove(line[0])
            line2 = line.copy()
            line2.remove(line[1])
            return (checkLine(line1, False) or checkLine(line2, False))
        else:
            return False
    if(int(line[0]) < int(line[1])):
        for i in range(1, len(line) - 1):
            delta = int(line[i]) - int(line[i+1])
            if(delta < 0):
                delta *= -1
            if(delta < 1 or delta > 3):
                if(first):
                    line1 = line.copy()
                    line1.remove(line[i])
                    line2 = line.copy()
                    line2.remove(line[i+1])
                    return (checkLine(line1, False) or checkLine(line2, False))
                else:
                    return False
            if(int(line[i]) > int(line[i+1])):
                if(first):
                    line1 = line.copy()
                    line1.remove(line[i])
                    line2 = line.copy()
                    line2.remove(line[i+1])
                    return (checkLine(line1, False) or checkLine(line2, False))
                else:
                    return False
            
    else:
        for i in range(1, len(line) - 1):
            delta = int(line[i]) - int(line[i+1])
            if(delta < 0):
                delta *= -1
            if(delta < 1 or delta > 3):
                if(first):
                    line1 = line.copy()
                    line1.remove(line[i])
                    line2 = line.copy()
                    line2.remove(line[i+1])
                    return (checkLine(line1, False) or checkLine(line2, False))
                else:
                    return False
                
            if(int(line[i]) < int(line[i+1])):
                if(first):
                    line1 = line.copy()
                    line1.remove(line[i])
                    line2 = line.copy()
                    line2.remove(line[i+1])
                    return (checkLine(line1, False) or checkLine(line2, False))
                else:
                    return False
    return True

if __name__ == '__main__':
    fname = "test2.txt"
    file = open(fname)
    
    safeCount = 0
    for line in file:
        line = line.strip().split()
        for i in range(len(line)):
            line[i] = int(line[i])
        if(checkLine(line, True)):
            safeCount+=1

    print(safeCount)