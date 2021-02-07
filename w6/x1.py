name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
file = open(name)

counts = dict();
for line in file:
    if not line.startswith("From") or line.startswith("From:")  : continue
    list = line.split()
    times = list[5].split(':')
    hour = times[0]
    counts[hour] = counts.get(hour,0) + 1

list = sorted([(hour,count) for hour,count in counts.items()])

for hour,count in list:
    print(hour,count)
