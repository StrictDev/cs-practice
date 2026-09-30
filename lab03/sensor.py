threshold = float(input())
n = int(input())

sm, mx, excess, errs = 0, float('-inf'), 0, 0

for _ in range(n):
    tmpr = input()
    if tmpr == 'error':
        errs += 1
    else:
        tmpr = float(tmpr)
        excess += 1 if tmpr > threshold else 0
        sm += tmpr
        mx = max(mx, tmpr)

print(f'Количество записей: {n}\n\
Ошибок: {errs}\n\
Превышений: {excess}\n\
Максимальное: {mx:.1f}\n\
Среднее: {(sm / (n - errs)):.1f}')
