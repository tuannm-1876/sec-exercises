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

## Bài 4:
* Decompile file ra ta thấy cấu trúc file như sau
<figure class="image">
  <img src="{{ /0x09/solve/ex4-01.png }}">
</figure>

* Nhìn hình thấy ta nhập cờ sẽ có 2 hướng báo đúng và báo sai rồi thoát
* Convert code ta được
``` c
void __noreturn start()
{
  DWORD NumberOfBytesWritten; // [esp+0h] [ebp-4h]

  NumberOfBytesWritten = 0;
  hFile = GetStdHandle(0xFFFFFFF6);
  dword_403074 = GetStdHandle(0xFFFFFFF5);
  WriteFile(dword_403074, aG1v3M3T3hFl4g, 0x13u, &NumberOfBytesWritten, 0);
  sub_4010F0(NumberOfBytesWritten);
  if ( sub_401050() )
    WriteFile(dword_403074, aG00dJ0b, 0xAu, &NumberOfBytesWritten, 0);
  else
    WriteFile(dword_403074, aN0tT00H0tRWe7r, 0x24u, &NumberOfBytesWritten, 0);
  ExitProcess(0);
}
```
* Vậy hàm `sub_401050()` sẽ xử lý cờ. Tập trung vào hàm này.
* Tiếp tục convert code hàm `sub_401050()` ta được
``` c
signed int sub_401050()
{
  int v0; // ST04_4
  int i; // [esp+4h] [ebp-8h]
  unsigned int j; // [esp+4h] [ebp-8h]
  char v4; // [esp+Bh] [ebp-1h]

  v0 = sub_401020((int)byte_403078);            // v0 = lenght (chuoi flag) => flag co 39 ki tu
                                                // v0 = 39
  v4 = sub_401000();                            // v4=0x04
  for ( i = v0 - 1; i >= 0; --i )
  {
    byte_403180[i] = v4 ^ byte_403078[i];
    v4 = byte_403078[i];
  }
  for ( j = 0; j < 0x27; ++j )                  // j = 0 -> j = 39
  {
    if ( byte_403180[j] != (unsigned __int8)byte_403000[j] )// ham kiem tra flag
      return 0;
  }
  return 1;
}
```
* Ta cần tính giá trị trả về của `v0` và `v4`
* Đọc tiếp code trả về của `v0`
``` c
int __cdecl sub_401020(int a1)
{
  int i; // [esp+0h] [ebp-4h]

  for ( i = 0; *(_BYTE *)(i + a1); ++i )
    ;
  return i;
}
```
* `v0` sẽ trả về giá trị lenght của chuỗi nhập vào (Cụ thể là giá trị lenght của flag)
* Nhưng ở hàm bên dưới thấy
``` c
  for ( j = 0; j < 0x27; ++j )                  // j = 0 -> j = 39
  {
    if ( byte_403180[j] != (unsigned __int8)byte_403000[j] )// ham kiem tra flag
      return 0;
  }
  return 1;
```
* Đây là hàm check flag có `j` chạy từ `0` đến `38` -> `lenght(flag)=39`
* Vậy `v0=39`
* Tiếp tục xem đến giá trị của `v4`
``` c
__int16 sub_401000()
{
  return (unsigned __int16)__ROL4__(-2147024896, 4) >> 1;
}
```
* Hàm `sub_401000()` trả về giá trị 0x04
* Trong đoạn code này ta lại thấy
```c
  for ( i = v0 - 1; i >= 0; --i )
  {
    byte_403180[i] = v4 ^ byte_403078[i];
    v4 = byte_403078[i];
  }
```
* Mảng nhập vào sẽ XOR liên tục với `v4` rồi lưu giá trị cũ vào `v4`
* Vậy ta chỉ cần tìm được chuỗi kiểm tra rồi XOR ngược lại với `v4` ta sẽ tìm được cờ
* Tìm được chuỗi `byte_403078`
```
.data:00403000 byte_403000     db 0Dh                  ; DATA XREF: sub_401050+84↑r
.data:00403001                 db  26h ; &
.data:00403002                 db  49h ; I
.data:00403003                 db  45h ; E
.data:00403004                 db  2Ah ; *
.data:00403005                 db  17h
.data:00403006                 db  78h ; x
.data:00403007                 db  44h ; D
.data:00403008                 db  2Bh ; +
.data:00403009                 db  6Ch ; l
.data:0040300A                 db  5Dh ; ]
.data:0040300B                 db  5Eh ; ^
.data:0040300C                 db  45h ; E
.data:0040300D                 db  12h
.data:0040300E                 db  2Fh ; /
.data:0040300F                 db  17h
.data:00403010                 db  2Bh ; +
.data:00403011                 db  44h ; D
.data:00403012                 db  6Fh ; o
.data:00403013                 db  6Eh ; n
.data:00403014                 db  56h ; V
.data:00403015                 db    9
.data:00403016                 db  5Fh ; _
.data:00403017                 db  45h ; E
.data:00403018                 db  47h ; G
.data:00403019                 db  73h ; s
.data:0040301A                 db  26h ; &
.data:0040301B                 db  0Ah
.data:0040301C                 db  0Dh
.data:0040301D                 db  13h
.data:0040301E                 db  17h
.data:0040301F                 db  48h ; H
.data:00403020                 db  42h ; B
.data:00403021                 db    1
.data:00403022                 db  40h ; @
.data:00403023                 db  4Dh ; M
.data:00403024                 db  0Ch
.data:00403025                 db    2
.data:00403026                 db  69h ; i
.data:00403027                 db    0
```
* Chạy file `ex4-0x09.py` ta tìm được cờ: `R_y0u_H0t_3n0ugH_t0_1gn1t3@flare-on.com`

