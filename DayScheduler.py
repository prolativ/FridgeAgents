from mesa.time import BaseScheduler

class DayScheduler(BaseScheduler):
    def __init__(self, model):
        super(DayScheduler, self).__init__(model)
        self.days = 0

    
    def step(self):
        self.steps += 1
        self.time += 1

        if not self.model.isSupplyInProgress:
            self.days += 1
            self.model.nextDay()

        for agent in self.agents:
            agent.step(self.model)
    


