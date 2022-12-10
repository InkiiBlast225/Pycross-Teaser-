from random import randint

def findRule(rowCol):
    streak = 0
    pattern = ''

    for i in rowCol:
        if i == '1':
            streak += 1
        if i == '0' and streak > 0:
            pattern += str(streak)
            streak = 0
    if streak > 0:
        pattern += str(streak)
    if pattern == '':
        pattern += '0'
    
    return(pattern)
def maxLen(lst):
    high = 0
    for i in lst:
        if len(i) > high:
            high = len(i)
    return high

cols = []
length = 3
newRowCol = []
pixels = ''
rowCol = ''
rows = []

# This code determines the rules for the rows and columns.
for _ in range(length * length):
    pixels += str(randint(0, 1))
for i in range(length):
    for j in range(length * length):
        if i * length <= j < (i + 1) * length:
            rowCol += pixels[j]
    rows.append(findRule(rowCol))
    rowCol = ''
for i in range(length):
    for j in range(length * length):
        if j % length == i:
            rowCol += pixels[j]
    cols.append(findRule(rowCol))
    rowCol = ''

print(pixels)
print(rows)
print(cols)
print('')

#This code prints the blank format.
for i in cols:
    newRowCol.append(' ' * (maxLen(cols) - len(i)) + i)
for i in range(maxLen(cols)):
    print(maxLen(rows) * ' ' + ' ', end = '')
    for j in newRowCol:
        print(j[i], end = '')
    print('')

for i in rows:
    newRowCol.append(' ' * (maxLen(rows) - len(i)) + i)
print(' ' * maxLen(rows) + '/' + length * '-')
for i in rows:
    print((' ' * (maxLen(rows) - len(i))) + i + '|', end = '')
    print(' ' * length)
