counts = dict()
n = input()
number = input().split()
for i in number:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1
for i in counts:
    if counts[i] == 1:
        print (i)