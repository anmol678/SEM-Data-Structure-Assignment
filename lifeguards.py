
for k in range(1, 11):

    maxCovered = 0

    with open(str(k) + '.in', 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        
        shifts = []
        SHIFT_START_INDEX = 0
        SHIFT_END_INDEX = 1

        for i in range(1, n + 1):
            line = lines[i]
            shift = tuple(map(int, line.split()))
            shifts.append(shift)

        shifts.sort(key=lambda a:a[0])

        start = 0
        end = 0
        totalDuration = 0

        for a, b in shifts:
            if end < b:
                start = max(a, end)
                totalDuration += b - start
                end = b

        shifts.append((shifts[n - 1][1], 0))
        minUncovered = totalDuration
        currentEnd = 0

        for i, (a, b) in enumerate(shifts):
            if i == n:
                break

            c, _ = shifts[i + 1]
            uncovered = min(c, b) - max(a, currentEnd)
            minUncovered = min(minUncovered, uncovered)
            currentEnd = max(currentEnd, b)

        maxCovered = totalDuration - max(minUncovered, 0)

    f = open(str(k) + '.out', 'a')
    f.write(str(maxCovered))
    f.close()