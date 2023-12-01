from curses.ascii import isdigit
from boilerplate.initialise_input import InitialiseInput

string_digit_of_digits = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

string_words_of_digits = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

def main():
    initialised_input = InitialiseInput()
    calibration_document = initialised_input.get_text_content()

    total_value = 0

    for calibration_line in calibration_document:
        number_of_characters = len(calibration_line)
        digits = ""

        digit_map_lower_bound = {}
        digit_map_upper_bound = {}

        for int_digit in string_digit_of_digits:
            # Get first instance of digit in string
            digit_map_lower_bound[int_digit] = calibration_line.find(int_digit)
        for string_digit in string_words_of_digits:
            # Get first instance of digit in string
            digit_map_lower_bound[string_digit] = calibration_line.find(string_digit)


        for int_digit in string_digit_of_digits:
            # Get last instance of digit in string
            digit_map_upper_bound[int_digit] = calibration_line.rfind(int_digit)
        for string_digit in string_words_of_digits:
            # Get last instance of digit in string
            digit_map_upper_bound[string_digit] = calibration_line.rfind(string_digit)

        # Strip -1 values from maps
        digit_map_lower_bound = {k: v for k, v in digit_map_lower_bound.items() if v != -1}
        digit_map_upper_bound = {k: v for k, v in digit_map_upper_bound.items() if v != -1}

        # Get the lowest index item in the map
        lowest_index = min(digit_map_lower_bound, key=digit_map_lower_bound.get)
        # Get the highest index item in the map
        highest_index = max(digit_map_upper_bound, key=digit_map_upper_bound.get)

        def convert_word_to_digit(word):
            if word in string_words_of_digits:
                return string_digit_of_digits[string_words_of_digits.index(word)]
            else:
                return word
            
        # Convert the lowest/highest index items to digits
        lowest_index = convert_word_to_digit(lowest_index)
        highest_index = convert_word_to_digit(highest_index)

        print(lowest_index + highest_index)
        total_value += int(lowest_index + highest_index)

    print(total_value)


if __name__ == "__main__":
    main()
