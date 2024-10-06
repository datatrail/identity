from yaml.loader import SafeLoader
import yaml


def connect(data, configData):
    fileName = configData["fileName"]
    with open(fileName, "r") as f:
        data = list(f)

    arrayRecords = []

    count = 0

    for x in data:
        count = count + 1
        #SHOULD BE CONFIGURABLE
        if count <= configData['specs']["firstRowsToSkip"]:
            continue

        record = { "keyPairVars": {}, "meta": {}}

        startWidth = 0
        endWidth = 0

        variable_ordering = ["Finummer", "Partner_finummer", "Belastingjaar", "Fasesoort", "Middel", "DatumBinnenkomst",
                             "Aangiftesoort", "Volgnummer_onderneming", "Bewering_volgnummer", "Waarde_datum",
                             "Waarde_getal", "Waarde_tekst", "Valutacode", "Valutafactor", "ABS_elementnummer",
                             "BMG_elementnummer", "Heftijdvak_begin", "Heftijdvak_einde", "Heza-soort", "Heza-subsoort"]
        #ADD ALL VALUES FROM FIXED WITH FILE ROW IN KEY PAIR OBJECT
        for variable in variable_ordering:
            variableWidth = int(configData["variables"][variable]["width"])
            endWidth += variableWidth
            record["meta"][variable] = x[startWidth:endWidth]
            startWidth += variableWidth

        keyPairVars = {}

        #HORIZONTAL SHOULD BE ENUM // CAN ALSO BE HANDLED BE A BASE CLASS AND SEPARATE IMPLEMENTATIONS
        if configData["specs"]["type"] == "horizontal":
            for variableForStandardisation in configData["specs"]["variablesForStandardisation"]:
                keyPairValue = {}
                keyPairValue["value"] = record["meta"][variableForStandardisation]
                keyPairVars[variableForStandardisation] = keyPairValue

        if configData["specs"]["type"] == "vertical":
            for variableForStandardisation in configData["specs"]["variablesForStandardisation"]:
                keyPairValue = {}


                fillVerticalVariableValue(keyPairValue, configData, record)

                #ADD ALL VARIABLES WHICH NEEDS TO BE STANDARDISED UNDER THE keyPairVars KEY
                #FOR HORIZONTAL SOURCES THERE CAN BE MULTIPLE VARIABLES IN ONE ROW, FOR VERTICAL SOURCES PROBABLY ONE 
                keyPairVars[record["meta"][variableForStandardisation].strip()] = keyPairValue

        for key, value in keyPairVars.items():
            value["standardisation_functions"] = []
            for specific in configData["standardisations"]["specific"]:
                if key.strip() in \
                        configData["standardisations"]["specific"][specific]:
                    value["standardisation_functions"].append(specific)
            for generic in configData["standardisations"]["generic"]:
                if value["type"] in configData["standardisations"]["generic"][generic]:
                    value["standardisation_functions"].append(generic)
            for category in configData["standardisations"]["categoryBased"]:
                id_list = get_category_ids(configData["standardisations"]["categories"],
                                           configData["standardisations"]["categoryBased"][category])
                if key.strip() in id_list:
                    value["standardisation_functions"].append(category)
        record["keyPairVars"] = keyPairVars

        arrayRecords.append(record)
    
    print("Dataconnector processed " + str(count) + " rows")
    return arrayRecords

def fillVerticalVariableValue(keyPairValue, configData, record):
    for field in configData["specs"]["verticalValueFields"]:
        fieldValue = field["value"]
        fieldType = field["type"]

        if record["meta"][fieldValue] and record["meta"][fieldValue].strip() != "":
            keyPairValue["value"] = record["meta"][fieldValue]
            keyPairValue["type"] = fieldType
            break

    if "value" not in keyPairValue.keys():
        keyPairValue = ""

    return keyPairValue



def get_category_ids(categories: dict, keys: list) -> list[str]:
    id_list = []

    for key, value in categories.items():
        if key in keys:
            id_list.extend(value)
    return id_list
