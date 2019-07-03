while True:
    height = int(input("Type in Mario height: "))
    if height >= 1 and height <= 100:
        break

for i in range(1, height + 1):

    # print the spaces
    number_of_spaces = height - i
    print((height - i) * " ", end="")

    # print the left xs
    print("x" * i, end="")

    # print the middle spaces
    print("  ", end="")

    # print the right xs
    print("x"* i)