import string
import base64
custom_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789=~.'
standard_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
decode_trans = string.maketrans(custom_string, standard_string)
def decode(str):
    return base64.b64decode(str.translate(decode_trans))
string = 'c3RyaW5nIGFiYw..'
print decode(string)