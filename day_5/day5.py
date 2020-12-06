passes = []
rows = []
cols = []
ids = []
with open('source.txt', 'r') as source:
    for item in source:
        passes.append(item)
for item in passes:
    rangetop = 127
    rangebottom = 0
    coltop = 7
    colbottom = 0
    for i, value in enumerate(item):
        if i < 6:
            if value == 'F':
                rangetop -= (rangetop - rangebottom) // 2 + 1
            else:
                rangebottom += (rangetop - rangebottom) // 2 + 1
        if i == 6:
            if value == 'F':
                rows.append(rangebottom)
            else:
                rows.append(rangetop)
        if 6 < i < 9:
            if value == 'L':
                coltop -= (coltop - colbottom) // 2 + 1
            else:
                colbottom += (coltop - colbottom) // 2 + 1
        if 9 == i:
            if value == 'L':
                cols.append(colbottom)
            else:
                cols.append(coltop)
for i, item in enumerate(rows):
    ids.append(item * 8 + cols[i])
# first part
print(max(ids))
# second part
print(sorted(ids))
yourseat = 0
for i in range(0, len(ids)):
    if min(ids) < i < max(ids) and i not in ids:
        yourseat = i
print(yourseat)
