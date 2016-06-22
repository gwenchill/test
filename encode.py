#coding:utf-8
from os import urandom
import hashlib

randata = urandom(256)
k = hashlib.md5(hashlib.sha512(randata).hexdigest()).hexdigest()[8:-8]
keystr = 'Key:' + k + ''
print keystr
f = open('key.txt', 'wb')
enc = ''
keystr=urandom(100)+keystr+urandom(100)
for c in keystr:
   enc+= hex(pow(ord(c), 0x2345678901, 243))[2:]

enc=enc.encode('base64').encode('zlib')
f.write(enc)
f.close()


