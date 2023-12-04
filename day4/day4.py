from boilerplate.initialise_input import InitialiseInput


def main():
    initialised_input = InitialiseInput()
    scratchcards = initialised_input.get_text_content()

    def get_split_numbers(input):
        return [int(item) for item in input.split(" ") if not not item]

    total_points = 0

    for scratchcard in scratchcards:
        _, scratchcard_content = scratchcard.split(": ")
        winning_numbers, ticket_numbers = scratchcard_content.split(" | ")
        winning_numbers = get_split_numbers(winning_numbers)
        ticket_numbers = get_split_numbers(ticket_numbers)

        # Get intersected list of winning numbers and ticket numbers
        winning_ticket_numbers = list(set(winning_numbers) & set(ticket_numbers))

        if len(winning_ticket_numbers) > 0:
            ticket_points = 1 * (2 ** (len(winning_ticket_numbers) - 1))
            total_points += ticket_points

    print(total_points)

if __name__ == "__main__":
    main()
