import sys
import time
import json

import theano
import theano.tensor as T
import numpy as np

if __name__=='__main__':
    data_location = sys.argv[1]
    print 'thinking'




class Layer(object):
    '''
    The base layer object.  an artificial neural network is composed
    of many of these objects connected.
    '''

    def __init__(self, input, n_in, n_out, activation, rng):
        W = np.asarray(
            rng.uniform(
                low=-np.sqrt(6. / (n_in + n_out)),
                high=-np.sqrt(6. / (n_in + n_out)),
                size=(n_in, n_out)
            ),
            dtype=theano.config.floatX
        )
        b = np.zeros(
            (n_out,), dtype=theano.config.floatX
        )
        self.input = input
        self.W = theano.shared(value=W, name='W', borrow=True)
        self.b = theano.shared(value=b, name='b', borrow=True)
        self.params = [self.W, self.b]

        linear_output = T.dot(input, self.W) + b

        if activation is None:
            self.output = linear_output
        else:
            self.output = activation(linear_output)

class ANN(object):

    def __init__(self, n_in, n_out, layer_sizes):
        '''
        takes a list of layer sizes and activation functions
        and builds an ANN from layer objects.
        '''
        self.rng = np.random.RandomState(12354)
        self.input = self.x
        self.x = T.dvector('x')
        self.y = T.dscalar('y')
        self.layers = []
        self.params = []

        for i in xrange(len(hidden_sizes)):

            if i == 0:
                layer_input = self.input
                n_in = input_size
                n_out = hidden_sizes[i]
            else:
                layer_input = self.layers[-1].output
                n_in = hidden_sizes[i - 1]
                n_out = hidden_sizes[i]

            layer = Layer(input=layer_input,
                         n_in=n_in,
                         n_out=n_out,
                         activation=T.tanh)
            self.layers.append(layer)
            self.params.extend(layer.params)


        self.output_layer = Layer(
            input=self.layers[-1].output,
            num_in=hidden_sizes[-1],
            num_out=output_size,
            activation=None
        )
        self.layers.append(self.output_layer)
        self.params.extend(self.output_layer.params)
        self.cost = T.mean((self.output_layer.output - self.y) ** 2)

    def training(self, dataset, learning_rate=0.01):
        set_x, set_y = dataset
        index = T.iscalar("index")
        gparams = T.grad(self.cost, self.params)
        updates = [
            (param, param - gparam * learning_rate)
            for param, gparam in zip(self.params, gparams)
        ]

        train = theano.function(
            inputs=[index],
            outputs=self.cost,
            updates=updates,
            givens={
                self.x: set_x[index],
                self.y: set_y[index]
            },
            name='train'
        )
        return train

    def predict(self, x):

        index = T.iscalar("index")
        predict = theano.function(
            inputs=[index],
            outputs=self.output_layer.output,
            givens={
                self.x: x[index]
            },
            name='predict'
        )
        return predict

class StatisticalAgent(object):
    '''
    This is the primary agent that directs construction and adjustment of
    theano ANNs
    '''
    def __init__(self, parameters):
        pass
