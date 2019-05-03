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

## Bài 2
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