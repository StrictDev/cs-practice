

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
