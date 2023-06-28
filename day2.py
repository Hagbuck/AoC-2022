f = open("input.txt","r")
lines = f.readlines()

def computeRound(opponent, player):
    score = player
    
    if opponent == player:
        return score + 3
    elif opponent == player - 1 or opponent == player + 2:
        return score + 6
    else:
        return score

# Part 1
score = 0

for line in lines:
    opponent = ord(line[0]) - ord('A') + 1
    player = ord(line[2]) - ord('X') + 1
    
    score += computeRound(opponent, player)
    
print("Part 1 : " + str(score))

# Part 2
score = 0

for line in lines:
    opponent = ord(line[0]) - ord('A') + 1
    player = ord(line[2]) - ord('X') + 1
    
    if player == 1: # loose
        player = opponent - 1
        if player <= 0:
            player = 3
   
    elif player == 2: # draw
        player = opponent
    
    else: # win
        player = opponent + 1
        if player > 3:
            player = 1
    
    score += computeRound(opponent, player)

    
print("Part 2 : " + str(score))

f.close()