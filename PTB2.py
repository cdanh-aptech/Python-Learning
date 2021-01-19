import math

def main():
    print("Giai Phuong Trinh Bac 2 (ax2 + bx + c = 0)")
    hs_a = int(input("Nhap he so a: "))
    hs_b = int(input("Nhap he so b: "))
    hs_c = int(input("Nhap he so c: "))
    
    giaiPT(hs_a, hs_b, hs_c)

def giaiPT(a, b, c):
    if a == 0:
        print(f"La phuong trinh bac 1, x = {-c/b}")
    else:
        delta = b*b - (4 * a * c)
        if delta < 0:
            print("Phuong trinh vo nghiem")
        elif delta == 0:
            x = -b / 2*a
            print(f"Phuong trinh co nghiem kep x1 = x2 = {x}")
        else:
            x1 = -b + math.sqrt(delta)
            x2 = -b - math.sqrt(delta)
            print("Phuong trinh co 2 nghiem")
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")

if __name__ == "__main__":
    main()