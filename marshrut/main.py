fin  = open("/home/oybek/menshikov/marshrut/input.txt")
fout = open("/home/oybek/menshikov/marshrut/output.txt","a")

n = int(fin.readline())

table = []
# summs = []
way = []

for i in range(0, n):
    table.append([int(char) for char in fin.readline().rstrip()])
    # summs.append([0 for i in range(0, n)])
    way.append(["-" for i in range(0, n)])

way[n-1][n-1] = "#"

def min_summ(a, b, x, y):
    if a <= b:
        way[x-1][y] = "#"
    else:
        way[x][y-1] = "#"

    return min(a, b)

def marshrut(i:int, j:int):
    if i == 0 and j == 0:
        way[0][0] = "#"
        return table[0][0]
    
    if i == 0:
        # way[0][j] = "#"
        return marshrut(0, j-1) + table[0][j]
    if j == 0:
        # way[i][0] = "#"
        return marshrut(i-1, 0) + table[i][0]

    return min_summ(marshrut(i-1, j), marshrut(i, j-1), i, j) + table[i][j]

print(marshrut(n-1, n-1))
print(way)

fin.close()
fout.close()

# not completed. This program returns min summ of array, but can't show that way yet.