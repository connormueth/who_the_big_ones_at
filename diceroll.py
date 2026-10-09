import random

def main():

    diceroll_1 = 0
    diceroll_2 = 0
    diceroll_total = 0

    counter = 0

    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    count_11 = 0
    count_12 = 0

    while True:
        diceroll_1 = roll()
        diceroll_2 = roll()
        diceroll_total = calc_total(diceroll_1, diceroll_2)
        counter += 1
        display(counter, diceroll_1, diceroll_2, diceroll_total)
        if diceroll_total == 2:
            count_2 += 1
        if diceroll_total == 3:
            count_3 += 1
        if diceroll_total == 4:
            count_4 += 1
        if diceroll_total == 5:
            count_5 += 1
        if diceroll_total == 6:
            count_6 += 1
        if diceroll_total == 7:
            count_7 += 1
        if diceroll_total == 8:
            count_8 += 1
        if diceroll_total == 9:
            count_9 += 1
        if diceroll_total == 10:
            count_10 += 1
        if diceroll_total == 11:
            count_11 += 1
        if diceroll_total == 12:
            count_12 += 1
        roll_again = input("Press ENTER to roll again\n"
                           "Type 'exit' to view statistics and exit game")
        if roll_again.lower() == "exit":
            print("Game Statistics")
            print("2s count:  {}  --  {:.1f}%".format(count_2, (count_2 / counter)* 100))
            print("3s count:  {}  --  {:.1f}%".format(count_3, (count_3 / counter)* 100))
            print("4s count:  {}  --  {:.1f}%".format(count_4, (count_4 / counter)* 100))
            print("5s count:  {}  --  {:.1f}%".format(count_5, (count_5 / counter)* 100))
            print("6s count:  {}  --  {:.1f}%".format(count_6, (count_6 / counter)* 100))
            print("7s count:  {}  --  {:.1f}%".format(count_7, (count_7 / counter)* 100))
            print("8s count:  {}  --  {:.1f}%".format(count_8, (count_8 / counter)* 100))
            print("9s count:  {}  --  {:.1f}%".format(count_9, (count_9 / counter)* 100))
            print("10s count: {}  --  {:.1f}%".format(count_10, (count_10 / counter) * 100))
            print("11s count: {}  --  {:.1f}%".format(count_11, (count_11 / counter) * 100))
            print("12s count: {}  --  {:.1f}%".format(count_12, (count_12 / counter) * 100))
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