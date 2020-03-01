from pwn import *
import base64

server = 'tasks.aeroctf.com'
port = 44323
form = '0123456789abcdef'
flag = '}'

for times in range(40):
    r = remote(server, port)
    check = False
    
    for ch in form:
        r.recv()
        r.sendline('3')
        r.recv()
        r.sendline(ch + flag[::-1].ljust(26+len(flag), '\x00' ))
        x = r.recvline().split(b'\'')[1]
        deco = base64.b64decode(x)

        for i in range(16):
            if deco[i] != deco[i+64]:
                break
            elif i == 15:
                flag += ch
                print('flag is {}'.format(flag[::-1]))
                check = True
                
        if check:
            break

    r.close()

print('Aero{' + flag[::-1])
# Aero{5013a76ed3b98bae1e79169b3495f47a}