import struct

class ItemSlot:
    def __init__(self, raw):
        t = struct.unpack("<HH", raw)
        self.id = t[0]
        self.quantity = t[1]

    def __str__(self) -> str:
        return "id:{: 3} 0x{:04X} qtt:{}".format(self.id, self.id, self.quantity)
