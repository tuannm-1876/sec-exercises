import os
import subprocess
def listdir():
    list=[]
    txt = os.popen('ls').read()
    txt = txt.splitlines()
    return txt
def strings(list):
    for i in list:
        txt1 = os.popen('strings -e l '+i+' | tail -1').read()
        txt1 = txt1.splitlines()
        print txt1
    return txt1
def result(list):
    for i in list:
        txt2 = os.popen('wine '+i).read()
        # txt2 = txt2.splitlines()
        print txt2
def main():
    strings(listdir())
    result(listdir())
main()