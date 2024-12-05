if __name__ == '__main__':
    fname = "input.txt"
    file = open(fname)
    ws = []
    for line in file:
        ws.append(line.strip())
    
    count = 0
    for i in range(len(ws)):
        for j in range(len(ws[0])):
            if(ws[i][j] == 'X'):
                #North dec i
                if(i >= 3):
                    if(ws[i-1][j] == "M" and ws[i-2][j] == "A" and ws[i-3][j] == "S"):
                        count += 1
                #NE dec i inc j
                if(i >= 3 and j < len(ws[0]) - 3):
                    if(ws[i-1][j+1] == "M" and ws[i-2][j+2] == "A" and ws[i-3][j+3] == "S"):
                        count += 1
                #East inc j
                if(j < len(ws[0]) - 3):
                    if(ws[i][j+1] == "M" and ws[i][j+2] == "A" and ws[i][j+3] == "S"):
                        count += 1
                #SE inc i inc j
                if(i < len(ws) - 3 and j < len(ws[0]) - 3):
                    if(ws[i+1][j+1] == "M" and ws[i+2][j+2] == "A" and ws[i+3][j+3] == "S"):
                        count += 1
                #South inc i
                if(i < len(ws) - 3):
                    if(ws[i+1][j] == "M" and ws[i+2][j] == "A" and ws[i+3][j] == "S"):
                        count += 1
                #SW inc i dec j
                if(i < len(ws) - 3 and j >= 3):
                    if(ws[i+1][j-1] == "M" and ws[i+2][j-2] == "A" and ws[i+3][j-3] == "S"):
                        count += 1
                #west dec j
                if(j >= 3):
                    if(ws[i][j-1] == "M" and ws[i][j-2] == "A" and ws[i][j-3] == "S"):
                        count += 1
                #NW dec i dec j
                if(i >= 3 and j >= 3):
                    if(ws[i-1][j-1] == "M" and ws[i-2][j-2] == "A" and ws[i-3][j-3] == "S"):
                        count += 1
    print(count)