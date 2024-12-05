if __name__ == '__main__':
    fname = "input.txt"
    file = open(fname)
    ws = []
    for line in file:
        ws.append(line.strip())
    
    count = 0
    for i in range(1, len(ws)-1):
        for j in range(1, len(ws[0]) - 1):
            if(ws[i][j] == 'A'):
                #topleft to bottom right
                if((ws[i-1][j-1] == "M" and ws[i+1][j+1] == "S") or (ws[i-1][j-1] == "S" and ws[i+1][j+1] == "M")):
                    #topright to bottom left
                    if((ws[i-1][j+1] == "M" and ws[i+1][j-1] == "S") or (ws[i+1][j-1] == "M" and ws[i-1][j+1] == "S")):
                        count += 1
                
    print(count)