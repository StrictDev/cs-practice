def read_rows(lines: list[str]) -> list[dict]:
    if len(lines) < 1:
        return []
    
    headers = [header for header in lines[0].rstrip().split(',') if header]
    rows = []

    for line in lines[1:]:
        row = [el for el in line.rstrip().split(',') if el]

        if len(row) == len(headers):
            rows += [{headers[i]: row[i] for i in range(len(row))}]

    return rows


def count_types(rows: list[dict]) -> dict:
    cnt = dict()
    for el in rows:
        cnt[el['тип']] = cnt.get(el['тип'], 0) + 1

    return cnt
        

def total_minutes(rows: list[dict], kind: str) -> float:
    minutes = 0.0
    for el in rows:
        if el['тип'] == kind:
            try:
                minutes += float(el['минуты'].replace(',', '.'))
            except ValueError:
                continue

    return round(minutes, 1)


def to_csv(counts: dict) -> str:
    ss = 'тип,количество\n'

    for key, value in sorted(counts.items()):
        ss += f'{key},{value}\n'

    return ss
        
    
    
