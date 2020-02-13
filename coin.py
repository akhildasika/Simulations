import random

numFlips = int(input("How many Flips: "))
               
flips = [0] * numFlips
               
i = int(0)
while(i < numFlips - 1):
       flip = random.randint(0,1)
       flips[i] = flip
       i += 1

            
side = int(input("Enter Side: "))

run = int(input("Enter Run: "))           

if(side == 0):
        phrase = 'heads'
else:
        phrase = 'tails'


a = int(0)
count = int(0)
runs = int(0)
while(a < numFlips - 1):
    if(flips[a] == side):
          count += 1
          a += 1
          if(count == run):
              runs += 1
              count = 0
    else:
          count = 0
          a += 1


print(f"{run} {phrase} occurs {runs} times") 
