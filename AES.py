ip_table = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
	62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
	57, 49, 41, 33, 25, 17,  9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
	61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

pc_1 = [57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4]

left_table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]



pc_2 = [14,17,11,24,1,5,3,28,15,6,21,10,
        23,19,12,4,26,8,16,7,27,20,13,2,
        41,52,31,37,47,55,30,40,51,45,33,
        48,44,49,39,56, 34,53,46,42,50,36,
        29,32]

e_table = [32,1,2,3,4,5, 4,5,6,7,8,9, 8,9,10,11,12,13,
           12,13,14,15,16,17,16,17,18,19,20,21,20,21,
           22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

def e_str(str):
    s = ''
    for i in e_table:
        s+= str[i-1]
    return s

def pt_xor_key(pt,k):
    xor = ''
    if (len(pt) == 48) & (len(k) == 48):
        for i in range(len(pt)):
            if i < len(pt):
                xor += pt[i:i+1] ^ k[i:i+1]
    return xor






def lsi(lst, k):
    return lst[k:] + lst[:k]

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
    return str[0:32],str[32:]

def checkplaintext(pt):
    if len(pt) % 64 !=0:
        for i in range(64-(len(pt)%64)):
            pt+='0'
    return pt

def checkkey(k):
    if len(k)<64:
        for i in range(64-(len(k)%64)):
            k+="0"
    else:
        k=k[0:64]
    return k


def pc_2f(k):
    pc2k=''
    for i in pc_2:
        pc2k += k[i-1]
    return pc2k

keylist = []

def key(k):
    k = checkkey(stringtobin(k))
    pc_k = ""
    for i in pc_1:
        pc_k += k[i-1]
    c = pc_k[0:28]
    d = pc_k[28:]
    store = ""
    for i in range(len(left_table)):
        if len(keylist) == 0:
            ci = lsi(c,left_table[i])
            di = lsi(d,left_table[i])
            store = ci+di
            keylist.append(pc_2f(ci+di))
        else:
            ci = lsi(store[0:28],left_table[i])
            di = lsi(store[28:], left_table[i])
            keylist.append(pc_2f(ci+di))
            store = ci + di











#print(stringtobin("hellowol"))
#print(ip_change(stringtobin("hellowol")))
key("hello")

print(pt_xor_key(keylist[0],keylist[1]))
#print(len(keylist))





