byte_403000 = '\x0D\x26\x49\x45\x2A\x17\x78\x44\x2B\x6C\x5D\x5E\x45\x12\x2F\x17\x2B\x44\x6F\x6E\x56\x09\x5F\x45\x47\x73\x26\x0A\x0D\x13\x17\x48\x42\x01\x40\x4D\x0C\x02\x69'
xor_value = '\x04'
result = ""
for x in byte_403000[::-1]:
    xor_value = chr(ord(x) ^ ord(xor_value))
    result += xor_value
print result[::-1]
#byte_403000 
# .data:00403000                 db  0Dh      
# .data:00403001                 db  26h ; &
# .data:00403002                 db  49h ; I
# .data:00403003                 db  45h ; E
# .data:00403004                 db  2Ah ; *
# .data:00403005                 db  17h
# .data:00403006                 db  78h ; x
# .data:00403007                 db  44h ; D
# .data:00403008                 db  2Bh ; +
# .data:00403009                 db  6Ch ; l
# .data:0040300A                 db  5Dh ; ]
# .data:0040300B                 db  5Eh ; ^
# .data:0040300C                 db  45h ; E
# .data:0040300D                 db  12h
# .data:0040300E                 db  2Fh ; /
# .data:0040300F                 db  17h
# .data:00403010                 db  2Bh ; +
# .data:00403011                 db  44h ; D
# .data:00403012                 db  6Fh ; o
# .data:00403013                 db  6Eh ; n
# .data:00403014                 db  56h ; V
# .data:00403015                 db    9
# .data:00403016                 db  5Fh ; _
# .data:00403017                 db  45h ; E
# .data:00403018                 db  47h ; G
# .data:00403019                 db  73h ; s
# .data:0040301A                 db  26h ; &
# .data:0040301B                 db  0Ah
# .data:0040301C                 db  0Dh
# .data:0040301D                 db  13h
# .data:0040301E                 db  17h
# .data:0040301F                 db  48h ; H
# .data:00403020                 db  42h ; B
# .data:00403021                 db    1
# .data:00403022                 db  40h ; @
# .data:00403023                 db  4Dh ; M
# .data:00403024                 db  0Ch
# .data:00403025                 db    2
# .data:00403026                 db  69h ; i
# .data:00403027                 db    0