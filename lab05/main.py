from tablestats import read_rows, count_types

filename = 'events.csv'

with open(filename, 'r', encoding='utf-8') as table:
    rows = read_rows(table)

if __name__ == '__main__':
    print(rows)
    print(count_types(rows))
