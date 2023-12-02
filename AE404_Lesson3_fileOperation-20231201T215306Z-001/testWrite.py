import os

file = open("test.txt", "w") 
file.write("CodingAPE")
file.close()

file = open("test.txt", "r")
Mystr=file.read()
print(Mystr)
file.close()

os.system("copy /b test.txt testCopyPython.txt")
file = open("testCopyPython.txt", "r")
Mystr=file.read()
print(Mystr)
file.close()