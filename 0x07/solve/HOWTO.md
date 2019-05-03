## Bài 1
* Mở mã nguồn trang `http://secs-ex-001.surge.sh/login.html` ta thấy có đoạn code
```js
if ("PyvragFvqrYbtvafNerRnfl@syner-ba.pbz" == rotFlag) {
          alert("Correct flag!");
        } else {
          alert("Incorrect flag, rot again");
        }
```
* Ta thấy cờ là mã hoá của biến rotFlag
* Đọc tiếp đoạn code tạo biến `rotFlag`
```js
var rotFlag = flag.replace(/[a-zA-Z]/g, function(c) {
          return String.fromCharCode(
            (c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26
          );
        });
```
* Đây là đoạn mã của rot13
* Chuyển đoạn `PyvragFvqrYbtvafNerRnfl@syner-ba.pbz` sang `rot13` ta được cờ `ClientSideLoginsAreEasy@flare-on.com`

## Bài 2
*