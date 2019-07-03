
name = input("What is your name? ")
product = input("What would you like to buy " + name + "? ")
cost = float(input("How much does " + product + " cost? "))
moneyPaid = float(input("How much did you pay? "))
change = round(moneyPaid - cost, 2)
print("Cost: " + str(cost) + " less money paid: " + str(moneyPaid) + " gives change of: " + str(change))

# while True:
#     change = float(input("How much change is owed?"))
#     if change >= 0:
#         break

fiftyPounds = 50.00
twentyPounds = 20.00
tenPounds = 10.00
fivePounds = 5.00
twoPound = 2.00
onePound = 1.00
fiftyPence = 0.50
twentyPence = 0.20
tenPence = 0.10
fivePence = 0.05
twoPence = 0.02
onePence = 0.01


print()
print("The shortest amount of change is:")

if change / fiftyPounds >= 1:
    numberOf50Pounds = int(change / fiftyPounds)
    change = round(change - (numberOf50Pounds * fiftyPounds), 2)
    print("Number of £50 notes: ", numberOf50Pounds)

if change / twentyPounds >= 1:
    numberOf20Pounds = int(change / twentyPounds)
    change = round(change - (numberOf20Pounds * twentyPounds), 2)
    print("Number of £20 notes: ", numberOf20Pounds)

if change / tenPounds >= 1:
    numberOf10Pounds = int(change / tenPounds)
    change = round(change - (numberOf10Pounds * tenPounds), 2)
    print("Number of £10 notes: ", numberOf10Pounds)

if change / fivePounds >= 1:
    numberOf5Pounds = int(change / fivePounds)
    change = round(change - (numberOf5Pounds * fivePounds), 2)
    print("Number of £5 notes: ", numberOf5Pounds)

if change / twoPound >= 1:
    numberOf2Pound = int(change / twoPound)
    change = round(change - (numberOf2Pound * twoPound), 2)
    print("Number of £2 coins: ", numberOf2Pound)

if change / onePound >= 1:
    numberOf1Pound = int(change / onePound)
    change = round(change - (numberOf1Pound * onePound), 2)
    print("Number of £1 coins: ", numberOf1Pound)

if change / fiftyPence >= 1:
    numberOf50Pence = int(change / fiftyPence)
    change = round(change - (numberOf50Pence * fiftyPence), 2)
    print("Number of 50p coins: ", numberOf50Pence)

if change / twentyPence >= 1:
    numberOf20Pence = int(change / twentyPence)
    change = round(change - (numberOf20Pence * twentyPence), 2)
    print("Number of 20p coins: ", numberOf20Pence)

if change / tenPence >= 1:
    numberOf10pence = int(change / tenPence)
    change = round(change - (numberOf10pence * tenPence), 2)
    print("Number of 10p coins: ", numberOf10pence)

if change / fivePence >= 1:
    numberOf5pence = int(change / fivePence)
    change = round(change - (numberOf5pence * fivePence), 2)
    print("Number of 5p coins: ", numberOf5pence)

if change / twoPence >= 1:
    numberOf2pence = int(change / twoPence)
    change = round(change - (numberOf2pence * twoPence), 2)
    print("Number of 2p coins: ", numberOf2pence)

if change / onePence >= 1:
    numberOf1pence = int(change / onePence)
    change = round(change - (numberOf1pence * onePence), 2)
    print("Number of 1p coins: ", numberOf1pence)

print(name + ", you are now the proud owner of " + product)


