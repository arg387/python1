text = "X-DSPAM-Confidence:    0.8475"
noun = text.strip()
sub = noun.find('0')
print(noun[sub:sub+6])


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hour_counts = {}
for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    for word in words:
        if ':' not in word: continue # Check if the word contains ':' and is 8 characters long
        hour = word.split(':')[0]
        hour_counts[hour] = hour_counts.get(hour, 0) + 1
        hours =sorted(hour_counts.items())
for hour, key in hours:      
    print(f"{hour} {key}")
        #print(hour)


def add(*args):
    sum = 0
    args = list(args)
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4))

    


    


