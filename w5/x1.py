name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
file = open(name)

counts = dict();
for line in file:
    if not line.startswith("From:") : continue
    list = line.split()
    sender = list[1]
    counts[sender] = counts.get(sender,0) + 1

winner = None
winner_count = None
for sender,count in counts.items():
     if winner == None or count > winner_count:
        winner = sender
        winner_count = count

print(winner, winner_count)
