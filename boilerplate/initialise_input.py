import sys
import __main__ as main


def get_input_path():
    is_testing = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            is_testing = True
    running_path = main.__file__
    running_path = running_path.split("/")[:-1]
    return "/".join(running_path) + ("/test.txt" if is_testing else "/input.txt")


class InitialiseInput(object):
    def __init__(self, no_strip=False):
        text_filename = get_input_path()
        with open(text_filename) as f:
            content = f.readlines()
        content = [(x.replace("\n", "") if no_strip else x.strip()) for x in content]
        self.text_content = content

    def get_text_content(self):
        return self.text_content
