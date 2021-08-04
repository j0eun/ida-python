from idc_bc695 import *

def get_str(ea):
    s = []
    i = 0
    while Byte(ea+i) != 0:
        s.append(Byte(ea+i))
        i += 1

    return s 

def decode(ea_encoded):
    decoded = []
    encoded = get_str(ea_encoded)
    length = len(ea_encoded)
    xorkey = 0xff
    for e in encoded:
        decoded.append(e ^ xorkey)
    for i in range(length):
        PatchByte(ea_encoded+i, decoded[i])
    create_strlit(ea_encoded, ea_encoded+length)


func_decode = LocByName('sub_1400010C0')
gen_xrefs = XrefsTo(func_decode, 0)
for x in gen_xrefs:
    if GetMnem(x.frm) == 'call':
        var_name = GetOpnd(x.frm - 0x11, 1)
        ea_encoded = LocByName(var_name)
        decode(ea_encoded)
        for ea in range(x.frm-10, x.frm+5):
            PatchByte(ea, 0x90)

        
