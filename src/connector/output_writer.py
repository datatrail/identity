import json


def write_output(data, file_path):
    if file_path is None:
        return None
    with open(file_path, "w") as outfile:
        json.dump(data, outfile, indent=2, sort_keys=True)
