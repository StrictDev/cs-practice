import numpy as np

def make_hours() -> list[int]:
    return np.arange(0, 22, 3).tolist()

def vector_report(values: list[float]) -> dict:
    return {
        "third": values[2],
        "last": values[-1],
        "middle": values[2:6],
        "every_second": values[::2],
        "reversed": values[::-1]
    }

def change_vector(values: list[float]) -> list[float]:
    newvals = np.asarray(values.copy(), dtype=float)

    newvals[2:5] = 99
    newvals[::2] = -1

    return newvals.tolist()

def cap_above(values: list[float], limit: float) -> list[float]:
    newvals = np.asarray(values.copy(), dtype=float)
    newvals[newvals > limit] = limit
    return newvals.tolist()

def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    newvals = np.asarray(values.copy(), dtype=float)
    return  (newvals * 9 / 5 + 32).tolist()

