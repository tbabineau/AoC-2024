def checkValid(rules, update):
    for i in range(len(update)):
        for j in range(len(rules)):
            if(rules[j][0] == update[i]):
                for k in range(len(update)):
                    if update[k] == rules[j][1]:
                        if(k < i):
                            return False
    return True

if __name__ == '__main__':
    #fname = "test.txt"
    fname = "input.txt"
    file = open(fname)
    rules = []
    updates = []
    done = False #tracks whether all rules are taken in

    #puts the rules and updates into integer arrays
    for line in file:
        if(not done):
            if(line == "\n"):
                done = True
            else:
                line = line.strip().split("|")
                rules.append([int(line[0]), int(line[1])])
        else:
            line = line.strip().split(",")
            temp = []
            for elem in line:
                temp.append(int(elem))
            updates.append(temp)
    
    #Could be made more efficient by sorting rules and using binary search
    goodUpdates = updates.copy()
    for i in range(len(updates)):
        valid = True
        for j in range(len(updates[i])):
            if(valid):
                for k in range(len(rules)):
                    if(updates[i][j] == rules[k][0]):
                        for m in range(len(updates[i])):
                            if(updates[i][m] == rules[k][1]):
                                if(m < j):
                                    valid = False
        if(not valid):
            goodUpdates.remove(updates[i])

    for update in goodUpdates:
        updates.remove(update)
    
    for i in range(len(updates)):
        while(not checkValid(rules, updates[i])):
            for j in range(len(updates[i])):
                for k in range(len(rules)):
                    if(updates[i][j] == rules[k][0]):
                        for m in range(len(updates[i])):
                            if(updates[i][m] == rules[k][1]):
                                if(m < j):
                                    temp = updates[i][m]
                                    updates[i][m] = updates[i][j]
                                    updates[i][j] = temp
    
    total = 0
    for list in updates:
        total += list[int((len(list))/2)]