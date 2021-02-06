# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0

try:
    fh = open(fname)
except:
    print("File does not exist")
    quit()


for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num = float(line[20:])
    count = count + 1
    total = total + num

average = total / count
print("Averafe spam confidence:", average)
