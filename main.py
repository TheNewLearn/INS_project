import AES as aes

file = open('efile.txt','r',encoding='utf-8')
data = file.read().split(" ")
file.close()





writefile = open("encrypted.txt",'w',encoding='utf-8')
for i in data:
    #print(aes.encryption(i,"password"))
    e = aes.encryption(i,"password")
    writefile.write(e)
#print(type(data[77][7:8])
#writefile.close()




#file = open('encrypted.txt','r',encoding='utf-8')
#datas = file.read().split(" ")
#for i in datas:
    #print(aes.decryptiondemo(i,"password"),end=" ")
