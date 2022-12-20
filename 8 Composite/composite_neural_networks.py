from abc import ABC
from collections.abc import Iterable


class NeuronConnector(Iterable, ABC):
    def connect_to(self, other):
        # Connect connect ourselves to ourselves
        if self == other:
            return

        for neuron in self:
            for other_neuron in other:
                neuron.outputs.append(other_neuron)
                other_neuron.inputs.append(neuron)


class Neuron(NeuronConnector):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f'<Neuron: {self.name}, ' \
            f'{len(self.inputs)} inputs, ' \
            f'{len(self.outputs)} outputs>'

    def __iter__(self):
        yield self

    # def connect_to(self, other):
    #     # Bidirectional connection
    #     self.outputs.append(other)
    #     other.inputs.append(self)


class NeuronLayer(list, NeuronConnector):
    def __init__(self, name, neurons_count):
        super().__init__()
        self.name = name
        for i in range(neurons_count):
            self.append(Neuron(f'{name}-{i}'))

    def __str__(self):
        return f'<NeuronLayer: {self.name} with {len(self)} neurons>'


if __name__ == '__main__':
    n1 = Neuron('n1')
    n2 = Neuron('n2')

    l1 = NeuronLayer('L1', 3)
    l2 = NeuronLayer('L2', 4)

    n1.connect_to(n2)
    n1.connect_to(l1)

    l1.connect_to(n2)
    l1.connect_to(l2)

    print(n1)
    print(n2)
    print(l1)
    print(l2)
