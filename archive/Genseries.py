import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Genseries:

    def linear(self, first_point=0, last_point=1000):
        self.data = np.linspace(first_point, last_point, self.points)
        return self

    def nonlinear(self, first_point=-3, last_point=3, n=5):
        x = self.linear(first_point, last_point).data
        apex = (last_point + first_point) / 2
        y = list()
        for i in x:
            y.append([(i - apex)**n - 10])
        self.data = y
        return self

    def quadratic(self, first_point=-10, last_point=10):
        self.data = self.nonlinear(first_point, last_point, 2).data
        return self

    def cubic(self, first_point=-10, last_point=10):
        self.data = self.nonlinear(first_point, last_point, 3).data
        return self

    def __init__(self, points=1000):
        self.points = points
        self.data = []
        self.data_frame = pd.DataFrame([])
