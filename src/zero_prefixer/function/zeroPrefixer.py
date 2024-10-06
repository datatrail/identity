from yaml.loader import SafeLoader
import yaml

def addZeros(number):
    stringNumber = str(number)

    while len(stringNumber) < 9:
        stringNumber = "0" + stringNumber

    return str(stringNumber)

def zeroPrefixer(record):
    name="zeroPrefixer"

    for variable in record["keyPairVars"]:
        if variable.strip() == "":
            continue
        if name in record["keyPairVars"][variable]["standardisation_functions"]:
            number = record["keyPairVars"][variable]["value"]
            record["keyPairVars"][variable]["value"] = addZeros(int(number))
    return record
