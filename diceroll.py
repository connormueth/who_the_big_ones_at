import random

def main():

    diceroll_1 = 0
    diceroll_2 = 0
    diceroll_total = 0

    counter = 0

    rollcounts = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0
        }

    while True:
        diceroll_1 = roll()
        diceroll_2 = roll()
        diceroll_total = calc_total(diceroll_1, diceroll_2)
        counter += 1
        rollcounts[diceroll_total] += 1
        display(counter, diceroll_1, diceroll_2, diceroll_total)
        roll_again = input("Press ENTER to roll again\n"
                           "Type 'x' to view statistics and exit game")
        if roll_again.lower() == "x":
            statistics(rollcounts, counter)
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

def statistics(rollcounts, counter):
    print("{:>3} {:>4} {:>5}".format("Roll", "Hits", "%"))
    print("-" * 20)
    for dice_total in rollcounts:
        print("{:>3} {:>4} {:>6.1f}".format(dice_total, rollcounts[dice_total], (rollcounts[dice_total] / counter * 100)))

main()





