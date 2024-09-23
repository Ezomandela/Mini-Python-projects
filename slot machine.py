import random

MAX_LINE = 3
MIN_BET=1
MAX_BET=100

rows=3
colums=3

symbole_count={
    'A':2,
    'B':4,
    'C':6,
    'D':8
}

symbole_value={
    'A':5,
    'B':4,
    'C':3,
    'D':2
}
def get_winning(colmuns,lines,bet,values):
    winning=0
    winning_lines=[]
    for line in range(lines):
        symbol=colmuns[0][lines]
        for column in colmuns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
            else:
                winning += values[symbol] * bet
            winning_lines.append(line + 1 )
        return winning,winning_lines
def slot_sppin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbole_count in symbols.items():
        for _ in range(symbole_count):
            all_symbols.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbole=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbole)
            current_symbole.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
         for i,j in enumerate (columns):
             if i != len(columns) -1:
                 print(j[row],end="|")
             else:
                 print(j[row],end=" ")
         print()
def deposite():
    while True:
        money = input(" amount you want to deposite $ :")
        if money.isdigit():
            money = int(money)
            if money > 0:
                break
            else:
                print(" the amount must grater than 0")
        else:
            print("please input the valid amount of money")
    return money
def lines():
    while True:
        lin = input("input the number of lines you want to put (1-"+ str(MAX_LINE) + ")? ")
        if lin.isdigit():
            lin = int(lin)
            if 1<=lin<=MAX_LINE:
                break
            else:
                print("print the correct lines ")
        else:
            print("please input the valid amount of lines ")
    return lin
def bet():
    while True:
        bet = input("input the amount you want to bet ( "+ str(MIN_BET)+") - ("+ str(MAX_BET)+")")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print("print the correct bet points  ")
        else:
            print("please input the valid amount of bets ")
    return bet

def game(balance):
    line = lines()
    while True:
        bet1 = bet()
        total_amount = bet1 * line
        if total_amount > balance:
            print(f"you must have the balance to compute with this bet your balance is  {balance}")
        else:
            break
    slots = slot_sppin(rows, colums, symbole_count)
    print_slot_machine(slots)
    winnings, winning_liness = get_winning(slots, line, bet1, symbole_value)
    print(winnings)
    print(f"your winning is ", *winning_liness)
    return winnings - total_amount
def main():
    balance = deposite()
    while True:
        print(f"current balance is ${balance} ")
        spin=input("press eneter to spin (q to quite )")
        if  spin == "q":
            break
        else:
            balance += game(balance)
        print(f"you left with{balance}")


main()

