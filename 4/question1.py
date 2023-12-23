import math


sum = 0
with open("puzzle-input.txt") as file:
    for line in file:
        game_data = line.split(": ")[1].strip().split(" | ")
        winning_numbers = game_data[0].strip().split()
        winning_numbers = [int(i) for i in winning_numbers]
        number_draw = game_data[1].strip().split()
        number_draw = [int(i) for i in number_draw]

        matches = 0
        for number in number_draw:
            for winner in winning_numbers:
                if winner == number:
                    matches += 1

        if matches > 1:
            score = math.pow(2, matches - 1)
        elif matches == 1:
            score = 1
        else:
            score = 0

        sum += int(score)

print(sum)
