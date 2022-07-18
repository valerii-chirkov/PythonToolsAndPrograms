class Layer:
    def __init__(self) -> None:
        self.name = 'Layer'
        self.next_layer = None

    def __call__(self, next_layer):
        self.next_layer = next_layer
        return next_layer


class Input(Layer):
    def __init__(self, inputs) -> None:
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs
    
    def __call__(self, next_layer):
        return super().__call__(next_layer)
        

class Dense(Layer):
    def __init__(self, *args) -> None:
        super().__init__()
        self.name = 'Dense'
        self.inputs, self.outputs, self.activation = args
        

class NetworkIterator:
    def __init__(self, network) -> None:
        self.network = network

    def __iter__(self):
        obj = self.network
        while obj:
            yield obj
            obj = obj.next_layer

            
network = Input(128)
layer1 = network(Dense(network.inputs, 1024, 'linear'))
layer2 = layer1(Dense(layer1.inputs, 10, 'softmax'))


for x in NetworkIterator(network):
    print(x.name)
