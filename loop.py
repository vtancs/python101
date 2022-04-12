# loops

largest = 0
smallest = 999
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    #print(num)
    try:
        number = int(num)
    except:
        print("Invalid input")
    else:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

print("Maximum", largest)
print("Minimum ", smallest)
