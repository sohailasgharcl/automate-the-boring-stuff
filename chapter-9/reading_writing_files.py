#backslash on windows 
from pathlib import Path
print(Path("spam", "bacon","eggs"))

#implementing loop on filenames
myFile = ["accounts.txt","invite.csv","details.docs"]
for filename in myFile:
    print(Path(r"C:\Users\AI",filename))

#using the divide operator to join paths objects and strings
print(Path("spam")/"bacon"/"eggs")#the only one thing to remember is that one of the first two values must be a path object
print(Path("folder1")/Path("folder2/folder3"))
homeFolder = Path(r"C:\skills\AI")
subFolder = Path("spam")
print(homeFolder/subFolder)

#the current working directory
import os 
print(Path.cwd())
print(os.chdir(r"D:\my_skills\dev\backend_roadmap"))
print(Path.cwd())

#home directory
print(Path.home())#in windows, home directory is in C:\Users

#creating the new folder using os.makdirs()Function
#import os module
#print(os.makedirs(r"D:\my_journey\development\AI"))#its reslut will be the path that is passed to this function

#handling absolute and relative paths
print(Path.cwd())
print(Path.cwd()/Path(r"python/ABSP"))
print(Path.home()/Path(r"my/relative/path"))
print(os.path.abspath("."))
print(os.path.abspath("./python/ABSP"))#this is then best way to convert a relative path to an absolute one
print(os.path.isabs("."))
print(os.path.isabs(os.path.abspath(".")))
print(os.path.relpath(r"C:/Users","C:/"))
print(os.path.relpath(r"C:/Users","C:/Admin"))

#getting the parts of a file path
p = Path(r"C:/Users/Admin/Z/myFile.txt")
print(p.anchor)#prints the root folder(drive)
print(p.parent)#this is the path object
print(p.stem)#prints the name of file
print(p.suffix)#prints the extension of the file

#parent attribute evaluates to ancestor folder of path object with an integer index
print(os.chdir(r"D:\my_skills\dev\backend_roadmap\python\ABSP"))
print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
print(Path.cwd().parents[2])
print(Path.cwd().parents[3])
print(Path.cwd().parents[4])

#getting path name and directyory name seperalety
calcFile = ("C:Windows/System32/calc.exe")
print(os.path.basename(calcFile))
print(os.path.dirname(calcFile))
#getting patha nd directory name together
print(os.path.split(calcFile))
#using the os.sep (os part not os.path)
print(calcFile.split(os.sep))#in book it tells that it prints a list of string of each folder but it actually prints the whole patha as one string

#finding file sizes and folder contents
print(os.path.getsize("C:/Users/Admin/test.txt"))#list the file size
print(os.listdir("C:/Users/Admin"))#prints the ist of all files and folder inthat specified path
#getting the totalsize of all files at once
totalSize = 0
for filename in os.listdir("C:/Users/Admin"):
    totalSize = totalSize + os.path.getsize(os.path.join("C:/Users/Admin",filename))#used.join to join the folder name with the filename

print(totalSize)

#modifying a list of file with glob patterns
myFolder = Path("D:/my_journey")
print(list(myFolder.glob("*")))# * stands for multiple of any character
print(list(myFolder.glob("*.txt")))#listv all the txt files
print(list(myFolder.glob("zzz?.txt")))#the ? will notreturn the file with two charactes matches like filename22, filename72etc
print(list(myFolder.glob("*.?x?")))

#checking the validity of a path
winDir = Path("C:/Windows")
filePath = Path("C:/Windows/valid_path.txt")
print(winDir.exists())
print(winDir.is_dir())
print(filePath.is_file())
print(filePath.is_dir())

#opening file with the open() function
helloFile = open("C:/Users/Admin/hello.txt")
#reading file with the read() function
helloContent = helloFile.read()
print(helloContent)
#writing files with the write() function
simpleFile = open("C:/Users/Admin/simple.txt","w")
simpleFile.write("hello, world!\n")
simpleFile.close()
simpleFile = open("C:/Users/Admin/simple.txt","a")
simpleFile.write("this file contains a simple text.")
simpleFile.close()
simpleFile = open("C:/Users/Admin/simple.txt")
content = simpleFile.read()
simpleFile.close()
print(content)