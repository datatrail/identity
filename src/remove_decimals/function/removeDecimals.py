from yaml.loader import SafeLoader
import yaml

def removeDecimalsWhenZero(number):
    if number%1==0:
        return int(number)
    else:
        return number


def removeDecimals(record):
    name="removeDecimals"

    for variable_name in record["keyPairVars"]:

        if len(record["keyPairVars"][variable_name]) > 0:
            type = record["keyPairVars"][variable_name]["type"]

            if name in record["keyPairVars"][variable_name]["standardisation_functions"]:
                #THIS SHOULD BE FOR ALL LIKE A STANDARDISATION
                number = record["keyPairVars"][variable_name]["value"].split(",")
                if len(number) > 1:
                    numWithDecimal = str(number[0]) + "." + str(number[1])
                else:
                    numWithDecimal = str(number[0])
                #THIS SHOULD BE CONFIGURATION
                record["keyPairVars"][variable_name]["value"] = removeDecimalsWhenZero(float(numWithDecimal))
   
    return record