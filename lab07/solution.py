import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if len(values) % width != 0:
        return []
    arr = np.asarray(values)
    return arr.reshape(len(arr) // width, width).tolist()

    
