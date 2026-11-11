import numpy as np

# - 1

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.identity(3)

print(f'hours: {hours}')
print(f'shape: {hours.shape}')
print(f'ndim: {hours.ndim}')
print(f'size: {hours.size}')
print(f'dtype: {hours.dtype}')

# - 2

print(f'3-elem: {hours[3]}')
print(f'last-elem: {hours[-1]}')
print(f'2-5-elem: {hours[2:6]}')
print(f'every2: {hours[::2]}')
print(f'reverse: {hours[::-1]}')

# - 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(f'shape: {temperatures.shape}')
print(f'ndim: {temperatures.ndim}')
print(f'size: {temperatures.size}')
print(f'2,3: {temperatures[1, 2]}')
print(f'1st-row: {temperatures[0]}')
print(f'-1st-row: {temperatures[-1]}')
print(f'1without1: {temperatures[:2, 1:]}')
print(f'center2x2: {temperatures[:2, 1:3]}')

