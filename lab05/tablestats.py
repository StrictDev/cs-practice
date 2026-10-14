def read_rows(lines: list[str]) -> list[dict]:
    headers = [header for header in lines.readline().rstrip().split(',') if header]
    rows = []

    for line in lines:
        row = line.rstrip().split(',')

        if len(row) != len(headers):
            continue

        for i in range(len(row)):
            if row[i]:
                rows += [{headers[i]: row[i]}] 

    return rows


def count_types(rows: list[dict]) -> dict:
    cnt = dict()
    for i in range(0, len(rows), 3):
        data, event_type, time = rows[i]['дата'], rows[i + 1]['тип'], rows[i + 2]['минуты']
        cnt[event_type] = cnt.get(event_type, 0) + 1

    return cnt
        

def total_minutes(rows: list[dict], kind: str) -> float:
    minutes = 0.0
    for i in range(0, len(rows), 3):
        data, event_type, time = rows[i]['дата'], rows[i + 1]['тип'], rows[i + 2]['минуты']
        
        if event_type == kind:
            try:
                minutes += float(time)
            except ValueError:
                continue

    return round(minutes, 1)


def to_csv(counts: dict) -> str:
    ss = 'тип,количество\n'

    for key, value in sorted(counts.items()):
        ss += f'{key},{value}\n'

    return ss
        
    
    
