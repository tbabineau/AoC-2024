if __name__ == '__main__':
    fname = "input.txt"

    file = open(fname)
    active = True
    total = 0

    for line in file:
        for i in range(len(line) - 8):
            if(line[i:i+4] == "do()"):
                active = True
            elif(line[i:i+7] == "don't()"):
                active = False
            elif line[i:i+4] == "mul(" and active:
                num1 = 0
                num2 = 0
                jump = 0
                possible = True

                for j in range(4):
                    if(i+5+j >= len(line)):
                        possible = False
                        break
                    elif(line[i+4+j] == ','):
                        break
                    else:
                        if(48 <= ord(line[i+4+j]) and ord(line[i+4+j]) <= 57):
                            num1 *= 10
                            num1 += int(line[i+4+j])
                            jump += 1
                        else:
                            possible = False
                            break
                for k in range(4):
                    if(i+5+k+jump >= len(line)):
                        possible = False
                        break
                    elif(possible):
                        if(line[i+5+k+jump] == ')'):
                            break
                        else:
                            if(48 <= ord(line[i+5+k+jump]) and ord(line[i+5+k+jump]) <= 57):
                                num2 *= 10
                                num2 += int(line[i+5+k+jump])
                            else:
                                possible = False
                                break
                
                if(possible and num1 != 0 and num2 != 0):
                    total += num1*num2
    print(total)