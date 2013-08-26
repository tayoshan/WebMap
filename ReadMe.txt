-Code 4 and 5 currently house the web service scripts that perform the database query to PostGIS and return the results in GeoJSON format

-httpd file is the config file for apache web server. I have backed it up here since it has the necessary lines of code (at the bottom) that enable WSGI_mod for python back end scripting and links to the necessary files for this application

-autoMap.html is the latest web application file. It has been enables to accept a comma separated list of artifactID's (ex. 19660043) in the url (ex. http://poggiocivitate.classics.umass.edu:8081/app/autoMap.html?19660043,20100001,20080001) and will automatically add those features to the map. This feature is mainly so that the web mapping application can be linked into the original database interface.

-files frefixed with trenches or artifacts provides scripts to package the data seelcted within a users browsers into different formats and then returns the file for download in their browser