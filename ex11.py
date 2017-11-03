name = input("Enter File:")
if len(name) > 1 : name = "ex11real.txt"
handle = open(name)

total = []

import re
for line in handle:
    num = re.findall('[0-9]+', line)
    for count in num:
        total.append(int(count))

print (sum(total))
