import random

coin = ['heads', 'tails']
coinFlips = []
sequence = {'heads':0, 'tails':0}
sampleSize = 10000
streakMax = 6
count = 1

# simulate the random coin flip & store results in coinFlips[]
for i in range(sampleSize):
    coinFlips.append(random.choice(coin))

# check for streak of results
for i,v in enumerate(coinFlips):
    if count == streakMax:
        sequence[v] += 1
        count = 1
        continue
    else:
        try:
            if coinFlips[i+1] == v:
                count +=1
            else:
                count = 1
        except:
            print('///')

print(sequence)
numberOfStreaks = sum(sequence.values())
print('\nchance of streak: %s%%' % (numberOfStreaks / 100))
print()
