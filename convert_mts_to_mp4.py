import sys, os

args = sys.argv
path = os.getcwd()
os.chdir(path)
for file in args[1:]:
    print('converting...'+file)
    result = file.split(".")
    name = result[0]
    cmd = path+"\\ffmpeg.exe -i "+ path +"\\new\\"+file+" "+path+"\\new\\"+name+".mp4"
    os.system(cmd)