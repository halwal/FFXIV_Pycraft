class Item:
    """Class for keeping info about item parameters"""
    def __init__(self, name, doh_class, lvl, rlvl, durability, progress, quality):
        self.doh_class = doh_class
        self.lvl = lvl
        self.name = name
        self.rlvl = rlvl
        self.durability = durability
        self.progress = progress
        self.quality = quality
