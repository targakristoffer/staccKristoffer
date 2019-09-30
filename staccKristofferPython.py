import json
import requests
import pandas as pd
import numpy as np

data = {
  "laanebelop": 2000000,
  "nominellRente": 3,
  "terminGebyr":30,
  "utlopsDato":"2045-01-01",
  "saldoDato":"2020-01-01",
  "datoForsteInnbetaling":"2020-02-01",
  "ukjentVerdi":"TERMINBELOP"
}
api = "https://visningsrom.stacc.com/dd_server_laaneberegning/rest/laaneberegning/v1/nedbetalingsplan?"
#response = requests.post(api, json=data)
#response.status_code
#Post requestet til JSON
r = requests.post(api, json=data)

nedbetalingsplan = r.json()


#nedbetalingsPlan = json.dumps(response.json(), indent=4)
#print(nedbetalingsPlan)
#print(espen)

table = {
    "Restgjeld" : [],
    "Dato" : [],
    "Innbetaling": [],
    "Gebyr": [],
    "Renter": [],
    "Total": []
    }
#for loop, går igjennom json request, data blir lagt inn i tabellen
for item in nedbetalingsplan["nedbetalingsplan"]["innbetalinger"]:
    table["Restgjeld"].append(item["restgjeld"]),
    table["Dato"].append(item["dato"]),
    table["Innbetaling"].append(item["innbetaling"]),
    table["Gebyr"].append(item["gebyr"]),
    table["Renter"].append(item["renter"]),
    table["Total"].append(item["total"]),

df = pd.DataFrame (table)
print(df.round(1))
print("success")
