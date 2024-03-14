f = open("text.txt", "r")


f2 = open("text.txt", "r")
print(f.read())

f3 = open("text.txt", "r")
print(f.read(5))

f4 = open("text.txt", "r")
print(f.readline())
f.close()

f = open("text.txt", "r")
for x in f:
    print(x)

