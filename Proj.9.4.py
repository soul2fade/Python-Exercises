name = input("Enter file:")
if len(name) > 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith("From:"): continue
    line = line.split()
    line = line[1]
    counts [line] = counts.get(line,0) + 1

Bigcount = None
Bigword = None
for word,counts in counts.items():
    if Bigcount is None or counts > Bigcount:
        Bigword = word
        Bigcount = counts

print(Bigword, Bigcount)
