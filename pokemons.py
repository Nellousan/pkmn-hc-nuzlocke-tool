import struct


class Pokemon:
    class Subdata:
        ORDERS = [
            "GAEM", "GAME", "GEAM", "GEMA", "GMAE", "GMEA",
            "AGEM", "AGME", "AEGM", "AEMG", "AMGE", "AMEG",
            "EGAM", "EGMA", "EAGM", "EAMG", "EMGA", "EMAG",
            "MGAE", "MGEA", "MAGE", "MAEG", "MEGA", "MEAG"
        ]

        class Growth:
            def __init__(self, section):
                self.raw = section
                self.specie = None
                self.held_item = None
                self.experience = None
                self.pp_bonuses = None
                self.friendship = None
                self.unknown = None

            def __str__(self) -> str:
                pass

            def decrypt(self, key) -> None:
                bkey = key.to_bytes(4, 'little')
                decrypted = []
                for i in range(3):
                    decrypted += [a ^ b for a, b in zip(self.raw[(i * 4):(i * 4) + 4], bkey)]
                t = struct.unpack("<HHLLBBH", decrypted)
                self.specie = t[0]
                self.held_item = t[1]
                self.experience = t[2]
                self.pp_bonuses = t[3]
                self.friendship = t[4]
                self.unknown = t[5]

        class Attacks:
            def __init__(self, section):
                self.raw = section
                self.move_1 = None
                self.move_2 = None
                self.move_3 = None
                self.move_4 = None
                self.pp_1 = None
                self.pp_2 = None
                self.pp_3 = None
                self.pp_4 = None

            def __str__(self) -> str:
                pass

        class EVsCondition:
            def __init__(self, section):
                self.raw = section
                self.ev_hp = None
                self.ev_atk = None
                self.ev_def = None
                self.ev_spd = None
                self.ev_sp_atk = None
                self.ev_sp_def = None
                self.coolness = None
                self.beauty = None
                self.cuteness = None
                self.smartness = None
                self.toughness = None
                self.feel = None

            def __str__(self) -> str:
                pass

        class Miscellaneous:
            def __init__(self, section):
                self.raw = section
                self.pokerus = None
                self.location = None
                self.origin = None
                self.ivs = None      # This contains IVs, egg, and Ability
                self.ribbons = None  # This contains ribbons and obedience

            def __str__(self) -> str:
                pass

        def __init__(self, section, p_value):
            order = self.ORDERS[p_value % 24]
            self.growth = None
            self.attacks = None
            self.evs_condition = None
            self.miscellaneous = None
            for i in range(4):
                match order[i]:
                    case "G":
                        self.growth = self.Growth(section[(i * 12):(i * 12) + 12])
                    case "A":
                        self.attacks = self.Attacks(section[(i * 12):(i * 12) + 12])
                    case "E":
                        self.evs_condition = self.EVsCondition(section[(i * 12):(i * 12) + 12])
                    case "M":
                        self.miscellaneous = self.Miscellaneous(section[(i * 12):(i * 12) + 12])

        def __str__(self) -> str:
            res = ""
            res += "-- GROWTH --\n"
            res += str(self.growth)
            res += "-- ATTACKS --\n"
            res += str(self.attacks)
            res += "-- EVS & CONDITION --\n"
            res += str(self.evs_condition)
            res += "-- MISCELLANEOUS --\n"
            res += str(self.miscellaneous)

    def __init__(self, section):
        t = struct.unpack("<LL10sBB7sBHH48sLBBHHHHHHH", section)
        self.p_value = t[0]
        self.ot_id = t[1]
        self.nickname = t[2]
        self.language = t[3]
        self.egg_name = t[4]
        self.ot_name = t[5]
        self.marking = t[6]
        self.checksum = t[7]
        self.unknown = t[8]
        self.subdata_raw = t[9]
        self.status = t[10]
        self.level = t[11]
        self.rmn_pkrus = t[12]
        self.hp = t[13]
        self.max_hp = t[14]
        self.attack = t[15]
        self.defense = t[16]
        self.speed = t[17]
        self.sp_attak = t[18]
        self.sp_defense = t[19]

    def __str__(self) -> str:
        res = str(self.nickname) + "\n"
        res += "\t\t\tLevel: {}\n".format(self.level)
        return res

    def decrypt(self, trainer_id):
        key = self.p_value ^ trainer_id

        bkey = key.to_bytes(4, byteorder="little")
        self.subdata_dec = []
        for i in range(len(self.subdata_raw)):
            self.subdata_dec.append(bkey[i % 4] ^ self.subdata_raw[i])
