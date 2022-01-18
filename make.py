import sys
import os

# if there's no parameters
# show how to use the tool
if len(sys.argv) == 1:
    print(f"use: {sys.argv[0]} file -o outfile")
    sys.exit()
else:
    # if there's parameter
    filename = sys.argv[1]

def check(filename):
    cmd=os.popen("ls")
    if filename+"\n" not in cmd.readlines():
        print("file not found") # file not exists
        sys.exit()
    else:
        print(os.popen("ls").readlines()[:])
        pass # the file exists


check(filename) # check if the file (source code) exists

# compile the source code file
compile = f"clang -S -emit-llvm {filename}"
os.system(compile)
print("compiled!")
