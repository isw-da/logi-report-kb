---
title: "Geographic Maps"
id: 1500009606302
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606302-Geographic-Maps
updated_at: 2021-07-24T16:05:15Z
---

# Geographic Maps

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629141-Maps) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629161-Inserting-Geographic-Maps-in-a-Report)

# Geographic Maps

The geographic map component is a data component integrated with Google Maps, OpenStreetMap or OpenCycleMap, which enables analyzing data geographically. Geo analysis extends traditional data analysis on static maps, where zooming and panning are common, to more dynamic methods of interacting with geographic data. Drill down the hierarchy from country to state to county. Navigate through and analyze the data using a familiar map interface.

If you have data that represents locations such as street addresses recognized by Google Maps, you can use geographic maps in your reports. You usually need to write a formula to combine items such as address, city, state and zip into one field to use for the location. You can group by multiple levels such as country, state and city as long as you use data recognized by Google Maps. OpenStreetMap and OpenCycleMap will also recognize the location if Google Maps does.

* **Google Maps**Using the Google Maps JavaScript API, three types of maps can be displayed in Logi Report: Roadmap, Satellite and Terrain. Logi Report only supports the Google Maps JavaScript API Version 3.

  Users with higher permission level can access more resources about Google Maps. For the Google Maps API documentation, it is suggested that you apply for one API key to Google Maps application. If you have one API key, you can add it directly in the configuration file mapConfiguration.xml in `<install_root>\bin` with the following format: `<property name="google.api.key">your key</property>`. If you are a business user with a client ID, you can add it in the configuration file mapConfiguration.xml with the following format: `<property name="google.api.client">your client id</property>`. Then you can access more resources about Google Maps.
* **OpenStreetMap and OpenCycleMap**Using OpenLayers JavaScript API, OpenStreetMap and two types of OpenCycleMap, Cycle Map and Transport Map, can be displayed in Logi Report.

Every geographic map component has its own data definition and can be manipulated by report developers. You can create a geographic map with a defined data source and group levels. Each group level has some markers with marker tips which show the defined tip information when you move the mouse over the markers at runtime. For geographic maps in web reports or library components, each group level can even have some areas with area tips, and each area can be shown with a polygon of distinct color.

The interactive features of geographic maps only work in Page Report Studio, Web Report Studio and JDashboard. In Logi Report Designer, you can preview geographic maps in web reports and library components as static maps and export them as static maps to Mail, HTML, PDF, Excel, RTF, PostScript and Fax.

The following topics discuss geographic maps in further detail:

* [Inserting Geographic Maps in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009629161-Inserting-Geographic-Maps-in-a-Report)
* [Modifying Geographic Maps](https://devnet.logianalytics.com/hc/en-us/articles/1500009606342-Modifying-Geographic-Maps)
* [Example: Using Geographic Map](https://devnet.logianalytics.com/hc/en-us/articles/1500009606322-Example-Using-Geographic-Map)

**Notes:**

* To use the geographic map features, you have to make sure your Logi Report Server and browser have access to the internet. If you are in an intranet, you should specify the proxy for both of them. To specify the proxy for the server, you need to open the batch file JRServer.bat in `<install_root>\bin`, and then add the following parameters in the file::
  + **http.proxyHost**: The host name of the proxy server.
  + **http.proxyPort**: The port number, the default value being 80.
  + **http.nonProxyHosts**: A list of hosts that should be reached directly, bypassing the proxy. This is a list of patterns separated by '|'. The patterns may start or end with a '\*' for wildcards. Any host matching one of these patterns will be reached through a direct connection instead of through a proxy.

  Besides HTTP protocol, HTTPS protocol is also supported by Logi Report. Loading the Maps API over HTTPS is necessary in SSL applications to avoid security warnings in most browsers, and is recommended for applications that include sensitive user data, such as a user's location, in requests.

  You can specify the required URL in the configuration file mapConfiguration.xml in `<install_root>\bin`.
* The Geographic Map feature cannot work on Internet Explorer 8.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629141-Maps) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629161-Inserting-Geographic-Maps-in-a-Report)
