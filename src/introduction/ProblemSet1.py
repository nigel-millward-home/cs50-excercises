while True:
    height = int(input("Type in Mario height: "))
    if height >= 1 and height <= 8:
        break

for i in range(1, height + 1):

    # print the spaces
    number_of_spaces = height - i
    print((height - i) * " ", end="")

    # print the xs
    print("x" * i)
