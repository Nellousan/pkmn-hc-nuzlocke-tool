import struct
import items


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


class SectionTeamsItems(Section):
    def __init__(self, section):
        Section.__init__(self, section)
        self.team_size = struct.unpack("<L", section[0x234:0x238])[0]
        t = struct.unpack("<LH", section[0x490:0x496])
        self.money = t[0]
        self.coins = t[1]

        # Fetching pc items, there are 50 slots
        self.pc_items = []
        for i in range(50):
            self.pc_items.append(items.ItemSlot(section[(i * 4) + 0x498:(i * 4) + 0x49C]))

        # Fetching item pocket, there are 30 slots in emerald
        self.pocket_items = []
        for i in range(30):
            self.pocket_items.append(items.ItemSlot(section[(i * 4) + 0x560:(i * 4) + 0x564]))

        # Key items, 30 slots
        self.key_items = []
        for i in range(30):
            self.key_items.append(items.ItemSlot(section[(i * 4) + 0x5D8:(i * 4) + 0x5DC]))

    def __str__(self) -> str:
        res = ""
        res += Section.__str__(self)
        res += "\n\t\tteam size: {} money: {}, coins: {}\n".format(self.team_size, self.money, self.coins)
        res += "\t\tPC Items:\n"
        for item in self.pc_items:
            if item.id == 0x0:
                continue
            res += "\t\t\t" + str(item) + "\n"
        return res


class SectionFactory:
    def from_raw_section(section) -> Section:
        t = struct.unpack("<hHll", section[0xFF4:0x1000])
        id = t[0]
        match id:
            case 0:
                return SectionTrainer(section)
            case 1:
                return SectionTeamsItems(section)
            case _:
                return Section(section)
