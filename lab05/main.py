from tablestats import read_rows, count_types, total_minutes, to_csv

filename = 'events.csv'

with open(filename, 'r', encoding='utf-8') as table:
    rows = read_rows(table)

    print(len(rows) // 3)
    print(len(count_types(rows)))
    print(total_minutes(rows, 'ошибка'))

with open('summary.csv', 'w', encoding='utf-8') as out:
    counts = count_types(rows)
    out.write(to_csv(counts))
    pass

# if __name__ == '__main__':
    # print(rows)
    # print(count_types(rows))
    # print(total_minutes(rows, 'ошибка'))
    # print(to_csv({'ошибка': 4, 'запуск': 4}))
