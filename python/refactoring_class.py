from refactoring_class_tools import *


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                aged_brie = AgedBrie()
                gilded_rose = GildedRoseContext(aged_brie)
                gilded_rose.make_update_quality_strategy(item)

            elif item.name == "Sulfuras, Hand of Ragnaros":
                sulfuras = Sulfuras()
                gilded_rose = GildedRoseContext(sulfuras)
                gilded_rose.make_update_quality_strategy(item)

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                backstage = BackstagePasses()
                gilded_rose = GildedRoseContext(backstage)
                gilded_rose.make_update_quality_strategy(item)

            elif item.name == "Conjured Mana Cake":
                conjured = Conjured()
                gilded_rose = GildedRoseContext(conjured)
                gilded_rose.make_update_quality_strategy(item)
            else:
                standard_item = StandardItem()
                gilded_rose = GildedRoseContext(standard_item)
                gilded_rose.make_update_quality_strategy(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
