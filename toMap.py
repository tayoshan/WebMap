import json
import web
db = web.database(dbn='postgres', user='postgres', pw='password', db='Artifacts')
urls = (
      '/.*', 'hello',
      )

class hello:
    def GET(self):
        web.header('Content-Type', 'application/json')
        params = web.input(toMap = [])
        #params = {"toMap": []}

        queryStartWoDist = "SELECT row_to_json(fc) FROM (SELECT 'FeatureCollection'  As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type    , ST_AsGeoJSON(lg.geom)::json As geometry    , row_to_json((SELECT l FROM (SELECT catalogid, trench, name, fabric, chronology) As l      )) As properties   FROM artifactsshp As lg WHERE "
        queryEnd = "  ) As f )  As fc"

        

        if len(params["toMap"]) > 0:
            if len(params["toMap"]) == 1:
                query = queryStartWoDist
                query = query + "artifactid = " + params["toMap"][0]
            elif params["toMap"] > 1:
                query = queryStartWoDist
                query = query + "artifactid = " + params["toMap"][0]
                for artifact in params["toMap"][1:]:
                    query = query + " OR artifactid = " + artifact
				

        query = query + queryEnd
       
        #print query

        todos = db.query(query)
        for todo in todos:
            geojson = todo['row_to_json']
            

        return json.dumps(geojson)

    
application = web.application(urls, globals()).wsgifunc()

