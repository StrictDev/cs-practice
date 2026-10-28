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
    return np.round(np.mean(arr, axis=0), decimals=6).tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0
    col = np.asarray(matrix, dtype=float)[:, column]
    return float(np.round(max(col) - min(col), decimals=6))
