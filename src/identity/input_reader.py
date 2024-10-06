import json


def read_input(input_files):
    input_lists = {}
    for key in input_files:
        input_lists[key] = read_input_file(input_files[key])
    return input_lists


def read_input_file(file_path):
    if file_path is None:
        return None
    else:
        with open(file_path, "r") as infile:
            return json.load(infile)
