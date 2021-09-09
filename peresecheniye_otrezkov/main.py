from os import EX_OSFILE


fin  = open("/home/oybek/menshikov/peresecheniye_otrezkov/input.txt")
fout = open("/home/oybek/menshikov/peresecheniye_otrezkov/output.txt","a")

a_x1, a_y1 = map(int, fin.readline().split())
a_x2, a_y2 = map(int, fin.readline().split())
b_x1, b_y1 = map(int, fin.readline().split())
b_x2, b_y2 = map(int, fin.readline().split())

def coefficients(x1, y1, x2, y2):
    coefs = list()
    if y1 == 0 and y2 == 0:
        coefs.append(0, 0)
        return coefs
    
    

fin.close()
fout.close()

# Done successfully, Alhamdulillah