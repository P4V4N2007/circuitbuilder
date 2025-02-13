from components import Component
class VoltageSource(Component):
    def __init__(self, name, voltage):
        # Initialize attributes specific to VoltageSource
        self.name = name
        self.voltage = voltage
        super().__init__(name)  # Call the parent class constructor

    def get_voltage(self):
        return self.voltage 

    def add_component(self):
        # Append the name of the component to the nodes list
        self.nodes.append(self.name)
        return self.nodes
        




