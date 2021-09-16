fin  = open("/home/oybek/menshikov/zmeyka/input.txt")
fout = open("/home/oybek/menshikov/zmeyka/output.txt","a")

number: int = int(fin.readline())
max_count: int = number ** 2
max_iter: int = number - 1

res_arr = [["#" for i in range(0, number)] for j in range(0, number)]

counter: int = 1
iteration: int = 1
is_reached: bool = False

pos_x = 0
pos_y = 0

def draw(side, iteration):
    global counter, max_count, pos_x, pos_y, is_reached

    if counter == max_count:
        return

    if iteration == number - 1:
        is_reached = True

    if side == "right_bottom":
        print(res_arr)
        if pos_x == 0 or pos_x == number - 1:
            if pos_y == number - 1:
                pos_x += 1
                res_arr[pos_x][pos_y] = str(counter)
            else:
                pos_y += 1
                res_arr[pos_x][pos_y] = str(counter)
        elif pos_y == 0 or pos_y == number - 1:
            if pos_x == number - 1:
                pos_y += 1
                res_arr[pos_x][pos_y] = str(counter)
            else:
                pos_x += 1
                res_arr[pos_x][pos_y] = str(counter)
        counter += 1
    else:
        print(res_arr)
        if pos_x == 0:
            for i in range(0, iteration):
                pos_x += 1
                pos_y -= 1
                res_arr[pos_x][pos_y] = str(counter)
                counter += 1
        elif pos_y == 0:
            for i in range(0, iteration):
                pos_x -= 1
                pos_y += 1
                res_arr[pos_x][pos_y] = str(counter)
                counter += 1






res_arr[pos_x][pos_y] = counter
counter += 1

while counter <= max_count:
    draw("right_bottom", iteration)
    draw("diagonal", iteration)

    if is_reached:
        iteration -= 1
    else:
        iteration += 1

print(res_arr)

fin.close()
fout.close()

# Done successfully, Alhamdulillah