values, rows = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5], []
for pos, center in enumerate(values):
    left, right = values[pos-1], values[pos+1] if pos != len(values)-1 else values[0]
    rows.append([[left, center, right], left + center + right])

[print(row) for row in rows]

