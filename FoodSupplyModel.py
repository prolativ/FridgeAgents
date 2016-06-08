from mesa import Agent, Model
from mesa.space import MultiGrid

from FridgeAgent import FridgeAgent
from TruckAgent import TruckAgent
from SupplierAgent import SupplierAgent
from DayScheduler import DayScheduler

import random

class FoodSupplyModel(Model):
    def __init__(self, fridgesCount, width, height):
        self.fridgesCount = fridgesCount
        self.running = True
        self.grid = MultiGrid(height, width, torus=False)
        self.schedule = DayScheduler(self)
        self.productTypes = ["A", "B", "C"]
        self.fridges = []
        self.isSupplyInProgress = False
        self.orders = []

        def randomFreeCoordinates():
            while True:
                x = random.randrange(self.grid.width)
                y = random.randrange(self.grid.height)
                if self.grid.is_cell_empty((x, y)):
                    return (x, y)

        def balancedInitialContents(capacity):
            amount = capacity / len(self.productTypes)
            return {product: amount for product in self.productTypes}

        for i in range(self.fridgesCount):
            capacity = 30
            dailyUsages = {"A": 3, "B": 2, "C": 1}
            fridge = FridgeAgent(i, capacity, dailyUsages, balancedInitialContents(capacity))
            self.fridges.append(fridge)
            self.grid.place_agent(fridge, randomFreeCoordinates())

        self.supplier = SupplierAgent(1000)

        self.truck = TruckAgent(0, capacity=100)
        self.schedule.add(self.truck)
        # self.grid.place_agent(self.truck, randomFreeCoordinates())
        self.grid.place_agent(self.truck, (0,0))


    def nextDay(self):
        for fridge in self.fridges:
            fridge.step(self)
        self.supplier.step(self)
        self.orders = []
        self.isSupplyInProgress = True


    def step(self):
        self.schedule.step()
    
    def run_model(self, n):
        for i in range(n):
            self.step()

