import random

def main():

    diceroll_1 = 0
    diceroll_2 = 0
    diceroll_total = 0
    eventroll = 0
    num_counter = 0
    event_counter = 0
    barb_position = 0

    num_rollcounts = {
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
        12: 0,
        }

    event_rollcounts = {
        "black": 0,
        "blue": 0,
        "green": 0,
        "yellow": 0
    }

    while True:
        diceroll_1 = roll()
        diceroll_2 = roll()
        diceroll_total = calc_total(diceroll_1, diceroll_2)
        eventroll, barb_position = event(barb_position)
        if barb_position >= 7:
            barb_position = 0
        num_counter += 1
        event_counter += 1
        num_rollcounts[diceroll_total] += 1
        event_rollcounts[eventroll] += 1
        display(num_counter, diceroll_1, diceroll_2, diceroll_total, eventroll, barb_position)
        roll_again = input("Press ENTER to roll again\n"
                           "Type 'x' to view statistics and exit game")
        if roll_again.lower() == "x":
            statistics(num_rollcounts, event_rollcounts, num_counter)
            break

def roll():
    diceroll = random.randrange(1,7,1)
    return diceroll

def calc_total(diceroll_1, diceroll_2):
    diceroll_total = diceroll_1 +diceroll_2
    return diceroll_total

def display(num_counter, diceroll_1, diceroll_2, diceroll_total, eventroll, barb_position):
    print("Roll #{}\n"
          "Dice A: {}\n"
          "Dice B: {}\n"
          "Total Roll: {}\n"
          "Event Dice: {}\n"
          "Barb Position: {}/7".format(num_counter, diceroll_1, diceroll_2, diceroll_total, eventroll, barb_position))

def statistics(num_rollcounts, event_rollcounts, num_counter):
    print("*" * 20)
    print("{:>6} {:>6} {:>6}".format("Roll", "Hits", "%"))
    print("*" * 20)
    for dice_total in num_rollcounts:
        print("{:>6} {:>5} {:>7.1f}".format(
                                            dice_total,
                                            num_rollcounts[dice_total],
                                            (num_rollcounts[dice_total] / num_counter * 100)))

    print("*" * 20)
    for event in event_rollcounts:
        print("{:>6} {:>5} {:>7.1f}".format(
                                            event,
                                            event_rollcounts[event],
                                            (event_rollcounts[event] / num_counter * 100)))

def event(barb_position):
    event = ["black",
             "black",
             "black",
             "blue",
             "green",
             "yellow"
             ]
    eventroll= random.choice(event)
    if eventroll == "black":
        barb_position += 1
    return eventroll, barb_position

main()





