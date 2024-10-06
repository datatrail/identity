import json
import time


def trim(record):
    for subject in record["keyPairVars"]:

        if len(record["keyPairVars"][subject]) > 0:
            record["keyPairVars"][subject]["value"] = record["keyPairVars"][subject][
                "value"
            ].strip()
    return record
