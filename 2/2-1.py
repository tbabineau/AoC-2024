if __name__ == '__main__':
    fname = "input.txt"
    file = open(fname)
    
    safeCount = 0
    for line in file:
        line = line.strip().split()
        safe = True

        delta = int(line[0]) - int(line[1])
        if(delta < 0):
            delta *= -1
        
        if(delta < 1 or delta > 3):
            safe = False
        elif(int(line[0]) < int(line[1])):
            for i in range(1, len(line) - 1):
                delta = int(line[i]) - int(line[i+1])
                if(delta < 0):
                    delta *= -1
                if(delta < 1 or delta > 3):
                    safe = False
                if(int(line[i]) > int(line[i+1])):
                    safe = False
                
        else:
            for i in range(1, len(line) - 1):
                delta = int(line[i]) - int(line[i+1])
                if(delta < 0):
                    delta *= -1
                if(delta < 1 or delta > 3):
                    safe = False
                if(int(line[i]) < int(line[i+1])):
                    safe = False

        
        if(safe):
            safeCount+=1

    print(safeCount)