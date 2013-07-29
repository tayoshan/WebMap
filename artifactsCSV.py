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
        web.header('Content-disposition', 'attachment; filename=artifactsCSV.csv')
        kml = web.input()
       
        kml = urllib.unquote(kml["jsondata"])
        x = json.loads(kml)
        csv = []
        csv.append("Artifact ID, Trench, Description, Fabric, Chronology, X Coordinate, Y Coordinate\n")






        for feature in x["features"]:
            row = []
            row.append(feature["properties"]["catalogid"].replace(",", "-"))
            row.append(feature["properties"]["trench"].replace(",", "-"))
            row.append(feature["properties"]["name"].replace(",", "-"))
            row.append(feature["properties"]["fabric"].replace(",", "-"))
            row.append(feature["properties"]["chronology"].replace(",", "-"))
            row.append(str(feature["geometry"]["coordinates"][0]))
            row.append(str(feature["geometry"]["coordinates"][1]) + "\n")

            csv.append(",".join(row))
        csv = "".join(csv)
        return csv
    
application = web.application(urls, globals()).wsgifunc()