## Bài 6:
* Decompile file apk, đọc file `JewlActivity.java` trong Source, đây là hàm xử lý chính nên ta tập trung vào hàm này
* Đầu tiên ta chú ý đến biến `deviceId`, đây sẽ là biến quan trọng. 
```java
String deviceId = ((TelephonyManager) getSystemService("phone")).getDeviceId();
        try {
            MessageDigest instance = MessageDigest.getInstance("SHA-256");
            instance.update(deviceId.getBytes("ASCII"));
            String bigInteger = new BigInteger(instance.digest()).toString(16);
            if (!deviceId.substring(0, 8).equals("99999991")) {
                new Builder(this).setMessage("Your device is not supported").setCancelable(false).setPositiveButton("OK", new C0001b(this)).show();
            }
```
* Đọc đoạn code trên ta thấy được `deviceId` được mã hóa theo `SHA-256` rồi chuyển sang mã `hex`
```java
if (!deviceId.substring(0, 8).equals("99999991")) {
                new Builder(this).setMessage("Your device is not supported").setCancelable(false).setPositiveButton("OK", new C0001b(this)).show();
            }
```
* Từ đoạn này ta thấy được `deviceId` sẽ có dạng `99999991xxxxx` với số x chưa biết. Mặt khác ta lại có mã hex sau khi mã hóa `SHA-256` nên ta tấn công `brute force`
> Chương trình brute force tìm `deviceId`
```python
import hashlib
deviceid = 999999910000000
for i in range(0, 100000000):
    text = str(deviceid+i)
    check = hashlib.sha256(text).hexdigest()
    print i
    if check == "356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5":
        print text
        break   
```
* Kết quả trả về `deviceId = 999999913371337`
* Đọc tiếp các đoạn code còn lại ta sẽ tìm thấy các thông tin giải mã `AES` với file raw của ảnh `jewel_c`
* Tìm thấy file `jewel_c.png` trong đường dẫn `/Jewel_source_from_JADX/res/raw` rồi giải mã `AES` với các giá trị sau
> `key: !999999913371337`
> `IV:kLwC29iMc4nRMuE5`
> `Mode:CBC`

* Render ra ảnh ta thấy flag trong comment của ảnh
* Vậy flag là `FLAG_9X4bfxgLTi5KtQss`

## Bài 7:

Decompile file `rightsout.exe` ra bằng `ILSpy` ta thấy có đoạn check 
``` C
private void check()
	{
		if (Array.IndexOf(state, value: true) >= 0)
		{
			return;
		}
		MessageBox.Show("Congratulations!");
		int[] array = new int[8]
		{
			1,
			7,
			16,
			11,
			14,
			19,
			20,
			18
		};
		bool flag = true;
		for (int i = 0; i < 8; i++)
		{
			if (hist[i] != array[i])
			{
				flag = false;
			}
		}
		if (flag)
		{
			int[] array2 = new int[33]
			{
				85,
				111,
				117,
				43,
				104,
				127,
				117,
				117,
				33,
				110,
				99,
				43,
				72,
				95,
				85,
				85,
				94,
				66,
				120,
				98,
				79,
				117,
				68,
				83,
				64,
				94,
				39,
				65,
				73,
				32,
				65,
				72,
				51
			};
			string text = "";
			for (int j = 0; j < array2.Length; j++)
			{
				text += (char)(array2[j] ^ array[j % array.Length]);
			}
			MessageBox.Show(text);
		}
	}
```
* Sửa sang lại 1 chút rồi chạy compile
``` c
using System;
					
public class Program
{
	public static void check()
      {
          int[] array = new int[8]
          {
              1,
              7,
              16,
              11,
              14,
              19,
              20,
              18
          };
          bool flag = true;
          if (flag)
          {
              int[] array2 = new int[33]
              {
                  85,
                  111,
                  117,
                  43,
                  104,
                  127,
                  117,
                  117,
                  33,
                  110,
                  99,
                  43,
                  72,
                  95,
                  85,
                  85,
                  94,
                  66,
                  120,
                  98,
                  79,
                  117,
                  68,
                  83,
                  64,
                  94,
                  39,
                  65,
                  73,
                  32,
                  65,
                  72,
                  51
              };
              string text = "";
              for (int j = 0; j < array2.Length; j++)
              {
                  text += (char)(array2[j] ^ array[j % array.Length]);
              }
              Console.WriteLine(text);
          }
      }
	public static void Main()
	{
		check();
	}
}
```
* Ta nhận được flag: `FLAG_EhiAfPAAY7JG3UZ2`