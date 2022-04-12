# love-calculator exercise

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1=  name1.lower()
name2 = name2.lower()

s1 = 0
s2 = 0

for c in "true":
    s1 = s1 + name1.count(c)
    s1 = s1 + name2.count(c)

for c in "love":
    s2 = s2 + name1.count(c)
    s2 = s2 + name2.count(c)

score = str(s1)+str(s2)
s = int(score)

if s < 10 or s > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif s >=40 and s <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
