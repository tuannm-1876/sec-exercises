from os import listdir
from os.path import isfile, join
import subprocess
mypath = '/home/nguy.minh.tuan/Documents/sec-exercises/0x09/FLEGGO/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in range(len(onlyfiles)):
    text = "strings -e l /FLEGGO/" +onlyfiles[i]+ " | tail -1 | wine /FLEGGO/"+ onlyfiles[i]
    print (text)