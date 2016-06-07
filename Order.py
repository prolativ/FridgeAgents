class Order(object):
    def __init__(self, fridgeId, demand):
        self.fridgeId = fridgeId
        self.demand = demand

    def totalVolume(self):
        return sum(self.demand.values())