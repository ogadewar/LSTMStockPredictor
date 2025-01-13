import math
import pandas as pd
import numpy as np
class LSTMCell:
    def __init__(self, isize, hsize):
        self.isize = isize
        self.hsize = hsize

        self.Wf = np.random.randn(hsize, isize + hsize) / np.sqrt(isize + hsize)
        self.Wi = np.random.randn(hsize, isize + hsize) / np.sqrt(isize + hsize)
        self.Wo = np.random.randn(hsize, isize + hsize) / np.sqrt(isize + hsize)
        self.Wc = np.random.randn(hsize, isize + hsize) / np.sqrt(isize + hsize)

        self.Bf = np.zeros((hsize,1))
        self.Bi = np.zeros((hsize,1))
        self.Bo = np.zeros((hsize,1))
        self.Bc = np.zeros((hsize,1))

    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def tanh(self, x):
        return np.tanh(x)
    
    def forward(self, x, h_prev, c_prev):
        vstack = np.vstack(h_prev, x)

        forget_gate = self.sigmoid(self.Wf@vstack + self.Bf)

        input_gate = self.sigmoid(self.Wi@vstack + self.Bi)
        c = self.tanh(self.Wc@vstack + self.Bc)

        c_next = c_prev + i*c
        
        output_gate = self.sigmoid(self.Wo@vstack +self.Bo)
        h_next = output_gate * self.tanh(c_next)

        return h_next, c_next, cache(forget_gate, input_gate,c, c_next, output_gate, vstack)
    
    

