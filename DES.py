import re


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

ip_1 = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,
        6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,
        44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,
        42,10,50,18,58,26,33,1,41,9,49,17,57,25]



left_table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]



pc_2 = [14,17,11,24,1,5,3,28,15,6,21,10,
        23,19,12,4,26,8,16,7,27,20,13,2,
        41,52,31,37,47,55,30,40,51,45,33,
        48,44,49,39,56, 34,53,46,42,50,36,
        29,32]

e_table = [32,1,2,3,4,5, 4,5,6,7,8,9, 8,9,10,11,12,13,
           12,13,14,15,16,17,16,17,18,19,20,21,20,21,
           22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

p_table = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
         [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
         [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
         [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6 ],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14 ],
          [ 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
         [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [ 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8 ],
          [ 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6 ],
          [ 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ]],
         [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1 ],
          [ 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6 ],
          [ 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2 ],
          [ 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
         [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7 ],
          [ 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2 ],
          [ 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8 ],
          [ 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]



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
                xor += str(int(pt[i:i+1],10) ^ int(k[i:i+1],10))
    return xor



def p_tablef(str):
    s = ""
    for i in p_table:
        s += str[i-1]
    return s



def lsi(lst, k):
    return lst[k:] + lst[:k]

def stringtobin(string):
    str = ""
    for i in string:
        b = bin(ord(i))[2:].zfill(8)
        str+=b
    return str

def ip_change(bstr):
    str = ""
    for i in ip_table:
        str+= bstr[i-1]
    return str[0:32],str[32:]



def ip_1f(str):
    s = ""
    for i in ip_1:
        s+=str[i-1]
    return s

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



def key(k):
    k = checkkey(stringtobin(k))
    pc_k = ""
    keylist = []
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
    return keylist


def xor32(s,f):
    xor = ''
    if len(s) == 32:
        for i in range(len(s)):
            if i < len(s):
                xor += str(int(s[i:i + 1], 10) ^ int(f[i:i + 1], 10))
    return xor


def bintostr(bin):
    b = ""
    str = ""
    for i in range(0,len(bin),8):
       b = bin[i:i+8]
       str+= chr(int(b,2))
    return str




def f(r,k):
    r = e_str(r)
    skxor = pt_xor_key(r,k)
    res = p_tablef(s_boxf(skxor))
    return res


def s_boxf(str):
    s = ""
    sbox_index = 0
    for i in range(0,len(str),6):
        si = str[i:i+6]
        row = int(si[0]+si[5],2)
        col = int(si[1:5],2)
        num = bin(s_box[sbox_index][row][col])[2:].zfill(4)
        s+=num
        sbox_index += 1
    return s


def encryption(pt,keys,m):
    binstr = stringtobin(pt)
    binstr = checkplaintext(binstr)
    ctext = ""
    k = key(checkkey(keys))
    if len(binstr) > 64:
        strblock = []
        s = ""
        for j in range(0,len(binstr),64):
            s = binstr[j:j+64]
            strblock.append(s)
        for i in range(len(strblock)):
            l0 = ip_change(strblock[i])[0]
            r0 = ip_change(strblock[i])[1]
            leftbuffer = ""
            rightbuffer = ""
            for i in range(0,17):
                if i == 0:
                    l1 = r0
                    r1 = xor32(l0,f(r0,k[i]))
                    leftbuffer = l1
                    rightbuffer = r1

                elif i == 16:
                    ctext+=ip_1f(rightbuffer+leftbuffer)
                else:
                    li = rightbuffer
                    ri = xor32(leftbuffer,f(rightbuffer,k[i]))
                    leftbuffer = li
                    rightbuffer = ri
        if m == "1":
            return bintostr(ctext)
        else:
            return ctext
        return ctext
    else:
        l0 = ip_change(binstr)[0]
        r0 = ip_change(binstr)[1]
        leftbuffer = ""
        rightbuffer = ""
        for i in range(0,17):
                if i == 0:
                    l1 = r0
                    r1 = xor32(l0,f(r0,k[i]))
                    leftbuffer = l1
                    rightbuffer = r1
                elif i == 16:
                    ctext+=ip_1f(rightbuffer+leftbuffer)
                else:
                    li = rightbuffer
                    ri = xor32(leftbuffer,f(rightbuffer,k[i]))
                    leftbuffer = li
                    rightbuffer = ri
        if m == "1":
            return bintostr(ctext)
        else:
            return ctext
        return ctext

def decryption(pt,keys):
    binstr = stringtobin(pt)
    binstr = checkplaintext(binstr)
    ctext = ""
    k = key(checkkey(keys))
    if len(binstr) > 64:
        strblock = []
        s = ""
        for i in range(0, len(binstr), 64):
            strblock.append(binstr[i:i + 64])
        for i in range(len(strblock)):
            l0 = ip_change(strblock[i])[0]
            r0 = ip_change(strblock[i])[1]
            leftbuffer = ""
            rightbuffer = ""
            for i in range(0, 17):
                if i == 0:
                    l1 = r0
                    r1 = xor32(l0, f(r0, k[(len(k) - 1) - i]))
                    leftbuffer = l1
                    rightbuffer = r1
                elif i == 16:
                    ctext += ip_1f(rightbuffer + leftbuffer)
                else:
                    li = rightbuffer
                    ri = xor32(leftbuffer, f(rightbuffer, k[(len(k) - 1) - i]))
                    leftbuffer = li
                    rightbuffer = ri
        return bintostr(ctext)
    else:
        l0 = ip_change(binstr)[0]
        r0 = ip_change(binstr)[1]
        leftbuffer = ""
        rightbuffer = ""
        for i in range(0, 17):
            if i == 0:
                l1 = r0
                r1 = xor32(l0, f(r0, k[(len(k) - 1) - i]))
                leftbuffer = l1
                rightbuffer = r1
            elif i == 16:
                ctext += ip_1f(rightbuffer + leftbuffer)

            else:
                li = rightbuffer
                ri = xor32(leftbuffer, f(rightbuffer, k[(len(k) - 1) - i]))
                leftbuffer = li
                rightbuffer = ri
        return bintostr(ctext)


def decryptiondemo(binstr,keys):
    ctext = ""
    k = key(checkkey(keys))
    if len(binstr) > 64:
        strblock = []
        s = ""
        for i in range(0,len(binstr),64):
            strblock.append(binstr[i:i+64])
        for i in range(len(strblock)):
            l0 = ip_change(strblock[i])[0]
            r0 = ip_change(strblock[i])[1]
            leftbuffer = ""
            rightbuffer = ""
            for i in range(0, 17):
                if i == 0:
                    l1 = r0
                    r1 = xor32(l0, f(r0, k[(len(k) - 1) - i]))
                    leftbuffer = l1
                    rightbuffer = r1

                elif i == 16:
                    ctext += ip_1f(rightbuffer + leftbuffer)
                else:
                    li = rightbuffer
                    ri = xor32(leftbuffer, f(rightbuffer, k[(len(k) - 1) - i]))
                    leftbuffer = li
                    rightbuffer = ri

        return bintostr(ctext)
    else:
        l0 = ip_change(binstr)[0]
        r0 = ip_change(binstr)[1]
        leftbuffer = ""
        rightbuffer = ""
        for i in range(0, 17):
            if i == 0:
                l1 = r0
                r1 = xor32(l0, f(r0, k[(len(k) - 1) - i]))
                leftbuffer = l1
                rightbuffer = r1
            elif i == 16:
                ctext += ip_1f(rightbuffer + leftbuffer)
            else:
                li = rightbuffer
                ri = xor32(leftbuffer, f(rightbuffer, k[(len(k) - 1) - i]))
                leftbuffer = li
                rightbuffer = ri
        return bintostr(ctext)

'''
x = encryption("helloworld!","password")
print(encryption("helloworld!","password"))
print(decryption(x,"password"))

file = open('efile.txt','r',encoding='utf-8')
data = file.read().split(" ")
file.close()


wf = open("encrypted.txt",'w',encoding='utf-8')
for i in data:
    a = encryption(i, "password")
    wf.write(a)

wf.close()
'''














