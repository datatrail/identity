import yaml
import os
from yaml import SafeLoader
from .connectors.connector import connect

def main(input_data, config):
  fileName = os.path.join(os.path.dirname(__file__), "inputFiles", "GeanonimiseerdeInput.txt")
  fwfConfig = os.path.join(os.path.dirname(__file__), "configs", "ihvpb.yml")

  with open(fwfConfig) as f:
    config_data = yaml.load(f, Loader=SafeLoader)

  standardisationRulesFile = os.path.join(os.path.dirname(__file__), config_data["specs"]["standardisationRules"])
  with open(standardisationRulesFile) as f:
    config_functions = yaml.load(f, Loader=SafeLoader)

  context = {
    "fileName": fileName,
    **config_data,
    **config_functions
  }

  output_data = connect(fileName, context)
  return output_data
