from mesa import Agent
from FridgeAgent import FridgeAgent
import random
import sys
from collections import defaultdict

class TruckAgent(Agent):
    def __init__(self, truckId, capacity):
        self.truckId = truckId
        self.capacity = capacity
        self.load = {}

    def get_distance(self, pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

    def find_closest_fridge(self, fridges):
        closest = None
        min_dist = sys.maxsize
        for f in fridges:
            if f.fridgeId in self.load:
                dist = self.get_distance(self.pos,f.pos)
                if dist<min_dist:
                    min_dist = dist
                    closest = f
        return closest

    def move(self, model):
        #mock - replace with algorithm finding path to nearest target fridge
        # possible_steps = model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        # new_position = random.choice(possible_steps)
        closest = self.find_closest_fridge(model.fridges)
        cx = -1
        cy = -1
        if closest is None:
            cx = 0
            cy = 0
        else:
            cx = closest.pos[0]
            cy = closest.pos[1]
        x = 0
        y = 0
        if (self.pos[0]-cx)<0:
            x = 1
        elif (self.pos[0]-cx)>0:
            x = -1
        if (self.pos[1]-cy)<0:
            y = 1
        elif (self.pos[1]-cy)>0:
            y = -1  
        new_position = (self.pos[0]+x,self.pos[1]+y)      
        model.grid.move_agent(self, new_position)
        if closest is None and self.pos[0]==0 and self.pos[1]==0:
            model.isSupplyInProgress = False

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