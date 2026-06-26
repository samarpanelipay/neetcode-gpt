import numpy as np
from numpy.typing import NDArray
import math

class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        your_answer=  1 / (1 + math.e**(-z))
        return np.round(your_answer, 5)
        

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        for i in range(len(z)):
            z[i]=max(0, z[i])
        return z
