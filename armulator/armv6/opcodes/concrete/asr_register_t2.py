from armulator.armv6.bits_ops import substring, bit_at
from armulator.armv6.opcodes.abstract_opcodes.asr_register import AsrRegister


class AsrRegisterT2(AsrRegister):
    @staticmethod
    def from_bitarray(instr, processor):
        rm = substring(instr, 3, 0)
        rd = substring(instr, 11, 8)
        rn = substring(instr, 19, 16)
        setflags = bit_at(instr, 20)
        if rd in (13, 15) or rn in (13, 15) or rm in (13, 15):
            print('unpredictable')
        else:
            return AsrRegisterT2(instr, setflags=setflags, m=rm, d=rd, n=rn)
