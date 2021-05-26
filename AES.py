ip_table = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
	62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
	57, 49, 41, 33, 25, 17,  9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
	61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]



def stringtobin(string):
    str = ""
    for i in string:
        b = bin(ord(i))[2:]
        for j in range(0,8-len(b)):
            b = '0'+b
        str+=b
    return str

def ip_change(bstr):
    str = ""
    for i in ip_table:
        str+= bstr[i-1]
    return str

print(stringtobin("hellowol"))
print(ip_change(stringtobin("hellowol")))


