import re
import sys

filePath = sys.argv[1]

with open(filePath, "r") as f:
    fstring = f.read()
    hexed = re.sub("(0[xX][0-9a-fA-F]+)", lambda m : m.group(1) + " ==> " + str(int(m.group(1),16)), fstring)
    print(hexed)
    with open(filePath + "_DEC", "w") as f_out:
        f_out.write(hexed)
