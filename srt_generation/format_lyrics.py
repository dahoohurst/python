import sys

print("formating lyrics")

i = 1
prefix = "\n00:00:00.000 --> 00:00:00.000\n"
final = ""
f = open(sys.argv[1])

strings  = f.readlines()
for line in strings:
    if line not in ['\n', '\r\n']:
        temp = str(i)+prefix
        final += temp+line+"\n"
        i=i+1

print(final)
f.close()

f=open(sys.argv[1],"w")
f.write(final)
f.close()

