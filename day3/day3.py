from curses.ascii import isdigit
from re import I
from tabnanny import filename_only
from boilerplate.initialise_input import InitialiseInput


def main():
    initialised_input = InitialiseInput()
    engine_schematics = initialised_input.get_text_content()

    number_tracker = []
    symbol_tracker = []
    valid_numbers = []

    for line_index, line in enumerate(engine_schematics):
        tracking_number = ""
        tracking_number_indexes = []
        for character_index, character in enumerate(line):
            if character.isdigit():
                tracking_number += character
                tracking_number_indexes.append(character_index)
                # If we are at the end of the line, we need to add the number to the number tracker
                if character_index == len(line) - 1:
                    number_tracker.append(
                        [tracking_number, line_index, tracking_number_indexes]
                    )
            else:
                if character != ".":
                    symbol_tracker.append([character, line_index, character_index])

                if tracking_number != "":
                    number_tracker.append(
                        [tracking_number, line_index, tracking_number_indexes]
                    )
                    tracking_number = ""
                    tracking_number_indexes = []

    # Iterate each symbol in symbol tracker
    # If the symbol is a *
    # If the hash has TWO numbers in the number tracker that are adjacent, above, below, or diagonally adjacent
    # Multiply the two numbers together and add to a list of valid numbers
    for symbol in symbol_tracker:
        symbol_value = symbol[0]
        symbol_x = symbol[1]
        symbol_y = symbol[2]

        if symbol_value == "*":
            adjacent_numbers = []
            for number in number_tracker:
                number_value = number[0]
                number_x = number[1]
                number_ys = number[2]

                if (
                    symbol_x >= number_x - 1 and symbol_x <= number_x + 1
                ):
                    for number_y in number_ys:
                        if (
                            symbol_y >= number_y - 1 and symbol_y <= number_y + 1
                        ):
                            if number_value not in adjacent_numbers:
                                adjacent_numbers.append(number_value)

            if len(adjacent_numbers) == 2:
                valid_numbers.append(adjacent_numbers)

    final_value = 0
    for number_pair in valid_numbers:
        final_value += (int(number_pair[0]) * int(number_pair[1]))

    print(final_value)

if __name__ == "__main__":
    main()
