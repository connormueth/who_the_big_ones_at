import random

def main():

    diceroll_1 = 0
    diceroll_2 = 0
    diceroll_total = 0
    counter = 0

    while True:
        diceroll_1 = roll()
        diceroll_2 = roll()
        diceroll_total = calc_total(diceroll_1, diceroll_2)
        counter += 1
        display(counter, diceroll_1, diceroll_2, diceroll_total)
        roll_again = input("Press ENTER to roll again, or type 'exit' to quit")
        if roll_again.lower() == "exit":
            break

def roll():
    diceroll = random.randrange(1,7,1)
    return diceroll

def calc_total(diceroll_1, diceroll_2):
    diceroll_total = diceroll_1 +diceroll_2
    return diceroll_total

def display(counter, diceroll_1, diceroll_2, diceroll_total):
    print("Roll #{}\n"
          "Dice A: {}\n"
          "Dice B: {}\n"
          "Total Roll: {}".format(counter, diceroll_1, diceroll_2, diceroll_total))

#def count(counter):
    counter = counter + 1
    return counter

main()