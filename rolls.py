import random

roll = random.randint(1, 6)
    
numRoll = int(input("Enter number of rolls: "))

list1 = {}

i = int(0)
while(i <= (numRoll - 1)):
    roll = random.randint(1, 6)
    list1[i] = roll
    i += 1

o = int(0)
tw = int(0)
th = int(0)
fo = int(0)
fi = int(0)
si = int(0)

a = int(0)
while(a <= (numRoll - 1))
    if(list1[a] == 1):
            o += 1
    i += 1
    
b = int(0)
while(b <= numRoll - 1):
    if(list1[b] == 2):
            tw += 1
    b += 1
    
c = int(0)
while(c <= numRoll - 1):
    if(list1[c] == 3):
            th += 1
    c += 1
        
d = int(0)
while(d <= numRoll - 1):
    if(list1[d] == 4):
            fo += 1
    d += 1       
        
e = int(0)
while(e <= numRoll - 1):
    if(list1[e] == 5):
            fi += 1
    e += 1        
        
f = int(0)
while(f <= numRoll - 1):
    if(list1[f] == 6):
            si += 1
    f += 1


print(f"1: {o}/{numRoll} = {o / numRoll}%")
print(f"2: {tw}/{numRoll} = {tw / numRoll}%")
print(f"3: {th}/{numRoll} = {th / numRoll}%")
print(f"4: {fo}/{numRoll} = {fo / numRoll}%")
print(f"5: {fi}/{numRoll} = {fi / numRoll}%")
print(f"6: {si}/{numRoll} = {si / numRoll}%")

    
