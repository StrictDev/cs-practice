names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]


def winner(names: list[str], scores: list[float]) -> str:
    return names[scores.index(max(scores))]

def average(scores: list[float]) -> float:
    return sum(scores) / max(len(scores), 1)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    results = [(names[i], scores[i]) for i in range(len(names))]
    return [el[0] for el in sorted(results, key=lambda x: -x[1])]
