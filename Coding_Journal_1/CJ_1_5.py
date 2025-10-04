import numpy as np
from astropy.table import Table
from math import pi

def main():
        x = 0
        xList = []
        sinList = []
        while x < (2*pi):
                xList.append(x)
                sinList.append(np.sin(x))
                x += (2*pi)/1000
        data = Table([xList,sinList] , names = ["x", "sin(x)"])
        print(data)

if __name__ == '__main__':
        main()

