import re
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
file = open(name)

sumList = list()

for line in file:
    line.rstrip()
    line = re.findall('\d+', line)
    if len(line) == 0 : continue

    for num in line:
        n = int(num)
        sumList.append(n)

print(sum(sumList))
newList = [line for line in re.findall('[0-9]+', file.read())]
print(newList)
#print(sum([line for line in re.findall('\d+', file.read())]))
