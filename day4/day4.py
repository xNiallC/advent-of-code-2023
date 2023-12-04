from boilerplate.initialise_input import InitialiseInput


def main():
    initialised_input = InitialiseInput()
    scratchcards = initialised_input.get_text_content()

    num_scratchcards = len(scratchcards)

    def get_split_numbers(input):
        return [int(item) for item in input.split(" ") if not not item]

    # Each scratchcards result (the number of winning numbers), gives you a copy of the next N scratchcards in the pile equal to the result (as long as there are N scratchcards left in the pile, it will stop if there are not enough scratchcards left)
    # Therefore:
    # We start with 1 copy of every scratchcard
    # After processing scratchcard 1, the number of points we get (P), adds 1 copy of the next P scratchcards to the pile (up to the number of scratchcards left)
    # After processing scratchcard 2, the number of points we get (Q), adds 1 copy of the next Q scratchcards to the pile (up to the number of scratchcards left), times the number of copies of scratchcard 2 we have

    scratchcard_result_map = {}
    for i in range(num_scratchcards):
        scratchcard_result_map[i+1] = 1

    for scratchcard_index, scratchcard in enumerate(scratchcards):
        _, scratchcard_content = scratchcard.split(": ")
        scratchcard_number = scratchcard_index + 1
        winning_numbers, ticket_numbers = scratchcard_content.split(" | ")
        winning_numbers = get_split_numbers(winning_numbers)
        ticket_numbers = get_split_numbers(ticket_numbers)

        intersection_of_numbers = list(set(winning_numbers) & set(ticket_numbers))
        current_number_of_scratchcards = scratchcard_result_map[scratchcard_number]

        # In the range of (curr index + 1) to either (curr index + 1 + number of winning numbers) or (num_scratchcards)
        # Add current_number_of_scratchcards to each of the scratchcards in the range
        # If the range is out of bounds, it will just add to the scratchcards that are left
        for i in range(scratchcard_number, min(scratchcard_number + len(intersection_of_numbers), num_scratchcards)):
            scratchcard_result_map[i+1] += current_number_of_scratchcards

    total_used = 0
    for scratchcard_number, number_of_scratchcards in scratchcard_result_map.items():
        total_used += number_of_scratchcards

    print(total_used)



if __name__ == "__main__":
    main()
