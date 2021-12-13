def plotdots(dots):
    max_x = 0
    max_y = 0
    for dot in dots:
        if dot[0] > max_x:
            max_x = dot[0]
        if dot[1] > max_y:
            max_y = dot[1]
    #print(max_x,max_y)
    #square = max(max_y,max_x) + 1
    grid = []
    blank_row = []
    for i in range(0,max_x+1):
        blank_row.append('')
    for i in range(0,max_y+1):
        grid.append(blank_row.copy())
    #print("grid = \n",grid)
    #print(grid)
    for dot in dots:
        x = dot[0]
        y = dot[1]
        #print(x,y)
        grid[dot[1]][dot[0]] = 'X'
    #print(grid)
    return grid

def foldup(grid,line):
    newgrid = []
    for i in range(0,line):
        newgrid.append(grid[i])
    for i in range(0,line):
        for j in range(0,len(grid[line])):
            if grid[i+line+1][j] == 'X':
                newgrid[line-i-1][j] = 'X'
    return newgrid


def foldleft(grid,line):
    newgrid = []
    for row in grid:
        newgrid.append(row[0:line])
    for i in range(0,len(grid)):
        rightpart = grid[i][line+1:] 
        for j in range(0,len(rightpart)):
            if rightpart[j] == 'X':
                newgrid[i][line-j-1] = 'X'
        #print("rightpart=",rightpart)


    return newgrid
    
def countdots(grid):
    dotcounter = 0
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if grid[i][j] == 'X':
                dotcounter += 1
    return dotcounter


def part1(filename):
    import copy
    with open(filename,'r') as f:
        sections = f.read().split('\n\n')
    dots = sections[0].splitlines()
    folds = sections[1].splitlines()

    for i in range(0,len(dots)):
        s = dots[i].split(',')
        dots[i] = [int(s[0]),int(s[1])]
    
    for i in range(0,len(folds)):
        folds[i] = folds[i][11:]
        s = folds[i].split('=')
        folds[i] = dict(axis = s[0], value = int(s[1]))

    #print(dots,folds)
    grid = plotdots(dots)
    for i in range(0,1):
        if folds[i]['axis'] == 'y':
            grid = foldup(grid,folds[i]['value'])
            #print("UPFOLD!!!!!!!!")
        elif folds[i]['axis'] == 'x':
            grid = foldleft(grid,folds[i]['value'])
            #print("LEFTFOLD!!!!!!!!!!!")
        #print(grid)
    return countdots(grid)

    
def part2(filename):
    import copy
    with open(filename,'r') as f:
        sections = f.read().split('\n\n')
    dots = sections[0].splitlines()
    folds = sections[1].splitlines()

    for i in range(0,len(dots)):
        s = dots[i].split(',')
        dots[i] = [int(s[0]),int(s[1])]
    
    for i in range(0,len(folds)):
        folds[i] = folds[i][11:]
        s = folds[i].split('=')
        folds[i] = dict(axis = s[0], value = int(s[1]))

    #print(dots,folds)
    grid = plotdots(dots)
    for i in range(0,len(folds)):
        if folds[i]['axis'] == 'y':
            grid = foldup(grid,folds[i]['value'])
            #print("UPFOLD!!!!!!!!")
        elif folds[i]['axis'] == 'x':
            grid = foldleft(grid,folds[i]['value'])
            #print("LEFTFOLD!!!!!!!!!!!")
        #print(grid)
    for row in grid:
        rowprint = ''
        for char in row:
            if char == 'X':
                rowprint = rowprint + 'X'
            else:
                rowprint = rowprint + ' '
        print(rowprint)
                
    return countdots(grid)



print("Part 1 test 1 answer=",part1('day13input_test1.txt'))
#print("Part 1 test 1 answer=",part1('day13input_test2.txt'))
print("Part 1 answer=",part1('day13input.txt'))
#Not the right answer.  (102)  Too Low.    I didn't set it back to do just one fold
#Yup, it was 850, I folded too many times


print("Part 2 answer=",part2('day13input.txt'))
#This was fun  - AHGCPGAU