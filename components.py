class Component:
    def __init__(self, name, **kwargs):
        self.name = name
        self.nodes = []
        self.connections = []
        self.properties = kwargs

    def connect_to(self, other_component, node1, node2):
        """
        Connect this component to another component via specified nodes.
        """
        self.nodes.extend([node1, node2])
        self.connections.append((other_component, node1, node2))

        # Ensure the other component also registers this connection
        other_component.nodes.extend([node1, node2])
        other_component.connections.append((self, node1, node2))





# Example Usage
##circuit = Circuit()

# Create components
#r1 = Resistor("R1", 100)
#r2 = Resistor("R2", 50)
#v1 = VoltageSource("V1", 12)

# Connect components
#r1.connect_to(v1, 'node1', 'node2')
#r1.connect_to(r2, 'node2', 'node3')

# Add components to the circuit
#circuit.add_component(r1)
#circuit.add_component(r2)
#circuit.add_component(v1)

# Debugging Outputs
#print("Circuit Components:")
#for comp in circuit.components:
 #   print(f"Name: {comp.name}, Properties: {comp.properties}, Connections: {comp.connections}")

#print("\nCircuit Nodes:")
#print(circuit.nodes)#
