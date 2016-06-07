from mesa import Agent
from Order import Order

class FridgeAgent(Agent):
    def __init__(self, fridgeId, capacity, dailyUsages, initialContents):
        self.fridgeId = fridgeId
        self.capacity = capacity
        self.dailyUsages = dailyUsages
        self.contents = initialContents

    def consume(self):
        for product, amount in self.dailyUsages.items():
            self.contents[product] -= amount

    def acceptDelivery(self, delivery):
        for product, amount in delivery.items():
            self.contents[product] += amount

    def makeOrder(self, model):
        #use contents and dailyUsages to compute, don't exceed capacity
        #fake implementation
        order = Order(self.fridgeId, demand=self.dailyUsages)
        model.orders.append(order)

    def step(self, model):
        self.consume()
        self.makeOrder(model)