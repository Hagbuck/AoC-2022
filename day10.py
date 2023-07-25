import re
from math import ceil, floor

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

f = open("input.txt","r")
lines = f.readlines()

class CRT:
    def __init__(self):
        self.screen = ""
        self.row = ""
        self.pos = 0

class CPU:
    def __init__(self):
        self.cycle = 1
        self.X = 1
        self.sum = 0
        self.crt = CRT()
   
    def displaySprite(self):
        out = ""
        for i in range(0, 40):
            out += "#" if i >= self.X - 1 and i <= self.X + 1 else "."
        print(out)
        
    def nextCycle(self, inst, x = 0):
        print("Start cycle {} : {}".format(self.cycle, inst))
        print("CRT pos : {} and X = {}".format(self.crt.pos, self.X))
        
        
        self.crt.row += "#" if self.crt.pos >= self.X-1 and self.crt.pos <= self.X +1 else "."
        self.crt.pos += 1
        self.displaySprite()
        print("CRT row : {}\n".format(self.crt.row))
        
        
        self.X += x
        
        if self.cycle % 40 == 0:
            self.crt.screen += self.crt.row + " " + str(self.cycle)  + "\n"
            self.crt.row = ""
            self.crt.pos = 0
        
        self.cycle += 1
            
        if self.cycle % 40 == 20:
            self.sum += self.X*self.cycle


cpu = CPU()

for line in lines:
    line = line.replace("\n", "")
    groups = re.search(r"addx (-?[0-9]\d*)", line)
    
    if groups != None:
        # Read register move
        x = int(groups[1])
        
        # Add first cycle and do nothing
        cpu.nextCycle(groups[0])
        
        # Second cycle and add value to X
        cpu.nextCycle("EOF " + groups[0], x)
    else:
        # No move
        cpu.nextCycle(line)
    

print("Part 1 : " + str(cpu.sum))
print("Part 2 : \n" + cpu.crt.screen)

f.close()