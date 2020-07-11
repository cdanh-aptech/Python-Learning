import math

print("Giai Phuong Trinh Bac 2 (a2x + bx - c = 0)")
a = int(input("Nhap he so a: "))
b = int(input("Nhap he so b: "))
c = int(input("Nhap he so c: "))

if a == 0:
    print("La phuong trinh bac 2, x = {0}". format(c/b))
else:
    delta = b*b - 4 * a * c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / 2*a
        print("Phuong trinh co nghiem kep x1 = x2 = {0}".format(x))
    else:
        x1 = -b + math.sqrt(delta)
        x2 = -b - math.sqrt(delta)
        print("Phuong trinh co 2 nghiem")
        print("x1 = {0}". format(x1))
        print("x2 = {0}". format(x2))