pattern = int(input("Enter the size of the pattern: "))
while pattern <= 0:
    print("Please enter a positive integer.")
    pattern = int(input("Enter the size of the pattern: "))

row = 0
while row < pattern:
    col = 0
    while col < pattern:
        print("*", end="")
        col += 1
    print()  
    row += 1



    