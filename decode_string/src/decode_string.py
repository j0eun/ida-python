from idc_bc695 import *

def get_str(ea):
    s = []
    i = 0
    while Byte(ea+i) != 0:
        s.append(Byte(ea+i))
        i += 1

    return s 

# 난독화 해제 함수 슈도코드를 분석하여 Python 스크립트로 포팅
# 난독화 해제 알고리즘은 바이너리마다 다르기에 그때그때 분석해서 decode 함수를 채워줘야 함
def decode(ea_encoded):
    decoded = []
    encoded = get_str(ea_encoded)
    length = len(encoded)
    xorkey = 0xff
    for e in encoded:
        decoded.append(e ^ xorkey)
    for i in range(length):
        PatchByte(ea_encoded+i, decoded[i])         # 디코딩시킨 문자열로 패치
    create_strlit(ea_encoded, ea_encoded+length)    # idb에서 바이트 배열 문자열로 정의


# 디코딩시킨 문자열을 가지고 또다시 디코딩 함수를 호출하는 일이 없도록 패치해준다.
# opcode를 파싱할 때 쓰이는 오프셋이 바이너리마다 다르니 계산 필요
func_decode = LocByName('sub_1400010C0')            # 난독화 해제 함수
gen_xrefs = XrefsTo(func_decode, 0)
for x in gen_xrefs:
    if GetMnem(x.frm) == 'call':
        var_name = GetOpnd(x.frm - 0x11, 1)
        ea_encoded = LocByName(var_name)
        decode(ea_encoded)
        for ea in range(x.frm-10, x.frm+5):
            PatchByte(ea, 0x90)                     # 필요 없는 부분은 NOP으로 패치


        
