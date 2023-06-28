f = open("input.txt","r")
lines = f.readlines()

max_cal = 0
curr_cal = 0

# Part one
for line in lines:
    if line in ['\n', '\r\n']:
        if curr_cal > max_cal:
            max_cal = curr_cal
        curr_cal = 0
    else:
        curr_cal += int(line)
      
print("Part 1 : " + str(max_cal))

# Part two
elves = []
elf = 0
for line in lines :
    if line.strip():
        elf += int(line)
    else:
        elves.append(elf)
        elf = 0
        
elves.sort(reverse=True)
bo_3 = elves[0]+elves[1]+elves[2]
print("Part 2 : " + str(bo_3))

f.close()