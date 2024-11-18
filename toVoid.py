from funcs import *



with open("input.py") as f:
    s = f.read()
    for i in KeywordsInversed:
        s = s.replace(i, KeywordsInversed[i])

f = open("output.vq", "w")
f.write(s)
f.close()