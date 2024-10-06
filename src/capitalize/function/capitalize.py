from yaml.loader import SafeLoader
import yaml

def capitalize(record):
    name="capitalize"

    for variable in record["keyPairVars"]:
        if variable.strip() == "":
            continue

        if name in record["keyPairVars"][variable]["standardisation_functions"]:
            record["keyPairVars"][variable]["value"] = record["keyPairVars"][variable]["value"].upper()

    return record
