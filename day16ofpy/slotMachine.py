# python slot machine
import random
def spin_row():
    symbols = ['🍒', '🍊', '🍋', '🔔', '⭐']
    
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("---------------------------------------")
    print(" | ".join(row))
    print("---------------------------------------")
    pass

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 10
        elif row[0] == "🍊":
            return bet * 5
        elif row[0] == "🍋":
            return bet * 3
        elif row[0] == "🔔":
            return bet * 2
        elif row[0] == "⭐":
            return bet * 1
    else:
        return -bet
    pass

def play_again():
    play_again = input("Do you want to play again? (Y/N): ")
    return play_again.upper() == 'Y'
    pass

def main():
    balance = 100

    print("---------------------------------------")
    print("Welcome to the Slot Machine!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("---------------------------------------")

    while balance > 0:
        print("Current balance: ${}".format(balance))
        bet = input("Enter your bet: ") 
        
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue
        
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds.")
            continue
        
        if bet <= 0:
            print("Please enter a valid number.")
            continue

        balance -= bet

        row = spin_row()
        print("Spining..............")
        print_row(row)
        print("Balance: ${}".format(balance))

        payout = get_payout(row, bet)

        if payout > 0:
            print("You won ${}".format(payout))
            balance += payout
        else:
            print("You lost ${}".format(bet))
        
        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.upper() != 'Y':
            break
        
        
        

    print("Game over. Your final balance is ${}".format(balance))
    print("---------------------------------------")
    print("Thank you for playing!")
    print("---------------------------------------")
    print("Bye!")
    pass

if __name__ == '__main__':
    main()

