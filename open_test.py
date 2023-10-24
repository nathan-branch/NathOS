import subprocess;

openTrue = input("Should i open space rocks:: ")

if openTrue == "yes":
    subprocess.Popen('C:\\Users\\rnbra\\Desktop\\Old Computer\\Folder\\SpaceRocks\\Space Rocks.exe')
else:
    print("Okay, i wont open")
print (openTrue);