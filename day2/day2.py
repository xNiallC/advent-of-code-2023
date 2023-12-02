from boilerplate.initialise_input import InitialiseInput


def main():
    initialised_input = InitialiseInput()
    games = initialised_input.get_text_content()

    sum_of_powers = 0

    for game in games:
        split_game = game.split(": ")
        game_data = split_game[1]

        game_min_possible_cube_amounts = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        game_steps = game_data.split("; ")

        for game_step in game_steps:
            game_sub_steps = game_step.split(", ")
            for sub_step in game_sub_steps:
                split_sub_step = sub_step.split(" ")
                cube_count = int(split_sub_step[0])
                cube_colour = split_sub_step[1]

                # Min possible should be minimum of either the current cube count or the current min possible
                game_min_possible_cube_amounts[cube_colour] = max(
                    cube_count, game_min_possible_cube_amounts[cube_colour]
                )

        power_of_cube_amounts = (game_min_possible_cube_amounts["red"] * game_min_possible_cube_amounts["green"] * game_min_possible_cube_amounts["blue"])
        sum_of_powers += power_of_cube_amounts

    print(sum_of_powers)


if __name__ == "__main__":
    main()
