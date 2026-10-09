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
        display(counter, diceroll_1, diceroll_2, diceroll_total)
        rollcounts[diceroll_total] += 1
        roll_again = input("Press ENTER to roll again\n"
                           "Type 'exit' to view statistics and exit game")
        if roll_again.lower() == "exit":
            print("Game Statistics")
            print("2s count:  {}  --  {:.1f}%".format(rollcounts[2], (rollcounts[2] / counter)* 100))
            print("3s count:  {}  --  {:.1f}%".format(rollcounts[3], (rollcounts[3] / counter)* 100))
            print("4s count:  {}  --  {:.1f}%".format(rollcounts[4], (rollcounts[4] / counter)* 100))
            print("5s count:  {}  --  {:.1f}%".format(rollcounts[5], (rollcounts[5] / counter)* 100))
            print("6s count:  {}  --  {:.1f}%".format(rollcounts[6], (rollcounts[6] / counter)* 100))
            print("7s count:  {}  --  {:.1f}%".format(rollcounts[7], (rollcounts[7] / counter)* 100))
            print("8s count:  {}  --  {:.1f}%".format(rollcounts[8], (rollcounts[8] / counter)* 100))
            print("9s count:  {}  --  {:.1f}%".format(rollcounts[9], (rollcounts[9] / counter)* 100))
            print("10s count: {}  --  {:.1f}%".format(rollcounts[10], (rollcounts[10] / counter) * 100))
            print("11s count: {}  --  {:.1f}%".format(rollcounts[11], (rollcounts[11] / counter) * 100))
            print("12s count: {}  --  {:.1f}%".format(rollcounts[12], (rollcounts[12] / counter) * 100))
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

main()