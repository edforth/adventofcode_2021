with open('day01input.txt','r') as f:
    lines = f.read().splitlines()

#Part 1
inccount = 0
for i in range(1,len(lines)):
    if int(lines[i]) > int(lines[i-1]):
        inccount=inccount + 1
print("Part 1 answer = ",inccount)




#print("Part 1 Answer =")
#Correct first try (1390)

#Part 2

suminccount = 0 
for i in range(0,len(lines)-3):
    suma = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    sumb = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
    if sumb > suma:
        suminccount = suminccount + 1
print("Part 1 answer = ",suminccount)
#Correct first try (1457)