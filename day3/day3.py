from curses.ascii import isdigit
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

    # If a number in the number tracker is adjacent, above, below, or diagonal to a symbol in the symbol tracker, it is valid
    # As numbers span multiple Y values, we need to compare the symbol Y to any of the number Ys
    for number in number_tracker:
        using_number = number[0]
        number_x = number[1]
        number_ys = number[2]

        for symbol in symbol_tracker:
            symbol_x = symbol[1]
            symbol_y = symbol[2]

            # If the symbol and the number are on the same line, we see if the symbols Y value is between -1 and 1 of the numbers Y value
            # if the symbol is on the line above the number, or the line below the number, we see if the symbols Y value is between -1 and 1 of the numbers Y value
            if (
                symbol_x == number_x
                or symbol_x == number_x - 1
                or symbol_x == number_x + 1
            ):
                lower_y_bound = number_ys[0] - 1
                upper_y_bound = number_ys[-1] + 1
                if symbol_y >= lower_y_bound and symbol_y <= upper_y_bound:
                    valid_numbers.append(using_number)
                    break

    final_number = 0
    for valid_number in valid_numbers:
        final_number += int(valid_number)

    print(final_number)


if __name__ == "__main__":
    main()
