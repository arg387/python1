class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split(" ")])



#code on a fully different topic
root = "he.l.lo"
pos = root.find('.')
print(root[pos:pos+3])
st = "pip"
print(str.capitalize(root))
sr = root.replace("he.l.lo","ohh")
print(sr)
# use of index operator '[]' to print out characters from string
print(root[4])
print(root+" "+st)
t = [9, 41, 12, 3, 74, 15]
print(t[2:4])

fname = input("Enter file name: ")
fh = open(fname)
si = fh.read()
sip = list(si.split())  # Split the entire content into words and store them in 'sip'
# Print the sorted list
words = list(set(sip))
words.sort()
print(words)  

fname = input("Enter file name: ")
fh = open(fname)
si = fh.read()
sip = list(si.split())
words = []
for word in sip:
    if word not in words:
        words.append(word)
words.sort()
print(words)

