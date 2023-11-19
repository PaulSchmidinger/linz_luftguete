import requests
import json
import datetime

#logging
def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S-%Z'
    now = datetime.datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open('jsondump/jsondump.log','a') as f:
        f.write(timestamp + ';' + message + '\n')

#API
APIs = {
    "Linz 24er-Turm":"https://www2.land-oberoesterreich.gv.at/imm/jaxrs/messwerte/json?stationcode=S415",
    "Linz Chemiepark":"https://www2.land-oberoesterreich.gv.at/imm/jaxrs/messwerte/json?stationcode=C001",
    "Linz Goethestraße":"https://www2.land-oberoesterreich.gv.at/imm/jaxrs/messwerte/json?stationcode=L001",
    "Linz Neue Welt":"https://www2.land-oberoesterreich.gv.at/imm/jaxrs/messwerte/json?stationcode=S416",
    "Linz Römerberg":"https://www2.land-oberoesterreich.gv.at/imm/jaxrs/messwerte/json?stationcode=S431",
    "Linz Schlossmuseum":"https://www2.land-oberoesterreich.gv.at/imm/jaxrs/messwerte/json?stationcode=L002",
    "Linz Stadtpark":"https://www2.land-oberoesterreich.gv.at/imm/jaxrs/messwerte/json?stationcode=S184",
    "Linz Sternwarte":"https://www2.land-oberoesterreich.gv.at/imm/jaxrs/messwerte/json?stationcode=L003",
    "Freinberg-Sender":"https://www2.land-oberoesterreich.gv.at/imm/jaxrs/messwerte/json?stationcode=S425"
}

#download
now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")

for key in APIs:
    try:
        response = requests.get(APIs[key])
        data = response.json()
        #save data to file
        with open("jsondump/"+now+"_"+key+".json", "w") as outfile:
            json.dump(data, outfile)
        #log
        print(key, ": ", APIs[key])
        print(data)
        log(key + " " + APIs[key])
    except:
        print(key, "Error")
        log(key + " Error")
