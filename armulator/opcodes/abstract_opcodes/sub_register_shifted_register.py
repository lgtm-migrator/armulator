from armulator.opcodes.abstract_opcode import AbstractOpcode
from armulator.shift import shift
from armulator.bits_ops import add_with_carry


class SubRegisterShiftedRegister(AbstractOpcode):
    def __init__(self, setflags, m, s, d, n, shift_t):
        super(SubRegisterShiftedRegister, self).__init__()
        self.setflags = setflags
        self.m = m
        self.s = s
        self.d = d
        self.n = n
        self.shift_t = shift_t

    def execute(self, processor):
        shift_n = processor.core_registers.get(self.s)[24:32].uint
        shifted = shift(processor.core_registers.get(self.m), self.shift_t, shift_n,
                        processor.core_registers.cpsr.get_c())
        result, carry, overflow = add_with_carry(processor.core_registers.get(self.n), ~shifted, "1")
        processor.core_registers.set(self.d, result)
        if self.setflags:
            processor.core_registers.cpsr.set_n(result[0])
            processor.core_registers.cpsr.set_z(not result.any(True))
            processor.core_registers.cpsr.set_c(carry)
            processor.core_registers.cpsr.set_v(overflow)
