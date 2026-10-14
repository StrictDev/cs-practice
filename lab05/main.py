from tablestats import read_rows, count_types, total_minutes, to_csv

filename = input()

with open(filename, 'r', encoding='utf-8') as table:
    rows = read_rows(table.readlines())

    print(len(rows))
    print(len(count_types(rows)))
    print(total_minutes(rows, 'ошибка'))

with open('summary.csv', 'w', encoding='utf-8') as out:
    counts = count_types(rows)
    out.write(to_csv(counts))

# if __name__ == '__main__':
    # print(rows)
    # print(count_types(rows))
    # print(total_minutes(rows, 'ошибка'))
    # print(to_csv({'ошибка': 4, 'запуск': 4}))
    # print(read_rows(["дата,тип,минуты", "2026-03-01,запуск,1.5", \
    #                 "2026-03-01,ошибка,0.4", "2026-03-02,ошибка,0.6", \
    #                 "2026-03-02,проверка,3"]))
