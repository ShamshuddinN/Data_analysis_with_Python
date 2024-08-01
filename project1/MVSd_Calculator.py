import numpy as np

def calculate(listProvided) :
    if len(listProvided) < 9:
        raise ValueError("List must contain nine numbers.")
    
    calculations = {}
    arr = np.array(listProvided).reshape(3, 3)

    calculations['mean'] = [list(arr.mean(axis = 0)), list(arr.mean(axis = 1)), arr.reshape(9,).mean()]
    calculations['variance'] = [  list(arr.var(axis = 0)),  list(arr.var(axis = 1)), arr.reshape(9, ).var() ]
    calculations['standard deviation'] = [ list(arr.std(axis = 0)), list(arr.std(axis = 1)), arr.reshape(9, ).std()]
    calculations['max'] = [ list(arr.max(axis = 0)), list(arr.max(axis = 1)), arr.reshape(9, ).max() ]
    calculations['min'] = [ list(arr.min(axis = 0)), list(arr.min(axis = 1)), arr.reshape(9, ).min() ]
    calculations['sum'] = [ list(arr.sum(axis = 0)), list(arr.sum(axis = 1)), arr.reshape(9, ).sum() ]

    return calculations