import sys
import math

# https://www.codingame.com/ide/puzzle/mime-type

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mimeTable = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mimeTable[ext.lower()] = mt

for i in range(q):
    fname = input()  # One file name per line.
    if not "." in fname: 
        print("UNKNOWN")
    else:
        grp = fname.split(".")
        ext = grp[-1].lower()
        mimeType = mimeTable.get(ext)
        print(mimeType) if mimeType else print("UNKNOWN")

