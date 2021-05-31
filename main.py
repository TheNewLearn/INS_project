import DES as des

file = open('efile.txt','r',encoding='utf-8')
data = file.read().split(" ")
file.close()



''''

writefile = open("encrypted.txt",'w',encoding='utf-8')
for i in data:
    e = des.encryption(i,"password","2")
    writefile.write(e+" ")
writefile.close()



file = open('encrypted.txt','r',encoding='utf-8')
datas = file.read().split(" ")
for i in range( len(datas)):
    if i< len(datas)-1:
        print(des.decryptiondemo(datas[i],"password"),end=" ")

'''



s = "hellowor"
k1 = "password"
k2 = "passwor1"
k3 = "passwor2"
#3DES
e1 = des.encryption(s,k1,"1")
e2 = des.decryption(e1,k2)
e3 = des.encryption(e2,k3,"1")
e4 = e3
print(e4)

#3DES decrypt
e5 = des.decryption(e4,k3)
e6 = des.encryption(e5,k2,"1")
e7 = des.decryption(e6,k1)
print(e7)
