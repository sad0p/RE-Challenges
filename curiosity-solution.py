# Challenge: https://cdn.discordapp.com/attachments/779090563680829509/867294592503382036/Challenge.zip

import sys

counter_moved = False
jmp_count = 0
s_count = 1
count = 0
REG_0 = 0
REG_1 = 1
REG_2 = 2
REG_3 = 3
reg_ptr = [0, 0, 0, 0]
contents = []
gen_output = 0
flag = []
fh = open("disassembly.txt", mode="w+")

    
def print_regs():
    print(
        f"\t\t\t\t\t\treg_0 = {hex(reg_ptr[REG_0])} reg_1 = {hex(reg_ptr[REG_1])}"
        f" reg_2 = {hex(reg_ptr[REG_2])} reg_3 = {hex(reg_ptr[REG_3])}",
        file=fh)

def syscall():
    global reg_ptr, count, s_count    
    if reg_ptr[REG_0] == 1:
        print("Syscall_write()", file=fh)
        return print(chr(reg_ptr[REG_1] & 0xff), flush=True, end='')
    if reg_ptr[REG_0] == 2:
        print("Syscall_exit()", file=fh)
        for c in flag:
            print(c, end='')

        sys.exit(reg_ptr[REG_1])
    
    #reg_ptr[REG_0] = ord(sys.stdin.read(1))
    reg_ptr[REG_0] = ord(chr(gen_output))
    print(f"Syscall_read() // {s_count}", file=fh)
    s_count = s_count + 1

#mov reg, mem            
def instruction_one():
    global count, reg_ptr, counter_moved
    reg_index = contents[count] & 3
    count = count + 1
    b = int.from_bytes(contents[count : count + 2], "little")
    print(f"mov reg[{reg_index}], {hex(b)}", file=fh)

    reg_ptr[reg_index] = b 
    count = count + 1
    counter_moved = True

#mov reg1, reg2    
def instruction_two():
    global reg_ptr
    print(f"mov reg[{contents[count] & 3}], reg[{(contents[count] >> 2) & 3}]", file=fh)
    reg_index_one = contents[count] & 3
    reg_index_two = (contents[count] >> 2) & 3
    reg_ptr[reg_index_one] = reg_ptr[reg_index_two]
        
#add reg, mem
def instruction_three():
    global count, reg_ptr, counter_moved
    reg_index = contents[count] & 3
    count = count + 1
    b = int.from_bytes(contents[count : count + 2], "little")
    print(f"add reg[{contents[count] & 3}], {hex(b)}", file=fh)
    reg_ptr[reg_index] = (reg_ptr[reg_index] + b) & 0xffff
    count = count + 1
    counter_moved = True
    
#not reg
def instruction_four():
    global reg_ptr
    print(f"not reg[{contents[count] & 3}]", file=fh)
    reg_index = contents[count] & 3
    reg_ptr[reg_index] = ~reg_ptr[reg_index] 
    
#imul reg, mem
def instruction_five():
    global count, reg_ptr, counter_moved
    reg_index = contents[count] & 3
    count = count + 1
    b = int.from_bytes(contents[count : count + 2], "little")
    print(f"imul reg[{reg_index}], {hex(b)}", file=fh)
    reg_ptr[reg_index] = (reg_ptr[reg_index] * b) & 0xffff
    count = count + 1
    counter_moved = True
    
#jmp instruction / set count
def instruction_six():
    global count
    if reg_ptr[REG_0]:
        print(f"set count = {reg_ptr[REG_1] - 1}", file=fh)
        count = reg_ptr[REG_1] - 1
    
#add reg1, reg2
def instruction_seven():
    global reg_ptr
    print(f"add reg[{contents[count] & 3}], reg[{(contents[count] >> 2) & 3}]", file=fh)
    reg_index_one = contents[count] & 3
    reg_index_two = (contents[count] >> 2) & 3
    reg_ptr[reg_index_one] = (reg_ptr[reg_index_one] + reg_ptr[reg_index_two]) & 0xffff

def exec_instruction(v):
    global jmp_count
    if v == 1:
        instruction_one()
    elif v == 2:
        instruction_two()            
    elif v == 3:
        instruction_three()
    elif v == 4:
        instruction_four()
    elif v == 5:
        instruction_five()
    elif v == 6:
        instruction_six()
        jmp_count = jmp_count + 1
    elif v == 7:
        instruction_seven()
    elif v == 0:
        pass    

def main():
    global count, contents, gen_output, counter_moved
    print("virtualization world!")
    
    if len(sys.argv) != 2:
        print("needs a target to emulate")
        sys.exit(1)
    
    target = sys.argv[1]
    with open(target, mode='rb') as fh:
        contents = fh.read()
    
    #0x20 - 0x60 is the printable ascii range
    emu_input = 0x20
    sys_offset = 0
    last_letter = False
    while(True):
        while(True):
            print_regs()
            if contents[count] == 0xff and not last_letter:
                if ((reg_ptr[REG_3] & 0xffff) != 0) and (reg_ptr[REG_0] != 1) and (reg_ptr[REG_0] != 2):
                    sys_offset = count
                    if counter_moved and not last_letter:
                        count = count - 1
                        while contents[count] != 0xff:
                            count = count - 1
                        counter_moved = False
                    reg_ptr[REG_3] = 0x0
                    break
                elif count >= sys_offset and sys_offset != 0:
                    flag.append(chr(emu_input))
                    emu_input = 0x20

                gen_output = emu_input
                syscall()
            
            if contents[count] == 0xff and last_letter:
                while(True):
                    print_regs()
                    gen_output = emu_input
                    if contents[count] == 0xff:
                        syscall()
                    
                    # look for jmp instruction...
                    if (contents[count] >> 4) == 6:
                        if (reg_ptr[REG_3] & 0xffff) == 0:
                            flag.append(chr(emu_input))
                            last_letter = False
                            break
                        else:
                            emu_input = emu_input + 1
                            reg_ptr[REG_3] = 0x0
                            reg_ptr[REG_1] = -0xe0
                            count = sys_offset
                            continue

                    exec_instruction(contents[count] >> 4)
                    count = count + 1

            v = contents[count] >> 4
            exec_instruction(v)
            if reg_ptr[REG_1] == 0x67 and jmp_count == 1:
                reg_ptr[REG_3] = 0x0
                reg_ptr[REG_1] = -0xe0
                count = sys_offset
                emu_input = 0x20
                last_letter = True
                continue
            count = count + 1
        emu_input = emu_input + 1
            
if __name__ == '__main__':
    main()