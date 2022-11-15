import struct


class Section:
    def __init__(self, section):
        t = struct.unpack("<hHll", section[0xFF4:0x1000])
        self.id = t[0]
        self.checksum = t[1]
        self.sig = t[2]
        self.save_idx = t[3]
        self.raw = section

    def __str__(self) -> str:
        return "Section: id: {:02d}, checksum: {:05d} {:04X}, sig: {:04X}, save idx: {:01X}".format(
            self.id, self.checksum, self.checksum, self.sig, self.save_idx
        )


class SectionTrainer(Section):
    def __init__(self, section):
        Section.__init__(self, section)
        t = struct.unpack("<8sbbI", section[0x0:0xE])
        self.player_name = t[0]
        self.gender = t[1]
        self.trainer_id = t[3]

    def __str__(self) -> str:
        res = ""
        res += Section.__str__(self)
        res += "\n\t\tName: {}, gender: {:01X}, trainer_id: {:08X}".format(
            self.player_name, self.gender, self.trainer_id
        )
        return res


class SectionFactory:
    def from_raw_section(section) -> Section:
        t = struct.unpack("<hHll", section[0xFF4:0x1000])
        id = t[0]
        match id:
            case 0:
                return SectionTrainer(section)
            case _:
                return Section(section)
