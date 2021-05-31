import numpy as np
import base64

s_box = [
    ["63","7c" ,"77", "7b","f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab" ,"76"],
    ["ca","82","c9","7d","fa","59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
    ["b7","fd", "93" ,"26" ,"36" ,"3f" ,"f7" ,"cc" ,"34" ,"a5" ,"e5" ,"f1", "71" ,"d8", "31" ,"15"],
    ["04","c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"],
    ["09","83"," 2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],
    ["53","d1", "00", "ed", "20", "fc", "b1", "5b", "6a","cb", "be", "39", "4a","4c","58", "cf"],
    ["d0","ef", "aa", "fb", "43", "4d" ,"33", "85" ,"45", "f9", "02" ,"7f" ,"50" ,"3c", "9f", "a8"],
    ["51","a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6" ,"da" ,"21", "10", "ff", "f3", "d2"],
    ["cd","0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d" ,"64" ,"5d", "19", "73"],
    ["60","81", "4f", "dc", "22", "2a" ,"90", "88", "46", "ee", "b8" ,"14", "de" ,"5e" ,"0b" ,"db"],
    ["e0","32", "3a", "0a", "49", "06" ,"24", "5c", "c2", "d3" ,"ac", "62" ,"91" ,"95" ,"e4", "79"],
    ["e7","c8" ,"37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4" ,"ea", "65" ,"7a", "ae", "08"],
    ["ba","78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f" ,"4b", "bd", "8b" ,"8a"],
    ["70","3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57" ,"b9" ,"86" ,"c1", "1d", "9e"],
    ["e1","f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"],
    ["8c","a1", "89", "0d", "bf", "e6" ,"42", "68", "41", "99" ,"2d", "0f", "b0" ,"54", "bb", "16"]
]


def subbyte(list4x4):
    hex4 = []
    row = ''
    col = ''
    newsb = []
    for i in range(len(list4x4)):
        hex4.append([])
        for j in range(len(list4x4[i])):
            hex4[i].append(hex(int(list4x4[i][j],2))[2:].zfill(2))
    for i in range(len(hex4)):
        newsb.append([])
        for j in range(len(hex4[i])):
            row = int(hex4[i][j][0], 16)
            col = int(hex4[i][j][1], 16)
            value = s_box[row][col]
            newsb[i].append(bin(int(value,16))[2:].zfill(8))
    return newsb


def gs_boxlookup(listw):
    hexlist = []
    row = ""
    col = ""
    lookuplist = []
    for i in listw:
        hexlist.append(hex(int(i,2))[2:].zfill(2))
    for i in hexlist:
        row = int(i[0],16)
        col = int(i[1], 16)
        lookuplist.append(s_box[row][col])
    s0 = bin(int(lookuplist[0],16))[2:].zfill(8)
    s1 = bin(int(lookuplist[1],16))[2:].zfill(8)
    s2 = bin(int(lookuplist[2],16))[2:].zfill(8)
    s3 = bin(int(lookuplist[3],16))[2:].zfill(8)
    return s0+s1+s2+s3

def xor32(s,f):
    xor = ''
    if len(s) == 32:
        for i in range(len(s)):
            if i < len(s):
                xor += str(int(s[i:i + 1], 10) ^ int(f[i:i + 1], 10))
    return xor


def nblock(string):
    bstr = ""
    block = []
    for i in string:
        bstr+= bin(ord(i))[2:].zfill(8)
    for i in range(0, len(bstr), 8):
        block.append(bstr[i:i + 8])
    return block



def keytobin(key):
    bstr = ""
    kb = []
    for i in key:
        bstr += bin(ord(i))[2:].zfill(8)
    for i in range(0,len(bstr),8):
        kb.append(bstr[i:i+8])
    return kb

def keyarray(k):
    kb = []
    for i in range(0,len(k),8):
        kb.append(k[i:i+8])
    return kb



def lsi(lst, k):
    return lst[k:] + lst[:k]

def xor(i,a):
    xor = ""
    for count in range(len(i)):
        if count<len(i):
            xor+=str(int(i[count:count+1])^int(a[count:count+1]))
    return xor


def kb4x4(k):
    k4b = np.array(k)
    k4b = k4b.reshape(4,4)
    return k4b.transpose()

def pt4x4(pt):
    ptb = np.array(pt)
    ptb = ptb.reshape(4,4)
    return ptb.transpose()


def keyr0(list4x4):
    w0 = list4x4[0][0] + list4x4[1][0] + list4x4[2][0] + list4x4[3][0]
    w1 = list4x4[0][1] + list4x4[1][1] + list4x4[2][1] + list4x4[3][1]
    w2 = list4x4[0][2] + list4x4[1][2] + list4x4[2][2] + list4x4[3][2]
    w3 = list4x4[0][3] + list4x4[1][3] + list4x4[2][3] + list4x4[3][3]
    return w0,w1,w2,w3


mix_table = [
    [0x02,0x03,0x01,0x01],
    [0x01,0x02,0x03,0x01],
    [0x01,0x01,0x02,0x03],
    [0x03,0x01,0x01,0x02]
]

rc = ["01","02","04","08","10","20","40","80","1B","36"]

def g(w3,rc):
    w3b = []
    for i in range(0,len(w3),8):
        w3b.append(w3[i:i+8])
    w3b = lsi(w3b,1)
    sb = gs_boxlookup(w3b)
    xrc = bin(int(rc,16))[2:].zfill(32)
    wi = xor32(sb,xrc)
    return wi

def genkeyi(w0,w1,w2,w3):
    keylist = []
    for i in range(len(rc)):
        w4 = xor32(g(w3,rc[i]),w0)
        w5 = xor32(w4,w1)
        w6 = xor32(w5,w2)
        w7 = xor32(w6,w3)
        keylist.append(w4+w5+w6+w7)
        w0 = w4
        w1 = w5
        w2 = w6
        w3 = w7
    return keylist

def addroundkey(pt4x4,key):
    k = []
    newarr = []
    for i in range(0, len(key), 8):
        k.append(key[i:i + 8])
    k4x4 = kb4x4(k)
    for i in range(len(pt4x4)):
        newarr.append([])
        for j in range(len(pt4x4[i])):
            newarr[i].append(xor(pt4x4[i][j],k4x4[i][j]))
    return newarr

def addroundkey2(pt4x4,key):
    newarr = []
    for i in range(len(pt4x4)):
        newarr.append([])
        for j in range(len(pt4x4[i])):
            newarr[i].append(hex(int(xor(bin(pt4x4[i][j])[2:].zfill(8),bin(key[i][j])[2:].zfill(8)),2)))
    return newarr

def shiftrows(list4x4):
    for i in range(len(list4x4)):
        if i>0:
            list4x4[i] = lsi(list4x4[i],i)
    return list4x4


def multiply(b,a):
    if b == 1:
        return a
    tmp = (a<<1) & 0xff
    if b == 2:
        return tmp if a < 127 else tmp^0x1b
    if b == 3:
        return tmp^a if a < 127 else (tmp^0x1b)^a


def mixcolumn(list4x4):
    new4x4 = []
    for i in range(len(list4x4)):
        col1 = int(list4x4[0][i],2)
        col2 = int(list4x4[1][i],2)
        col3 = int(list4x4[2][i],2)
        col4 = int(list4x4[3][i],2)
        new4x4.append([])
        for j in range(len(list4x4[i])):
            t1 = bin(multiply(mix_table[j][0], col1))[2:].zfill(8)
            t2 = bin(multiply(mix_table[j][1], col2))[2:].zfill(8)
            t3 = bin(multiply(mix_table[j][2], col3))[2:].zfill(8)
            t4 = bin(multiply(mix_table[j][3], col4))[2:].zfill(8)
            t5 = xor(t1, t2)
            t6 = xor(t3, t4)
            t7 = xor(t5, t6)
            new4x4[i].append(t7)

    npt = np.array(new4x4)
    npt = npt.transpose()
    return npt





def encryption(pt,keys):
    lstr = []
    nb = nblock(pt)
    nb4x4 = pt4x4(nb)
    r0key = keyr0(kb4x4(keytobin(keys)))
    k4x4 = kb4x4(keytobin(keys))
    genkey = genkeyi(r0key[0],r0key[1],r0key[2],r0key[3])
    addround0 = addroundkey(nb4x4,k4x4)
    for i in range(0,9):
        sb = subbyte(addround0)
        shf = shiftrows(sb)
        mic = mixcolumn(shf)
        ki4x4 = kb4x4(keyarray(genkey[i]))
        addri = addroundkey(mic,ki4x4)
        addround0 = addri
        lstr = addri
    finsb = subbyte(lstr)
    finsh = shiftrows(finsb)
    finalk = kb4x4(keyarray(genkey[9]))
    finaddr = addroundkey(finsh,finalk)
    return b4x4tostr(finaddr)



def b4x4tostr(list4x4):
    str=""
    for i in range(len(list4x4)):
        str+= bintostr(list4x4[i][0])
    for i in range(len(list4x4)):
        str+= bintostr(list4x4[i][1])
    for i in range(len(list4x4)):
        str+= bintostr(list4x4[i][2])
    for i in range(len(list4x4)):
        str+= bintostr(list4x4[i][3])
    return str

def bintostr(strs):
    s = ""
    s+= strs
    return s


a = str(0b00011011).encode("utf-8")

def bts(bin):
    s = ""
    for i in range(0,len(bin),8):
        s+= hex(int(bin[i:i+8],2))[2:]
    return s


a = encryption("helloworldtexthl","passwordlasheras")
print(bts(a))














