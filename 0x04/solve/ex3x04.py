from socket import socket

dic = {'1': ['  #', '  #', '  #', '  #', '  #'],
       '2': ['###', '  #', '###', '#  ', '###'],
       '3': ['###', '  #', '###', '  #', '###'],
       '4': ['# #', '# #', '###', '  #', '  #'],
       '5': ['###', '#  ', '###', '  #', '###'],
       '6': ['###', '#  ', '###', '# #', '###'],
       '7': ['###', '  #', '  #', '  #', '  #'],
       '8': ['###', '# #', '###', '# #', '###'],
       '9': ['###', '# #', '###', '  #', '###'],
       '0': ['###', '# #', '# #', '# #', '###'],
       '+': ['   ', ' # ', '###', ' # ', '   '],
       '-': ['   ', '   ', '###', '   ', '   '],
       '*': ['   ', '# #', ' # ', '# #', '   '],
       '/': ['   ', '  #', ' # ', '#  ', '   ']}

def parseString(input):
    lines = str(input).split("\n")
    result = ''
    leng = len(lines[0]) / 5
    for m in range(0, leng):
        temp = []
        for n in range(0, 5):
            temp.append(lines[n][m * 5:m * 5 + 3])
        for key in dic:
            if (dic[key] == temp):
                result += key
    return result

sock = socket()
sock.connect(('188.166.218.1', 2016))
#tmp = sock.recv(10240).decode()
#tmp = sock.recv(1024).decode()
#tmpLine = tmp.split("\n")
#print tmp
#result = parseString(tmp)
#print result
#print eval(result)
#sock.send((str(result)+"\n").encode())
while True:
    data = sock.recv(10240)
    print data
    data = sock.recv(10240)
    print(data)
    result = parseString(data)
    a = eval(result)
    sock.send((str(a) + "\n").encode())