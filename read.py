import csv
import datetime
import requests 
from requests_toolbelt import MultipartEncoder

with open('glucose-test-data.csv') as file:
    r = csv.reader(file)
    next(r)
    next(r)
    for row in r:
        if row[2] != "":
            if row[4] != "":
                date_time_str = row[2]
                date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')
                date_time_obj_0 = date_time_obj.timestamp()*1000
                print(str(date_time_obj_0) + " " + row[4])

                url = "https://api3.gamebus.eu/v2/activities?dryrun=false&fields=personalPoints.value"

                payload = MultipartEncoder(fields={'activity': '{"gameDescriptor":61,"dataProvider":1,"date":"'+str(int(date_time_obj_0))+'","propertyInstances":[{"property":87,"value":null},{"property":88,"value":'+row[4]+'},{"property":89,"value":"5"}],"players":[340]}'})
                files = [

                ]
                headers = {
                  'Content-Type': payload.content_type, 'Authorization': 'Bearer cf515c07-02cf-441e-b500-e1eb792ce8da'
                }
                # Need to get individual token and replace the token next to Bearer

                response = requests.request("POST", url, headers=headers, data = payload, files = files)

                print(response.text.encode('utf8'))

