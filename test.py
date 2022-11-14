import sys
import struct


def check_empty_save(save: list) -> bool:
    for byte in save:
        if byte != 0xFF:
            return False
    return True


class Section:
    def __init__(self, section):
        self.raw = section
        t = struct.unpack("<hHll", self.raw[0xFF4:0x1000])
        self.id = t[0]
        self.checksum = t[1]
        self.sig = t[2]
        self.save_idx = t[3]

    def __str__(self) -> str:
        return "Section: id: {:02d}, checksum: {:05d} {:04X}, sig: {:04X}, save idx: {:01X}".format(
            self.id, self.checksum, self.checksum, self.sig, self.save_idx
        )


class Save:
    def __init__(self, save: list):
        self.raw = save
        self.sections = []
        for i in range(14):
            self.sections.append(
                Section(self.raw[i * 0x1000:(i + 1) * 0x1000])
            )

    def __str__(self) -> str:
        res = ""

        res += "SECTIONS:\n"
        for section in self.sections:
            res += "\t" + str(section) + '\n'
        return res


f = open(sys.argv[1], "rb")
content = f.read()

sa = None
sb = None

save_a = content[0:0xE000]
save_b = content[0xE000:0x1C000]

if check_empty_save(save_a):
    print("save_a empty")
else:
    sa = Save(save_a)
    print(sa)

if check_empty_save(save_b):
    print("save_b empty")
else:
    sb = Save(save_b)
    print(sb)