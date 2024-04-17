# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        words = line.split()
        for word in words:
            try:
                number = float(word)
                count += 1
                total += number
            except ValueError:
                continue

fh.close()

if count > 0:
    average = total / count
    print("Average spam confidence:",average)
else:
    print("No floating-point numbers found.")