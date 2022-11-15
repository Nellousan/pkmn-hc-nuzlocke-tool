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
        for i in range(14):
            self.sections.append(
                section.SectionFactory.from_raw_section(self.raw[i * 0x1000:(i + 1) * 0x1000])
            )

    def __str__(self) -> str:
        res = ""

        res += "SECTIONS:\n"
        for section in self.sections:
            res += "\t" + str(section) + '\n'
        return res
