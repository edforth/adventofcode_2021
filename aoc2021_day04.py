
def checkboardwin(board2check,numbersthathavebeencalled):
    #checkrows 
    winningboard = False 
    #check rows
    for row in board2check:
        for number in row:
            if str(number) not in numbersthathavebeencalled:
                #print("Nope!", int(number), "is not in", numbersthathavebeencalled)
                winningboard = False
                break 
            else: 
                #print("Yup!", int(number), "is totally in", numbersthathavebeencalled)
                winningboard = True
        if winningboard == True:
            break
    
    #checkcolumns if needed
    if winningboard == False:
        for col in range(0,5):
            for row in range(0,5):
                if str(board2check[row][col]) not in numbersthathavebeencalled:
                    #print("Nope!", str(board2check[row][col]), "is not in", numbersthathavebeencalled)
                    winningboard = False
                    break 
                else: 
                    #print("Yup!", str(board2check[row][col]), "is totally in", numbersthathavebeencalled)
                    winningboard = True
            if winningboard == True:
                break
    
    
    """
    if winningboard:
        print("Hey! This board won!")
    else:
        print("Aww, this board did not win!")
    """
    
    return winningboard

def scoreboard(board2score,numbersthathavebeencalled):
    #print("board2score",board2score)
    #print("numbersthathavebeencalled=",numbersthathavebeencalled)
    sum = 0
    for row in board2score:
        for number in row:
            if number not in numbersthathavebeencalled:
                #print(number,"is not in",numbersthathavebeencalled)
                sum = sum + int(number)
                #print("newsum=",sum)
    return sum * int(numbersthathavebeencalled[len(numbersthathavebeencalled)-1])






def part1(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    #print("lines=",lines)
    callednumbers = lines[0].split(',')
    i = 1
    boardrow = []
    boards = []
    i = 2 
    while i < len(lines):
        #print("i=",i)
        board = [] 
        j = 0
        #print("j=",j)
        while j < 5:
            #do stuff here
            boardrow = lines[i].split()
            board.append(boardrow)
            #print("boardrow=",boardrow)


            #increment j
            j = j + 1
            i = i + 1
            #print("j=",j)
        #print("board=",board)
        boards.append(board)
        i = i+1
    #print("boards=",boards)

    #print("callednumbers=",callednumbers)
    #print("boards=",boards)
    for i in range(5,len(callednumbers)):
        for j in range(0,len(boards)):
            if checkboardwin(boards[j],callednumbers[0:i]):
                #print("callednumbers=",callednumbers[0:i])
                #print("boardthatwon=",boards[j])
                part1answer = scoreboard(boards[j],callednumbers[0:i])
                return part1answer
    return 0






def part2(filename):
    with open(filename,'r') as f:
        lines = f.read().splitlines()
    #print("lines=",lines)
    callednumbers = lines[0].split(',')
    i = 1
    boardrow = []
    boards = []
    i = 2 
    while i < len(lines):
        #print("i=",i)
        board = [] 
        j = 0
        #print("j=",j)
        while j < 5:
            #do stuff here
            boardrow = lines[i].split()
            board.append(boardrow)
            #print("boardrow=",boardrow)


            #increment j
            j = j + 1
            i = i + 1
            #print("j=",j)
        #print("board=",board)
        boards.append(board)
        i = i+1
    #print("boards=",boards)
    boardsthathavewon = []
    while len(boards) > 0:
        breakloops = False 
        for i in range(5,len(callednumbers)):
            for j in range(0,len(boards)):
                if checkboardwin(boards[j],callednumbers[0:i]):
                    boardsthathavewon.append(boards[j])
                    breakloops = True
                    lastcallednumbers = callednumbers[0:i] 
                    boards.remove(boards[j])
                    break
            if breakloops:
                break
    part2answer = scoreboard(boardsthathavewon[len(boardsthathavewon)-1],lastcallednumbers)
    print("lastboard=",boardsthathavewon[len(boardsthathavewon)-1],"lastcallednumbers=",lastcallednumbers)
    return part2answer




#print("Part 1 test answer = ",part1('day04input_test1.txt'))
#print("Part 1 answer = ",part1('day04input.txt'))
#FIRST TRY!!!! (This was pretty hard!) (71708)

print("Part 2 test answer = ",part2('day04input_test1.txt'))
print("Part 2 answer = ",part2('day04input.txt'))
#Correct first try!!!! (34726)