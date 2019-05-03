## Bài 1:


## Bài 2:

* Đây là Digest access authentication

* Đọc trong file q9.pcap dòng 39 ta được 1 đoạn mã
`q9:secret:c627e19450db746b739f41b64097d449`

`q9 là username`

`secret là realm`

`c627e19450db746b739f41b64097d449` là HA1 với `HA1 = MD5(username:realm:password)`

* Tiếp tục đọc dòng 37 ta được

`Digest username="q9", realm="secret", nonce="bbKtsfbABAA=5dad3cce7a7dd2c3335c9b400a19d6ad02df299b", uri="/~q9/htdigest", algorithm=MD5, response="d9f18946e5587401c303b34e00a059eb", qop=auth, nc=00000002, cnonce="6945eb2a7ba8cf7f"`

* Vậy ta có thể tạo thông tin xác thực gửi qua máy chủ với các thông tin sau

`username: q9`

`realm: secret`

`nonce: lấy trên trình duyệt`

`uri: /~q9/flag.html`

`qop: auth`

`nc=00000001`

`cnonce="9691c249745d94fc"`

`Algorithm: MD5`

`response = MD5(HA1 + ':' + nonce + ':' + nc + ':' + cnonce + ':' + qop + ':' + HA2)`

với `HA2 = MD5('GET:' + uri)`

* Sử dụng postman với

`Key: Authorization`

```Value: Digest username="q9", realm="secret", nonce="kRDCON6HBQA=a4eb04991a891867e7acc18213de589ba6141db5", uri="/~q9/flag.html", algorithm=MD5, response="2ae6627572978c4bb56aac57353351e9", qop=auth, nc=00000001, cnonce="9691c249745d94fc"```

Ta được flag: `FLAG_YBLyivV4WEvC4pp3`
