import section


def check_empty_save(save: list) -> bool:
    for byte in save:
        if byte != 0xFF:
            return False
    return True


class Save:
    def __init__(self, save: list):
        self.raw = save
        self.sections = []
        key = 0
        for i in range(14):
            s = section.SectionFactory.from_raw_section(self.raw[i * 0x1000:(i + 1) * 0x1000])
            self.sections.append(s)
            if s.id == 0:
                key = s.security_key

        for s in self.sections:
            s.decrypt(key)

    def __str__(self) -> str:
        res = ""

        res += "SECTIONS:\n"
        for s in self.sections:
            res += "\t" + str(s) + '\n'
        return res
