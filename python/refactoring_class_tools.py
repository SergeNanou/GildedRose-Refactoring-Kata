from abc import ABC, abstractmethod


# 1: Define the Strategy Interface (Abstract Class)
class GildedRoseStrategy(ABC):

    MIN_QUALITY = 0
    MAX_QUALITY = 50

    @abstractmethod
    def update_quality(self):
        pass


# 2 - Implement Concrete Strategies


class StandardItem(GildedRoseStrategy):
    def update_quality(self, item):
        if item.sell_in > 0:
            modification = -1
        else:
            modification = -2
        item.quality = max((item.quality + modification), self.MIN_QUALITY)
        item.sell_in += -1


class AgedBrie(GildedRoseStrategy):
    def update_quality(self, item):
        if item.sell_in > 0:
            modification = 1
        else:
            modification = 2
        item.quality = min((item.quality + modification), self.MAX_QUALITY)
        item.sell_in += -1


class AgedBrie(GildedRoseStrategy):
    def update_quality(self, item):
        if item.sell_in > 0:
            modification = 1
        else:
            modification = 2
        item.quality = min((item.quality + modification), self.MAX_QUALITY)
        item.sell_in += -1


class Sulfuras(GildedRoseStrategy):
    def update_quality(self, item):
        pass


class BackstagePasses(GildedRoseStrategy):
    def update_quality(self, item):

        if item.sell_in > 10:
            modification = 1
        elif item.sell_in > 5:
            modification = 2
        elif item.sell_in > 0:
            modification = 3
        else:
            item.quality = 0
            modification = 0
        item.quality = min((item.quality + modification), self.MAX_QUALITY)
        item.sell_in += -1


class Conjured(GildedRoseStrategy):
    def update_quality(self, item):
        if item.sell_in > 0:
            modification = -2
        else:
            modification = -4

        item.quality = max((item.quality + modification), self.MIN_QUALITY)
        item.sell_in += -1


# 3- Create the Context Class
class GildedRoseContext:
    def __init__(self, update_quality_strategy):
        self.update_quality_strategy = update_quality_strategy

    def set_update_quality_strategy(self, update_quality_strategy):
        self.update_quality_strategy = update_quality_strategy

    def make_update_quality_strategy(self, item):
        self.update_quality_strategy.update_quality(item)
