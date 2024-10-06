import os
import time
import argparse
from kwargs_append_action import kwargs_append_action

from input_reader import read_input
from function.main import main as main_function
from output_writer import write_output


def main(input_files, config, output_file):
    # convert input data to dict of lists
    input_data = read_input(input_files)
    # call function
    output_data = main_function(input_data, config)
    # write output to file
    write_output(output_data, output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # input files need to be key-value pairs
    parser.add_argument(
        "-i", "--inputfiles", nargs="*", action=kwargs_append_action, default={}
    )
    parser.add_argument(
        "-c", "--config", nargs="*", action=kwargs_append_action, default={}
    )
    # at most 1 single output file supported for now
    parser.add_argument("-o", "--outputfile")

    # extract args
    args = parser.parse_args()
    input_files = args.inputfiles
    config = args.config
    output_file = args.outputfile

    # execute main function
    main(input_files, config, output_file)
