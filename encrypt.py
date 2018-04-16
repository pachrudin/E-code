#!/usr/bin/python 

import base64
import sys
from time import sleep

try:
	import base64
except ImportError:
	tampil('\033[1;35[\033[0m\033[1;31m!\033[0m\033[1;35m]\033[0mSepertiNya Module \033[1;31m Base64 belum di install...')

print """
\033[1;31m###########################################\033[0m
\033[1;33m#\033[0m Author: \033[1;31mMR.R45K1N\033[0m
\033[0m\033[1;33m#\033[0m Team  : \033[1;33mBlackHole Security\033[0m
\033[1;33m#\033[0m Kode  : \033[1;32mPython\033[0m
\033[1;32m###########################################\033[0m"""
print

print """[1] Encrypt
[2] Decrypt
[0] Exit"""
print

Pilih = raw_input("\033[1;32mPilih:\033[0m")
print 

if Pilih == '1' or Pilih == '01':
  str = raw_input("\033[1;32mYour text:\033[0m")
  print "\033[1;32mHasil    :\033[0m" + str.encode('base64','strict')
  file = open("result.txt", 'a')
  file.write(str)
  file.close()

  print "\033[1;31mManaged saved file named  result.txt\033[0m"

if Pilih == '2' or Pilih == '02':
  str = raw_input("\033[1;32mYour text:\033[0m")
  print "\033[1;32mHasil    :\033[0m" + str.decode('base64','strict')
  file = open("result.txt", 'a')
  file.write(str)
  file.close()

  print "\033[1;31mManaged saved file named result.txt\033[0m"


if Pilih == '0' or Pilih == '00':
  print "\033[1;31m:*Thanks All\033[0m \033[1;33mMember\033[0m \033[1;32mBlackHole Security:*\033[0m"
  sleep(2)
  sys.exit()