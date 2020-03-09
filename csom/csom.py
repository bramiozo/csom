'''
features:
* progress monitor
* loss function
* similarity / distance function
* weight vector
* growing map size
* reducing dissimilarity

follow this blog for the intial code: https://medium.com/@navdeepsingh_2336/self-organizing-maps-for-machine-learning-algorithms-ad256a395fc5
'''

import numpy as np
# W(n+1) = W(n) + theta(u,v,n) * alpha(n) * (D(t) - Wv(n))


def progress(x):
    return True

def loss_function(x):
    return loss

def loss_gradient(x):
    return grad

def similarity(x):
    return True

def dissimilarity(x):
    return True

class csom:
    def __init__(self, num_iter=100, grid_size=(8, 8), grid_shape="rect"):
        self.num_iter = num_iter
        self.grid_size = grid_size
        self.grid_shape = grid_shape
        self.W = self._initiate()


    def _initiate(self):
        self.W = np.random.normal(0, 0.1, size=(self.grid_size, ))
        return True


    def _grow(self):
        return True



