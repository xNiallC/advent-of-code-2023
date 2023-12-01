from boilerplate.initialise_input import InitialiseInput


def main():
    initialised_input = InitialiseInput()
    content = initialised_input.get_text_content()
    print(content)


if __name__ == "__main__":
    main()
