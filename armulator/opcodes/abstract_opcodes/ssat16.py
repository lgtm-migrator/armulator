from armulator.opcodes.abstract_opcode import AbstractOpcode
from armulator.bits_ops import signed_sat_q, sign_extend


class Ssat16(AbstractOpcode):
    def __init__(self, saturate_to, d, n):
        super(Ssat16, self).__init__()
        self.saturate_to = saturate_to
        self.d = d
        self.n = n

    def execute(self, processor):
        if processor.condition_passed():
            result1, sat1 = signed_sat_q(processor.core_registers.get(self.n)[16:32].int, self.saturate_to)
            result2, sat2 = signed_sat_q(processor.core_registers.get(self.n)[0:16].int, self.saturate_to)
            processor.core_registers.set(self.d, sign_extend(result2, 16) + sign_extend(result1, 16))
            if sat1 or sat2:
                processor.core_registers.cpsr.set_q(True)
