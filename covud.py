import requests
import json
#To get DAILY Report Totals use the link below it
url = "https://covid-19-data.p.rapidapi.com/report/totals"

#To Get Latest Totals use the link below it
# url = "https://covid-19-data.p.rapidapi.com/totals"

# For the Current Date
querystring = {"date":"2020-07-21"}
#otherwise remove it
headers = {
    'x-rapidapi-key': "9f2b8b4c5fmshd29147ce2d8557ep196df0jsn6755ff3d09f7",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

#To Get total cases use the line below this
# response = requests.request("GET", url, headers=headers)



response = requests.request("GET", url, headers=headers, params=querystring)
response_data=response.json()
data=response.text
parsed=json.loads(data)
print(json.dumps(parsed,indent=4))

# data=parsed["confirmed"]

for s in range(len(data)):
    if data["confirmed"]==to_find:
        print("The confirmed cases are".format(data["confirmed"]))

