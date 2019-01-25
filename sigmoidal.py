import numpy as np
import matplotlib.pyplot as plt

def plot_sigm(a):
    x = [i for i in np.arange(a-5,a+5,0.1)]
    y = []

    for i in x:
        y.append(float((1 / (1 + np.exp(-float(a)*(float(i)-float(a)))))))

    plt.plot(x,y)
    plt.show()

def sigm(x,a):
    return float((1 / (1 + np.exp(-a*(x-a)))))


