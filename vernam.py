import random
import string

def key_gen(_len: int,  pool: str = string.ascii_letters):
  key = ''.join(random.choices(pool, k=_len))
  return key

def vern_byte(data,key):
    data_bin = str(bin(ord(data))).lstrip('0b')
    key_bin = str(bin(ord(key))).lstrip('0b')
    while len(data_bin) != len(key_bin):
      if len(key_bin) < len(data_bin):
        key_bin = '0'+key_bin                                                                                                                 
      else:
        data_bin = '0'+data_bin
    shifr_bin = ''.join(str(int(data_bin[i]) ^ int(key_bin[i])) for i in range(len(data_bin)))
    out_data = chr(int(shifr_bin,2))
    return  out_data

print('Что делать?(0 - зашифровать/1 - расшифровать)')
var = input()
if var == '0':

    df = open("text.txt","r")
    data = df.read().encode("cp1251").decode("utf-8")
    df.close()
    print("Входящие данные")
    print(data)

    key = key_gen(len(data))
    kf = open("key.txt","w",encoding = 'utf-8')
    kf.write(key)
    kf.close()
    print("ключ")
    print(key)

    shifr =''.join(vern_byte(data[i],key[i]) for i in range(len(data)))
    print ("шифр")
    print (shifr)
    sh = open("shifr.txt","w",encoding = 'utf-8')
    sh.write(shifr)
    sh.close()
else:
    df = open("shifr.txt","r",encoding = 'utf-8')
    data = df.read()
    df.close()
    print("Входящие данные")
    print(data)

    kf = open("key.txt","r",encoding = 'utf-8')
    key = kf.read()
    kf.close()
    print("ключ")
    print(key)

    shifr =''.join(vern_byte(data[i],key[i]) for i in range(len(data)))
    sh = open("deshifr.txt","w",encoding = 'utf-8')
    sh.write(shifr)
    sh.close()
    print ("Расшифровка")
    print (shifr)




