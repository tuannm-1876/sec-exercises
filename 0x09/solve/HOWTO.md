## Bài 1

* Decompile file jar ta được đoạn mã của Java
``` java
import javax.swing.JOptionPane;

public class InviteValidator {
  public InviteValidator() {}
  
  public static void main(String[] args) { String response = JOptionPane.showInputDialog(null, "Enter your invitation code:", "Minesweeper Championship 2018", 3);
    if (response.equals("GoldenTicket2018@flare-on.com"))
    {
      JOptionPane.showMessageDialog(null, "Welcome to the Minesweeper Championship 2018!\nPlease enter the following code to the ctfd.flare-on.com website to compete:\n\n" + response, "Success!", -1);
    }
    else
    {
      JOptionPane.showMessageDialog(null, "Incorrect invitation code. Please try again next year.", "Failure", 0);
    }
  }
}
```
* Dễ dàng nhìn thấy cờ `GoldenTicket2018@flare-on.com`

## Bài 3
* Decompiler file code.cpython-37.pyc ta được 1 chương trình 
```python
def check_flag(flag):
    a = 256
    n = 10 ** 60
    l = len(flag)
    if l != 22:
        return False
    else:
        result = 0
        for i in range(0, l):
            result += ord(flag[i]) * a ** (l - i - 1) % n

        return result == 39830963251313012931406054205649358377525286926249590L
```
* Sử dụng chương trình python ex2-0x09.py ra cờ `just_ascii_to_hex_conv`

* `code anh Tiến`
```python
x= 39830963251313012931406054205649358377525286926249590
hex(x)[2:-1].decode('hex')
```

## Bài 5:
* Thử mở file `1BpnGjHOT7h5vvZsV4vISSb60Xj3pX5G.exe`
Hiển thị ra `What is the password?`
Chương trình bắt ta nhập mật khẩu, tìm kiếm mật khẩu được ẩn dấu trong file
* Thử đọc các kí tự có thể đọc được trong file `1BpnGjHOT7h5vvZsV4vISSb60Xj3pX5G.exe` bằng lệnh trong terminal `strings -l e 1BpnGjHOT7h5vvZsV4vISSb60Xj3pX5G.exe` ta thu được 
```
@BRICK
%s\%s
IronManSucks
Oh, hello Batman...
I super hate you right now.
What is the password?
%15ls
Go step on a brick!
Oh look a rainbow.
Everything is awesome!
%s => %s
BRICK
ZImIT7DyCMOeF6
```
* Dòng cuối cùng có vẻ là mật khẩu, thử nhập vào và ta thu được
```
Everything is awesome!
65141174.png => w
```
* Trong thư mục chứa file hiển thị thêm 1 file ảnh `65141174.png` là hình Lego chứa số `7` và chữ `w`
* Làm tương tự với các file khác bằng chương trình `ex5-0x09.py` ta nhận được tất cả các ảnh và chữ
* Ghép các chữ cái thu được ứng với số thứ tự trong ảnh ta thu được cờ