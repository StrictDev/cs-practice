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

# - 4
matrix = np.arange(1, 26).reshape(5, 5)
fs = [matrix[:3], matrix[-2:], matrix[:, :2], matrix[1:4, 2:5], matrix[-2:, -2:]]
print(f'1-3-rows: {fs[0]}')
print(f'last2-rows: {fs[1]}')
print(f'1-2-cols: {fs[2]}')
print(f'frag: {fs[3]}')
print(f'1-3-rows: {fs[4]}')

print(f's1: {fs[0].shape}')
print(f's2: {fs[1].shape}')
print(f's3: {fs[2].shape}')
print(f's4: {fs[3].shape}')
print(f's5: {fs[4].shape}')

# - 5
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

# copy - потому что мы будем изменять массив, нужно сохранить данные
changed_hours = hours.copy()

changed_hours[2:5] = 99
changed_hours[::2] = -1

print(f'changed_hours: {changed_hours}')
print(f'hours: {hours}')

changed_matrix = matrix.copy()
changed_matrix[1] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4] = 100

print(f'changed_matrix: {changed_matrix}')
print(f'matrix: {matrix}')

# - 6
numbers = np.arange(0, 12)

# Произведение количества строк и столбцов должно равняться количеству элементов
# 3x4 = 12 - верно
# 5x3 != 12 (15) - неверно
table = numbers.reshape(3, 4)
transposed = table.T

print(f'numbers: {numbers}')
print(f'table: {table}')
print(f'transposed: {transposed}')





