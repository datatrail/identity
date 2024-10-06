from .capitalize import capitalize

def function_wrapper(func):
    def inner_func(data):
        return [func(record) for record in data]

    return inner_func

func_wrap = function_wrapper(capitalize)

def main(input_data, config):
  output_data = func_wrap(input_data["input_file"])
  return output_data
