from armulator.opcodes.abstract_opcode import AbstractOpcode


class BicImmediate(AbstractOpcode):
    def __init__(self, setflags, d, n, imm32, carry):
        super(BicImmediate, self).__init__()
        self.setflags = setflags
        self.d = d
        self.n = n
        self.imm32 = imm32
        self.carry = carry

    def execute(self, processor):
        if processor.condition_passed():
            result = processor.core_registers.get(self.n) & ~self.imm32
            if self.d == 15:
                processor.alu_write_pc(result)
            else:
                processor.core_registers.set(self.d, result)
                if self.setflags:
                    processor.core_registers.cpsr.set_n(result[0])
                    processor.core_registers.cpsr.set_z(result.all(False))
                    processor.core_registers.cpsr.set_c(self.carry)
