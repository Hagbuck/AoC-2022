import re

regex_config = r"\[([a-zA-Z])\]|(    )"
regex_data = r"move (\d*) from (\d*) to (\d*)"

class Ship:
    def __init__(self):
        self.stacks = []
        
    def loadCrate(self, stack_id, crate):
        stack_id -= 1
        if stack_id >= len(self.stacks):
            diff = stack_id - len(self.stacks) + 1
            for i in range(0, diff):
                self.stacks.append([])
                
        self.stacks[stack_id].append(crate)
       
    def reverse(self):
        for s in self.stacks:
            s.reverse()
   
    def move(self, src, dst, nb):
        # Remove offset
        src -= 1
        dst -= 1
        
        for i in range(0, nb):
            carte = self.stacks[src].pop() # Get lat from source and remove it
            self.stacks[dst].append(carte) # Push it at the last position of the dest
    
    def move2(self, src, dst, nb):
        # Remove offset
        src -= 1
        dst -= 1
        
        cartes = self.stacks[src][-nb:]
        del self.stacks[src][-nb:]
        self.stacks[dst].extend(cartes) # Push it at the last position of the dest
        
    def display(self):
        height = max([len(s) for s in self.stacks])
        out = ""
        
        for i in range(0, height):
            y = height - i - 1
            for s in self.stacks:
                if y < len(s):
                    out += "[" + str(s[y]) + "] "
                else:
                    out += '    '
            out += '\n'
        out += ' '
        for i in range(0, len(self.stacks)):
            out += str(i + 1) + "   "
        out += '\n'
        for i in range(0, len(self.stacks)):
            out += "----"
        out += '\n'
        print(out)
   
    def getTopCrates(self):
        out = [s[-1] for s in self.stacks if len(s) > 0]
        return "".join(out)

def linesToShip(lines):
    s = Ship()
    for line in lines:
        config_matches = re.finditer(regex_config, line, re.MULTILINE)
        if config_matches:
            x = 1
            for matchNum, match in enumerate(config_matches, start=1):
                    
                crate = match.group(1)
                if crate is not None and crate.isspace() == False:
                    s.loadCrate(x, crate)
                x += 1
        else:
            break
    s.reverse()
    return s

f = open("input.txt","r")
lines = f.readlines()

# Load config
s = linesToShip(lines)
s2= linesToShip(lines)

# Each move
for line in lines:
    data_matches = re.search(regex_data, line)
    if data_matches:
        s.move(int(data_matches.group(2)), int(data_matches.group(3)), int(data_matches.group(1)))
        s2.move2(int(data_matches.group(2)), int(data_matches.group(3)), int(data_matches.group(1)))

print("Part 1 : " + s.getTopCrates())
print("Part 2 : " + s2.getTopCrates())

f.close()