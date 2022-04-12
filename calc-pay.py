# exercise for if-else loop

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

pay=0

if h>=40:
    n=h-40
    pay=(40*r)  + (n*(r*1.5))
else:
    pay=r*h

print(str(pay))
