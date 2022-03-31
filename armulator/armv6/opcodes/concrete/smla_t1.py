from armulator.armv6.bits_ops import substring, bit_at
from armulator.armv6.opcodes.abstract_opcodes.smla import Smla


class SmlaT1(Smla):
    @staticmethod
    def from_bitarray(instr, processor):
        rm = substring(instr, 3, 0)
        rd = substring(instr, 11, 8)
        ra = substring(instr, 15, 12)
        rn = substring(instr, 19, 16)
        m_high = bit_at(instr, 4)
        n_high = bit_at(instr, 5)
        if rd in (13, 15) or rn in (13, 15) or rm in (13, 15) or ra == 13:
            print('unpredictable')
        else:
            return SmlaT1(instr, m_high=m_high, n_high=n_high, m=rm, a=ra, d=rd, n=rn)
