import xxtea
import string
import random

#key = os.urandom(16) # Key must be a 16-byte string.
#in_data = "xxtea is good"

#shifr = xxtea.encrypt_hex(in_data, key)
#deshifr = xxtea.decrypt_hex(shifr, key)
#print(in_data)
#print(shifr)
#print(deshifr)

def key_gen(_len: int,  pool: str = string.ascii_letters):
  key = ''.join(random.choices(pool, k=_len))
  return key

print('Что делать?(0 - зашифровать/1 - расшифровать)')
var = input()
if var == '0':

    df = open("text.txt","r")
    data = df.read().encode("cp1251").decode("utf-8")
    df.close()
    print("Входящие данные")
    print(data)

    key = key_gen(16)
    kf = open("key.txt","w",encoding = 'utf-8')
    kf.write(key)
    kf.close()
    print("ключ")
    print(key)

    shifr = xxtea.encrypt_hex(data, key.encode('utf-8'))
    print ("шифр")
    print (shifr.decode('utf-8'))
    sh = open("shifr.txt","w",encoding = 'utf-8')
    sh.write(shifr.decode('utf-8'))
    sh.close()
else:
    df = open("shifr.txt","r")
    data = df.read().encode('utf-8')
    df.close()
    print("Входящие данные")
    print(data)

    kf = open("key.txt","r")
    key = kf.read().encode('utf-8')
    kf.close()
    print("ключ")
    print(key)

    shifr = xxtea.decrypt_hex(data, key)
    sh = open("deshifr.txt","w",encoding = 'utf-8')
    sh.write(shifr.decode('utf-8'))
    sh.close()
    print ("Расшифровка")
    print (shifr.decode('utf-8'))
