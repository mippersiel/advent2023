instances = 0
with open("puzzle-input.txt") as file:
    copies = []
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

        number_of_cards = 1
        if copies:
            number_of_cards += copies.pop(0)

        if matches:
            next_copies = [number_of_cards] * matches
            if len(next_copies) > len(copies):
                diff = len(next_copies) - len(copies)
                copies.extend([0] * diff)
            elif len(copies) > len(next_copies):
                diff = len(copies) - len(next_copies)
                next_copies.extend([0] * diff)
            copies = [sum(x) for x in zip(copies, next_copies)]

        instances += number_of_cards

print(instances)
