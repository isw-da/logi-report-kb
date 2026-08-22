---
title: "General Introduction to Geographic Maps"
id: 28897841460109
section: "Working with Components in Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897841460109-General-Introduction-to-Geographic-Maps
updated_at: 2024-09-30T09:13:47Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
General Introduction to Geographic Maps

This topic introduces the Geographic Map component of Report in general.

You can integrate a geographic map in Report with Google Maps, OpenStreetMap, or OpenCycleMap. 

- 
Google Maps
Using the Google Maps JavaScript API, you can display three types of maps  in Report reports: Roadmap, Satellite, and Terrain. Report only supports the Google Maps JavaScript API Version 3.
    Users with higher permission level can access more resources about Google Maps. For the Google Maps API documentation, it is suggested that you apply for one API key to Google Maps application. If you have one API key, you can add it directly in the configuration file mapConfiguration.xml in <install_root>\bin with the following format: <property name="google.api.key">your key</property>. If you are a business user with a client ID, you can add it in the configuration file mapConfiguration.xml with the following format: <property name="google.api.client">your client id</property>. Then you can access more resources about Google Maps.

- 
OpenStreetMap and OpenCycleMap
Using the OpenLayers JavaScript API, you can display OpenStreetMap and two types of OpenCycleMap, Cycle Map, and Transport Map in Report reports.

Every geographic map component has its own data definition and can be manipulated by report developers. You can create a geographic map with a defined data source and group levels. Each group level has some markers with marker tips which show the specified tip information when users move the mouse over the markers at runtime. For geographic maps in web reports and library components, each group level can even have some areas with area tips, and you can display each area with a polygon of distinct color.

 In Designer, you can preview geographic maps in web reports and library components as static maps and export them as static maps to Mail, HTML, PDF, Excel, RTF, PostScript, and Fax. You can use the interactive features of geographic maps at runtime when your Server and web browser have access to the internet. If you are in an intranet, you should specify the proxy for both of them. To specify the proxy for Server, you need to open the batch file JRServer.bat in <install_root>\bin, and then add the following parameters in the file:      

- 
http.proxyHost
The host name of the proxy server.

- 
http.proxyPort
The port number, the default value being 80.

- 
http.nonProxyHosts
A list of hosts that should be reached directly, bypassing the proxy. This is a list of patterns separated by "|". The patterns may start or end with a "*" for wildcards. Report reaches any host matching one of these patterns  through a direct connection instead of through a proxy.

Besides HTTP protocol, Report also supports HTTPS protocol. Loading the Maps API over HTTPS is necessary in SSL applications to avoid security warnings in most browsers, and is recommended for applications that include sensitive user data, such as a user's location, in requests.

You can specify the required URL in the configuration file mapConfiguration.xml in <install_root>\bin.

Previous Topic  Next Topic
