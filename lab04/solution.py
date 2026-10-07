def winner(names: list[str], scores: list[float]) -> str:
    return names[scores.index(max(scores))]

def average(scores: list[float]) -> float:
    return round(sum(scores) / max(len(scores), 1), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    results = [(names[i], scores[i]) for i in range(len(names))]
    return [el[0] for el in sorted(results, key=lambda x: -x[1])]

def above_average(names: list[str], scores: list[float]) -> list[str]:
    results = [(names[i], scores[i]) for i in range(len(names))]
    avg = average(scores)
    return [el[0] for el in results if el[1] > avg]

if __name__ == '__main__':
    print(winner(["Аня", "Боря", "Вика"], [7.0, 9.0, 8.0]))
    print(average([7.0, 9.0, 9.0]))
                        
    
