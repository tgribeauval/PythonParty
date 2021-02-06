# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File does not exist')
    quit()

for line in fh:
    line = line.rstrip('\n').upper()
    print(line)
