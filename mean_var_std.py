import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    tasks = [
        ['mean', np.mean],
        ['variance', np.var],
        ['standard deviation', np.std],
        ['max', np.max],
        ['min', np.min],
        ['sum', np.sum],
    ]
    nd = np.reshape(list, (3, 3))
    calculations = {}

    for task in tasks:
      calculations[task[0]] = [task[1](nd, axis=i).tolist() for i in (0, 1, (0, 1))]
    return calculations