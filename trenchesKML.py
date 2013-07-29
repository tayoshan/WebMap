import web
import urllib
urls = (
      '/.*', 'hello',
      )

class hello:
    def POST(self):
        web.header('Content-Type', 'text/html')
        web.header('Content-disposition', 'attachment; filename=trenchesKML.kml')
        kml = web.input()
       
        kml = urllib.unquote(kml["jsondata"])
        return kml
        
    
application = web.application(urls, globals()).wsgifunc()
