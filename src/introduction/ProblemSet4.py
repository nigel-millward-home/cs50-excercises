cardNumber = input("Please enter your credit card number: ")

if len(cardNumber) != 16:
    print("INVALID")

firstDigit = cardNumber[0]

if firstDigit == "3":
    print("American Express")
elif firstDigit == "4":
    print("VISA")
elif firstDigit == "5":
    print("MASTER CARD")
