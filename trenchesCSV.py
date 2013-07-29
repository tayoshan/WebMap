import web
import csv
import json
import urllib

urls = (
      '/.*', 'hello',
      )

class hello:
    def POST(self):
        web.header('Content-Type', 'text/html')
        web.header('Content-disposition', 'attachment; filename=trenchesCSV.csv')
        kml = web.input()
       
        kml = urllib.unquote(kml["jsondata"])
        x = json.loads(kml)
        csv = []
        csv.append("Trench, Trench Area, Trench Number, Trench ID, Year, Excavator,\n")






        for feature in x["features"]:
            row = []
            row.append(str(feature["properties"]["trench"].replace(",", "-")))
            row.append(str(feature["properties"]["trencharea"].replace(",", "-")))
            row.append(str(feature["properties"]["trenchnumb"].replace(",", "-")))
            row.append(str(feature["properties"]["trenchid"]))
            row.append(str(feature["properties"]["year"]))
            row.append(str(feature["properties"]["excavator"]) + "\n")

            csv.append(",".join(row))
        csv = "".join(csv)
        return csv
    
application = web.application(urls, globals()).wsgifunc()
