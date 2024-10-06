import argparse

# https://stackoverflow.com/questions/27146262/create-variable-key-value-pairs-with-argparse-python
class kwargs_append_action(argparse.Action):
  """
  argparse action to split an argument into KEY=VALUE form
  on append to a dictionary.
  """

  def __call__(self, parser, args, values, option_string=None):
    try:
      #small edit to split after first ocurrence
      d = dict(map(lambda x: x.split('=', 1), values))
    except ValueError as ex:
      raise argparse.ArgumentError(self, f"Could not parse argument \"{values}\" as k1=v1 k2=v2 ... format")
    setattr(args, self.dest, d)