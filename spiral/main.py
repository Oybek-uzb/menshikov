fin  = open("/home/oybek/menshikov/spiral/input.txt")
fout = open("/home/oybek/menshikov/spiral/output.txt","a")

a = int(fin.readline())
target = a*a

pos_x = 0
pos_y = -1

res = [[0 for i in range(0, a)] for j in range(0, a)]

iteration = 0
counter = 1

def to_right(iter):
    global counter, pos_x, pos_y
    iter = a - 2*iter

    for i in range(0, iter):
        if counter > target:
            break
        pos_y += 1

        res[pos_x][pos_y] = str(counter)
    
        counter += 1

def to_bottom(iter):
    global counter, pos_x, pos_y
    iter = a - (2*iter+1)

    for i in range(0, iter):
        if counter > target:
            break
        pos_x += 1

        res[pos_x][pos_y] = str(counter)

        counter += 1

def to_left(iter):
    global counter, pos_x, pos_y
    iter = a - (2*iter+1)

    for i in range(0, iter):
        if counter > target:
            break
        pos_y -= 1

        res[pos_x][pos_y] = str(counter)

        counter += 1

def to_top(iter):
    global counter, pos_x, pos_y
    iter = a - (2*iter+2)

    for i in range(0, iter):
        if counter > target:
            break
        pos_x -= 1

        res[pos_x][pos_y] = str(counter)

        counter += 1

while counter <= target:
    to_right(iteration)
    to_bottom(iteration)
    to_left(iteration)
    to_top(iteration)

    iteration += 1

for i in res:
    fout.write(" ".join(i) + "\n")

fin.close()
fout.close()

# Done successfully, Alhamdulillah