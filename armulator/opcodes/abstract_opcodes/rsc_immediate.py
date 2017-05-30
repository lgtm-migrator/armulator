from armulator.opcodes.abstract_opcode import AbstractOpcode
from armulator.bits_ops import add_with_carry


class RscImmediate(AbstractOpcode):
    def __init__(self, setflags, d, n, imm32):
        super(RscImmediate, self).__init__()
        self.setflags = setflags
        self.d = d
        self.n = n
        self.imm32 = imm32

    def execute(self, processor):
        if processor.condition_passed():
            result, carry, overflow = add_with_carry(~processor.core_registers.get(self.n), self.imm32,
                                                     processor.core_registers.cpsr.get_c())
            if self.d == 15:
                processor.alu_write_pc(result)
            else:
                processor.core_registers.set(self.d, result)
                if self.setflags:
                    processor.core_registers.cpsr.set_n(result[0])
                    processor.core_registers.cpsr.set_z(result.all(False))
                    processor.core_registers.cpsr.set_c(carry)
                    processor.core_registers.cpsr.set_v(overflow)
