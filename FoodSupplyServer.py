from FoodSupplyModel import FridgeAgent, TruckAgent, FoodSupplyModel
from TableVisualization import TableVisualization
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.ModularVisualization import ModularServer, VisualizationElement


colors = ["Red", "Green", "Yellow", "Blue", "Orange", "Violet", "Pink", "DarkRed", "Khaki", "LightSeaGreen"]


def fridgePortrayal(fridge):
    portrayal = {
        "Shape": "rect",
        "Filled": True,
        "w": 0.8,
        "h": 0.8,
        "Color": colors[fridge.fridgeId],
        "Layer": 1
    }
    return portrayal


def truckPortrayal(truck):
    portrayal = {
        "Shape": "circle",
        "Filled": True,
        "r": 0.7,
        "Color": "Black",
        "Layer": 2
    }
    return portrayal

def agentPortrayal(agent):
    if isinstance(agent, FridgeAgent):
        return fridgePortrayal(agent)
    if isinstance(agent, TruckAgent):
        return truckPortrayal(agent)


def getFridgeTableHeader(model):
    return model.productTypes

def getFridgeTableValues(model):
    return list(map(lambda fridge: fridge.contents, model.fridges)) + [model.truck.loadProductAmounts()]

def getFridgeTableFormatings(model):
    return [{"color": color} for color in colors] + [{"color": "Black", "bold": True}]

class DaysCounter(TextElement):
    def render(self, model):
        return "Days: %d" % model.schedule.days 


grid = CanvasGrid(agentPortrayal, 20, 20, 500, 500)
fridgesStates = TableVisualization(getFridgeTableHeader, getFridgeTableValues, getFridgeTableFormatings)
daysCounter = DaysCounter()


server = ModularServer(FoodSupplyModel, [grid, fridgesStates, daysCounter], "Food supply model", 10, 20, 20)
server.port = 8889
server.launch()