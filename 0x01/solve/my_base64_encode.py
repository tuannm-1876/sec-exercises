import string
import base64
custom_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789=~.'
standard_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
encode_trans = string.maketrans(standard_string, custom_string)
def encode(str):
    return base64.b64encode(str).translate(encode_trans)
string = 'string abc'
print (encode(string))