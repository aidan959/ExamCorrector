import glob, os
os.chdir("/answers")
for file in glob.glob("*.txt"):
    print(file)
    