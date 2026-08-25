import random


def spin_row():
    symbols = ['🍒', '🍉', '⭐', '🔔', '🍋']

    # list comprehension
    # 1, first basic comprehension
    # results = []

    # for symbol in range(3):
    #     results.append(random.choice(symbols))

    # return results

    # modern approach comprehension
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(' | '.join(row))


def get_payout(row, bet):
    #check if the symbols match in a row

    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '⭐':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🍋':
            return bet * 20

    return 0


def main():
    balance = 100

    print("Welcome to python slots: ")
    print("Symbols: 🍒 🍉 ⭐ 🔔 🍋")

    while balance > 0:
        print(f"Current balance ${balance}")

        bet = input("Place your bet Amount: ")

        if not bet.isdigit():
            print('Please enter a valid amount number')
            continue

        bet = int(bet)

        if bet > balance:
            print("Insuffient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than zero")
            continue

        balance -= bet

        # get the spin row
        row = spin_row()
        print("Spinning . . . \n")
        print_row(row)
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print(f'Sorry you lost this round')

        balance += payout


        play_again = input('Do you want to spin again? (y/n): ')

        if play_again != "y":
            break

    print(f"Thanks for playing, your balance is ${balance}")
     

if __name__ == "__main__":
    main()
