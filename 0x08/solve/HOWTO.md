## Bài 1
* Đọc các packet trong file for.pcap ta chú ý đến các packet NTP
* Dòng 552 ta thấy raw data không có gì đặc biệt
* Dòng 553 ta lấy được chuỗi `iVBORw0KGgoAAAANSUhEUgAAAzcAAADiCAIAAAD8qK6MAA`, thử decode base64 ta nhận được
```
.PNG
.
...
IHDR...7...â.....ü¨®..
```
* Có vẻ như đây là raw data của một bức ảnh png
* Sử dụng UDP Stream lấy tất cả dữ liệu ra, xóa dòng `.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA..` rồi Render Image với đoạn mã còn lại ta thu được cờ `matesctf{s0_m4ny_3xf1l_pr0t0c0lz}`