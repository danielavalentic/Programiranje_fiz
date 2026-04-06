import numpy as np
import matplotlib.pyplot as plt
import Vjezbe_2.calculus as calc


calc.derivPoint([1, 0, 0, 0], 10)
calc.derivInterval([1, 0, 0, 0], 10, 20, 0.01)

calc.derivPoint(np.sin, 10)
calc.derivInterval(np.sin, 10, 20, 0.01)


calc.integRect([1, 0, 0, 0], 10, 20, 10000)
calc.integTrap([1, 0, 0, 0], 10, 20, 10000)

calc.integRect(np.sin, 10, 20, 10000)
calc.integTrap(np.sin, 10, 20, 10000)