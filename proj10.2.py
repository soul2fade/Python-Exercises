name = input("Enter file:")
if len(name) > 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    if line.startswith("From "):
        line = line.split()
        time = line[5]
        time = time.split(':')
        hr = time[0]
        count[hr] = count.get(hr,0) + 1

lst = list()
for key, val in count.items() :
    lst.append ((key, value))

lst = sorted(lst)
for val, key in lst:
    print(key, val)
