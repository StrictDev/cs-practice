names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]


def winner(names: list[str], scores: list[float]) -> str:
    return names[scores.index(max(scores))]
