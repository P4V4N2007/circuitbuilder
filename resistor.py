from components import Component
class Resistor(Component):
    def __init__(self, name):
        self.name=name
        self.resistance=0 
    def set_resistance(self,new_resistance):
        
        if new_resistance<0:
            raise ValueError("cannot use this value")
        self.resistance=new_resistance
    def get_resistance(self,resistance):
        return self.resistance
    

