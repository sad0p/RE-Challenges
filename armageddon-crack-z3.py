#!/usr/bin/env python3
 
# Solution for https://crackmes.one/crackme/5edb0b8533c5d449d91ae73b (Towel's Armageddon -- for ARM32)
# Requires z3 SMT solver
# install z3 with: pip install z3-solver

#$ ./armageddon-crack-z3.py
#<start>UMDCTF-{ARM_1s_s(_SATisfying_7y8fdlsjebnu</end>
#length: 41
#./armageddon   
#---------------
#-=UMDCTF 2019=-
#---------------
#[+] Enter Code: UMDCTF-{ARM_1s_s(_SATisfying_7y8fdlsjebnu
#
#[+] Code validated successfully!
#
#$ 



from z3 import *
 
def main():
    var_names = ''
    for i in range(0,41):
        var_names = var_names + 'i' + str(i) + ' '
 
    s = Solver()
    var_list = BitVecs(var_names, 32)
 
    s.add(var_list[0] >= 32, var_list[0] <= 127)
    s.add(var_list[1] >= 32, var_list[1] <= 127)
    s.add(var_list[2] >= 32, var_list[2] <= 127)
    s.add(var_list[3] >= 32, var_list[3] <= 127)
    s.add(var_list[4] >= 32, var_list[4] <= 127)
    s.add(var_list[5] >= 32, var_list[5] <= 127)
    s.add(var_list[6] >= 32, var_list[6] <= 127)
    s.add(var_list[7] >= 32, var_list[7] <= 127)
    s.add(var_list[8] >= 32, var_list[8] <= 127)
    s.add(var_list[9] >= 32, var_list[9] <= 127)
    s.add(var_list[10] >= 32, var_list[10] <= 127)
    s.add(var_list[11] >= 32, var_list[11] <= 127)
    s.add(var_list[12] >= 32, var_list[12] <= 127)
    s.add(var_list[13] >= 32, var_list[13] <= 127)
    s.add(var_list[14] >= 32, var_list[14] <= 127)
    s.add(var_list[15] >= 32, var_list[15] <= 127)
    s.add(var_list[16] >= 32, var_list[16] <= 127)
    s.add(var_list[17] >= 32, var_list[17] <= 127)
    s.add(var_list[18] >= 32, var_list[18] <= 127)
    s.add(var_list[19] >= 32, var_list[19] <= 127)
    s.add(var_list[20] >= 32, var_list[20] <= 127)
    s.add(var_list[21] >= 32, var_list[21] <= 127)
    s.add(var_list[22] >= 32, var_list[22] <= 127)
    s.add(var_list[23] >= 32, var_list[23] <= 127)
    s.add(var_list[24] >= 32, var_list[24] <= 127)
    s.add(var_list[25] >= 32, var_list[25] <= 127)
    s.add(var_list[26] >= 32, var_list[26] <= 127)
    s.add(var_list[27] >= 32, var_list[27] <= 127)
    s.add(var_list[28] >= 32, var_list[28] <= 127)
    s.add(var_list[29] >= 32, var_list[29] <= 127)
    s.add(var_list[30] >= 32, var_list[30] <= 127)
    s.add(var_list[31] >= 32, var_list[31] <= 127)
    s.add(var_list[32] >= 32, var_list[32] <= 127)
    s.add(var_list[33] >= 32, var_list[33] <= 127)
    s.add(var_list[34] >= 32, var_list[34] <= 127)
    s.add(var_list[35] >= 32, var_list[35] <= 127)
    s.add(var_list[36] >= 32, var_list[36] <= 127)
    s.add(var_list[37] >= 32, var_list[37] <= 127)
    s.add(var_list[38] >= 32, var_list[38] <= 127)
    s.add(var_list[39] >= 32, var_list[39] <= 127)
    s.add(var_list[40] >= 32, var_list[40] <= 127)
 
    s.add((((var_list[1] * (var_list[39] * var_list[21])) + var_list[17]) + (var_list[19] * var_list[30])) == 0xDB11E) #1st check
    s.add((var_list[37] - (var_list[19]  * var_list[12])) == 0xFFFFF3F4) #2nd check
    s.add(((var_list[2] - var_list[31]) + (var_list[33] * (var_list[13] * var_list[20])) - var_list[17]) == 0xEBD1D) #3rd check 
    s.add(((var_list[7] + (var_list[36] * var_list[15]))  -  (var_list[29] * var_list[34])) == 0x18E5) #4th check
    s.add(((var_list[21] - (var_list[27] * var_list[15])) - var_list[17]) == 0xFFFFD1C5) #5th check
    s.add((((var_list[15] - (var_list[37] * var_list[8])) - var_list[5]) - var_list[6]) == 0xFFFFE65B) #6th check
    s.add((((var_list[35] + var_list[29]) - var_list[20])  + var_list[26]) == 0xC4) #7th check
    s.add(((var_list[7] * var_list[32]) + (var_list[31] * var_list[11])) == 0x45CA) #8th check
    s.add(((var_list[29] * (var_list[24] * var_list[36])) + var_list[37]) == 0xAC3FB) #9th check
    s.add(((((var_list[8] - var_list[16]) - var_list[12]) + var_list[40]) + var_list[15]) == 0xD0) #10th check
    s.add(((((var_list[17] * var_list[0]) * var_list[35]) - var_list[11]) + (var_list[12] * (var_list[7] * var_list[38]))) == 0x172E48) #11th check
    s.add((((var_list[26] - var_list[13]) + (var_list[3] * var_list[8])) - var_list[5]) == 0x10B8) #12th check
    s.add((((var_list[3] + var_list[17]) + var_list[36]) + var_list[20]) == 0x160) #13th check
    s.add(((var_list[26] - (var_list[21] * var_list[18])) + (var_list[27] * var_list[25])) == 0x8A2) #14th check    
    s.add((((var_list[34] - var_list[14]) + (var_list[5] * var_list[33])) + var_list[35]) == 0x1BD8) #15th check
    s.add((((var_list[5] * (var_list[8] * (var_list[38] * var_list[25]))) + var_list[21]) + var_list[35]) == 0x2CA6988) #16th check    
    s.add((((var_list[8] * var_list[8]) + (var_list[21] * var_list[12])) - var_list[36]) == 0x2430) #17th check    
    s.add(((((var_list[35] + var_list[2]) - var_list[7]) - (var_list[9] * var_list[18])) + (var_list[2] * var_list[39])) == 0x2DE) #18th check
    s.add(((((var_list[5] * (var_list[17] - 1)) - var_list[6]) - var_list[20]) - (var_list[34] * var_list[23])) == 0xFFFFEE2B) #19th check
    s.add(((var_list[34] - var_list[11]) + (var_list[11] * var_list[13])) == 0x2ABA) #20th check
    s.add((((var_list[27] + (var_list[18] * var_list[15])) + var_list[32]) + var_list[9]) == 0x2668) #21st check
    s.add((var_list[21] - (var_list[14] * var_list[29])) == 0xFFFFEC00) #22nd check 
    s.add((((((var_list[9] * var_list[9]) - var_list[10]) + var_list[13]) - var_list[36]) - var_list[20]) == 0x19AC) #23rd check
    s.add(var_list[12] + var_list[2] + var_list[34] - var_list[4] * var_list[20] * var_list[23] + var_list[22] == 0xFFF505F4) #24th check
    s.add(var_list[4] + var_list[5] - var_list[10] + var_list[27] == 0xB4) #25th check
    s.add(var_list[15] - var_list[28] - var_list[37] - var_list[24] * var_list[18] * var_list[0] == 0xFFF2F918) #26th check
    s.add(var_list[4] * var_list[35] + var_list[25] - var_list[21] - var_list[24] * var_list[20] == 0xFFFFFE08) #27th check 
    s.add(var_list[25] + var_list[10] - var_list[15] + var_list[28] - var_list[33] == 0x3E) #28th check
    s.add(var_list[6] - var_list[25] + var_list[2] - var_list[25] + var_list[1] + var_list[18] * var_list[28] == 0x1EB9) #29th check   
    s.add(var_list[11] * (var_list[5] + var_list[34] * var_list[22]) + var_list[12] + var_list[34] == 0x121B93) #30th check
    s.add(var_list[3] + var_list[14] - var_list[38] - var_list[13] - var_list[1] == 0xFFFFFF80) #31st check
    s.add(var_list[30] + var_list[21] - var_list[17] - var_list[23] * var_list[5] + var_list[33] == 0xFFFFE503) #32nd check
    s.add(var_list[7] - var_list[14] + var_list[17] + var_list[33] == 0xDF) #33rd check
    s.add(var_list[8] - var_list[3] + var_list[2] * var_list[10] * var_list[10] == 0x626E2) #34th check
    s.add(var_list[37] + var_list[7] - var_list[19] + var_list[12] + var_list[11] == 0x12F) #35th check
    s.add(var_list[1] + var_list[8] * var_list[20] + var_list[32] + var_list[15] == 0x167A) #36th check
    s.add(var_list[17] - var_list[4] - var_list[29] * var_list[18] == 0xFFFFEE36) #37th check
    s.add(var_list[13] * var_list[22] - var_list[10] - var_list[35] == 0x32E9) #38th check
    s.add(var_list[13] + var_list[11] + var_list[29] * var_list[19] == 0xEC9) #39th check
    s.add(var_list[25] + var_list[38] * var_list[15] - var_list[11] + var_list[32] - var_list[21] * var_list[34] == 0x2A) #40th check
    s.add(var_list[6] * var_list[9] + var_list[35] == 0xEDD) #41nd check

    
    check_result = s.check()
 
    #print(f"[+] check:  => {check_result}")
    if check_result == z3.sat:
        print_string(var_list, s)
    else:
        print("no solution")
 
def print_string(var_list, s):
    count = 0
    print("<start>", end='')
    for v in var_list:
        m = s.model()
        value = m[v]
        if value is not None:
            count = count + 1
            print(chr(value.as_long()), end='')
    print("</end>")
    print(f"length: {count}")


if __name__ == '__main__':
    main()
 

