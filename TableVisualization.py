from mesa.visualization.ModularVisualization import VisualizationElement

class TableVisualization(VisualizationElement):
    local_includes = ["VerticalHeaderTableModule.js"]
    js_code = "elements.push(new VerticalHeaderTableModule());"

    def __init__(self, getHeader, getValues, getColors):
    	self.getHeader = getHeader
    	self.getValues = getValues
    	self.getColors = getColors

    def render(self, model):
    	return {"header": self.getHeader(model), "values": self.getValues(model), "colors": self.getColors(model)}