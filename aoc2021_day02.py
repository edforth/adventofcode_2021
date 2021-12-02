with open('day02input.txt','r') as f:
    lines = f.read().splitlines()

#part 1
depth = 0
horizontal = 0

for line in lines:
    s=line.split()
    if s[0] == 'forward':
        horizontal = horizontal + int(s[1])
    elif s[0] == 'down':
        depth = depth + int(s[1])
    elif s[0] == 'up':
        depth = depth - int(s[1])
part1answer = horizontal*depth
print("Part 1 answer",part1answer)
#Correct first try (1693300)

#Part 2
aim = 0
depth = 0
horizontal = 0

for line in lines:
    s=line.split()
    if s[0] == 'forward':
        horizontal = horizontal + int(s[1])
        depth = depth + (aim*int(s[1]))
    elif s[0] == 'down':
        aim = aim + int(s[1])
    elif s[0] == 'up':
        aim = aim - int(s[1])
part1answer = horizontal*depth
print("Part 2 answer",part1answer)
#Correct first try (1857958050)




