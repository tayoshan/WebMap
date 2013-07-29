import json
import web
db = web.database(dbn='postgres', user='postgres', pw='password', db='Artifacts')
urls = (
      '/.*', 'hello',
      )

class hello:
    def GET(self):
        web.header('Content-Type', 'application/json')
        params = web.input(mappedArts = [], mappedTrenches = [])
        #params = {"name":"bronze", "trench":"", "catalogid": "20110069", "dist":"100", "distFeature": "Orientalizing Architecture"}

        differentiate = 0
        queryStartWoDist = "SELECT row_to_json(fc) FROM (SELECT 'FeatureCollection'  As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type    , ST_AsGeoJSON(lg.geom)::json As geometry    , row_to_json((SELECT l FROM (SELECT catalogid, trench, name, fabric, chronology) As l      )) As properties   FROM artifactsshp As lg WHERE "
        queryStartWDist = "SELECT row_to_json(fc) FROM (SELECT 'FeatureCollection'  As type, array_to_json(array_agg(f)) As features FROM (SELECT 'Feature' As type    , ST_AsGeoJSON(lg.geom)::json As geometry    , row_to_json((SELECT l FROM (SELECT catalogid, trench, name, fabric, chronology) As l      )) As properties   FROM artifactsshp As lg, "  
        queryEnd = "  ) As f )  As fc"

        

        if len(params["distFeature"]) > 0 and params['distFeature'] != "None":
            if params["distFeature"] == "Mapped Artifacts":
                query = queryStartWDist + "(Select ST_Collect(geom) as test from artifactsshp where catalogid = " + "'" + params["mappedArts"][0] + "'"
                for each in params["mappedArts"][1:]:
                    query = query + " or catalogid = " + "'" + each + "'"
                query = query + ") As oc WHERE St_Distance(lg.geom::geography, oc.test::geography) < " + params["dist"]  
                differentiate += 1
            elif params["distFeature"] == "Mapped Trenches":
                query = queryStartWDist + "(Select ST_Collect(geom) as test from trenchpolygonsllatt where trench = " + "'" + params["mappedTrenches"][0] + "'"
                for each in params["mappedTrenches"][1:]:
                    query = query + " or trench = " + "'" + each + "'"
                query = query + ") As oc WHERE St_Distance(lg.geom::geography, oc.test::geography) < " + params["dist"]  
                differentiate += 1
            else:
                query = queryStartWDist + '"' + params["distFeature"] + '"' + " As oc WHERE St_Distance(lg.geom::geography, oc.geom::geography) < " + params["dist"]
                differentiate += 1

        else:
            query = queryStartWoDist

        counter = 0
        for param in params:
            if param == "name" or param == "trench" or param == "catalogid":
                if len(params[param]) > 0 and differentiate == 0:
                    query = query + param + " ILIKE " + "'%" + params[param] + "%'"
                    #print query
                    differentiate += 1
                elif len(params[param]) > 0:
                    query = query + " AND " + param +" ILIKE " + "'%" + params[param] + "%'"
                    #print query
                counter += 1

        query = query + queryEnd
        print queryEnd
        #print query

        todos = db.query(query)
        for todo in todos:
            geojson = todo['row_to_json']
            

        return json.dumps(geojson)

    
application = web.application(urls, globals()).wsgifunc()

