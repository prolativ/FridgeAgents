from mesa import Agent

class SupplierAgent(Agent):
    def __init__(self, budget):
        self.budget = budget

    def step(self, model):
        self.loadTrucks(model)

    def loadTrucks(self, model):
        truck = model.truck
        sortedOrders = sorted(model.orders, key=lambda order: -order.totalVolume())
        totalVolume = 0
        while sortedOrders and totalVolume + sortedOrders[0].totalVolume() <= truck.capacity:
            order = sortedOrders.pop(0)
            fridgeId, demand = order.fridgeId, order.demand
            model.truck.addLoad(fridgeId, demand)
            totalVolume += order.totalVolume()



# TODO: Add budget simulation