# functions exercise

def computepay(h, r):
    if h>=40:
        n=h-40
        pay=(40*r)  + (n*(r*1.5))
    else:
        pay=r*h
    return pay 

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

p = computepay(hrs, rate)
print("Pay", p)
