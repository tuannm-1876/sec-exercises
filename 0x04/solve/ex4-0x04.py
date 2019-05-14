def find(div1, sur1, div2, sur2, div3, sur3):
    i = 0
    j = 0
    k = 0
    while True:
        num1 = sur1 + div1*i
        num2 = sur2 + div2*j
        num3 = sur3 + div3*k
        min_num = min(num1, num2, num3)
        if min_num == num1:
            i+=1
        elif min_num == num2:
            j+=1
        else:
            k+=1
        if num1 == num2 or num2 == num3 or num3 == num1:
            break
    return num1
# def findChr(number):
#     for i in range(32, 128):
#         for j in range(32, 128):
#             for k in range(32, 128):
#                 if ((i|(j << 8)|(k << 16))==number):
#                     break
#     return i
def bin_to_char(input):
    return chr(int(input, 2))
if __name__ == "__main__":
    a = find(3571, 2963, 2843, 215, 30243, 13059)
    b = find(80735, 51964, 8681, 2552, 40624, 30931)
    c = find(99892, 92228, 45629, 1080, 24497, 12651)
    d = find(54750, 26981, 99627, 79040, 84339, 77510)
    a = format(a, '#026b')
    b = format(b, '#026b')
    c = format(c, '#026b')
    d = format(d, '#026b')
    print bin_to_char(a[19:26])
    print bin_to_char(b[19:26])
    print bin_to_char(c[19:26])
    print bin_to_char(d[19:26])
    print bin_to_char(a[11:18])
    print bin_to_char(b[11:18])
    print bin_to_char(c[11:18])
    print bin_to_char(d[11:18])
    print bin_to_char(a[2:10])
    print bin_to_char(b[2:10])
    print bin_to_char(c[2:10])
    print bin_to_char(d[2:10])

