import os

f = open("text1.txt", "x")
print(f.readline(4))

# os.remove("Some.txt")
# os.rmdir("myfolder")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")