fname = input("Enter file name: ")
lst = list()

try:
    fh = open(fname)
except:
    print("Please enter valid file name")

for line in fh:
    line.rstrip()
    list = line.split()

    for word in list:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
