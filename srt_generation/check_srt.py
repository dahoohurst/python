import sys
import re

print("check srt file")

f = open(sys.argv[1])

content = f.readlines()
i=0
first=False
size = len(content)
newcontent = ""
for line in content:
    res = re.findall("[0-9][0-9]:[0-9][0-9]:[0-9][0-9][.][0-9][0-9][0-9]", line)
    if first == False and line.count('00:00:00.000') == 2 :
        first = True
        print(i)
        print("old is:"+line)
        for index in range(i+1, size):
            res2 = re.findall("[0-9][0-9]:[0-9][0-9]:[0-9][0-9][.][0-9][0-9][0-9]", content[index])
            if(content[index].count('00:00:00.000') != 2 and len(res2) == 2):
                print(index)
                pos = line.rfind('00:00:00.000')
                print(res2)
                line = line[0:pos] + res2[0] + "\n"
                print("new is:"+line)
                break
    elif len(res) == 2 and res[1] == '00:00:00.000' and res[0] != '00:00:00.000':
        print(i)
        print(line)
        for index in range(i+1, size):
            res2 = re.findall("[0-9][0-9]:[0-9][0-9]:[0-9][0-9][.][0-9][0-9][0-9]", content[index])
            if len(res2) == 2 and res2[1] == '00:00:00.000' and res2[0] != '00:00:00.000':
                print(index)
                pos = line.rfind('00:00:00.000')
                print(res2)
                line = line[0:pos] + res2[0]+ "\n"
                print(line)
                break
    else: 
        pass
    i =i + 1
    newcontent = newcontent + line

print(newcontent)
f.close()

f=open(sys.argv[1], "w")
f.write(newcontent)
f.close()




    