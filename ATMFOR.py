def check_amount(amount):
    while amount > 25000:
        amount = int(input("You are exceeding the maximum limit. Please enter an amount below 25000:\n"))
    print("Entered amount of money is =", amount)
    return amount

def check_option(mixed):
    while mixed not in [0, 1]:
        print("""Please select correct option!
                 Do you want to have mixed banknotes?
                 if yes enter 1
                 if no enter 0""")
        mixed = int(input())
    return mixed

def get_mixed_notes(amount, index):
    notes = [100, 50, 20, 10]
    for itrate, value in enumerate(notes[index:]):
        if amount != 0 and amount >= value:
            div = int(amount / value)
            remainder = amount % value
            print(value, "franc notes =", div)
            amount = remainder
        else:
            print(value, "franc notes =", 0)
    print("Rest =", amount)

def get_choice_notes(amount, cash):
    notes = [100, 50, 20, 10]
    for i, value in enumerate(notes):
        if cash == value:
            break
        print(value, "franc notes =", 0)
    get_mixed_notes(amount, i)

def main():
    print("WELCOME TO BANK YOU TRUST")
    print("*************************")

    amount = int(input("HOW MUCH AMOUNT DO YOU WANT TO WITHDRAW?\n"))

    amount = check_amount(amount)

    mixed = int(input("""Do you want to have mixed banknotes?
             if yes enter 1
             if no enter 0\n"""))

    mixed = check_option(mixed)
    i = 0
    if mixed == 1:
        get_mixed_notes(amount, i)
    elif mixed == 0:
        cash = int(input("Which note do you want: 50, 20, 10\n"))
        get_choice_notes(amount, cash)

if __name__ == "__main__":
    main()