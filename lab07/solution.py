import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype=float)
    return arr.reshape(len(arr) // width, width).tolist()

    
def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix, dtype=float)
    return arr[np.ix_(rows, columns)].tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    return np.mean(arr, axis=0).tolist()
