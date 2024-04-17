#ghand = open("fal copy.txt")
#inp = ghand.read()
#print(len(inp))
#count = 0
#for line in ghand :
#   count = count + 1
#   print("line count:", count)
#print("total no lines", count)
ghand = open("fal copy.txt", "r")  # Open the file in read mode
inp = ghand.read()
print("Total characters:", len(inp))

count = 0
for line in inp.splitlines():  # Iterate through the lines of the file content
    count = count + 1
    print("line count:", count)

ghand.close()  # Don't forget to close the file when you're done with it
print("Total number of lines:", count)
