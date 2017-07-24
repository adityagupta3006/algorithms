#!/bin/python
def displayPathtoPrincess(n,grid):
    for idx, row in enumerate(grid):
        if 'p' in row:
            p = idx, row.index('p')
        if 'm' in row:
            m = idx, row.index('m')
    row = p[0]-m[0]
    col = p[1]-m[1]
    return ''.join(['UP\n'*abs(row) if row<0 else 'DOWN\n'*row, 
                    'LEFT\n'*abs(col) if col<0 else 'RIGHT\n'*col ])
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

print displayPathtoPrincess(m,grid)
