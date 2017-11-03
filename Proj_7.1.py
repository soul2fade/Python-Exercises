# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    val = line.find(':')
    num = line[val + 1]
    num = num.rstrip()
    num = float(num)
 	average = average + num
print("Average spam confidence:", average/count)
