import os
import subprocess
def listdir():
    list=[]
    txt = os.popen('ls *.exe').read()
    txt = txt.splitlines()
    return txt
def strings(list):
    txt2 = []    
    for i in list:
        txt1 = os.popen('strings -e l '+i+' | tail -1').read()
        txt1 = txt1.splitlines()[0]
        txt2.append(txt1)
    return txt2
def result(list):
    a = 0    
    result1 = []
    for i in list:
        process = subprocess.Popen(["wine", ""+i], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        print process.stdin.write(strings(listdir())[a])
        b = process.communicate()[0].splitlines()[2]
        a+=1
        result1.append(b)
        process.stdin.close()
        # txt2 = txt2.splitlines()
    return result1
def main():
    strings(listdir())
    print result(listdir())
main()