f = open("input.txt","r")
lines = f.readlines()

def startOfMessage(offset):
    i = offset
    while i < len(line):
        buff = line[i-offset:i]
        if len(set(buff)) == len(buff):
            return i
        i += 1

line = lines[0]

print("Part 1 : " + str(startOfMessage(4)))
print("Part 2 : " + str(startOfMessage(14)))

f.close()