from mesa import Agent
from FridgeAgent import FridgeAgent
import random
from collections import defaultdict

class TruckAgent(Agent):
    def __init__(self, truckId, capacity):
        self.truckId = truckId
        self.capacity = capacity
        self.load = {}

    def move(self, model):
        #mock - replace with algorithm finding path to nearest target fridge
        possible_steps = model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = random.choice(possible_steps)
        model.grid.move_agent(self, new_position)

    def deliver(self, model):
        cellmates = model.grid.get_cell_list_contents([self.pos])
        fridges = list(filter(lambda x: isinstance(x, FridgeAgent), cellmates))
        if fridges:
            fridge = fridges[0]
            if fridge.fridgeId in self.load:
                orderedProducts = self.load.pop(fridge.fridgeId)
                fridge.acceptDelivery(orderedProducts)

    def loadProductAmounts(self):
        totalAmounts = defaultdict(int)
        for productAmounts in self.load.values():
            for product, amount in productAmounts.items():
                totalAmounts[product] += amount
        return totalAmounts

            
    def addLoad(self, fridgeId, demand):
        self.load[fridgeId] = demand

    def step(self, model):
        self.move(model)
        self.deliver(model)