---
title: "Geographic Maps"
id: 1500009563462
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563462-Geographic-Maps
updated_at: 2021-07-24T05:56:00Z
---

# Geographic Maps

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563562-Controlling-Labels-and-Summary-Fields-on-Shape-Map-Areas)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584101-Inserting-a-Geographic-Map)

# Geographic Maps

The geographic map component is a data component integrated with Google Maps, OpenStreetMap or OpenCycleMap, which enables analyzing data geographically. Geo Analysis extends traditional data analysis on static maps, where zooming and panning are common, to more dynamic methods of interacting with geographic data. Drill down the hierarchy from country to state to county. Navigate through and analyze the data using a familiar map interface.

If you have data that represents locations such as street addresses recognized by Google Maps, you can use geographic maps in your reports. You usually need to write a formula to combine items such as address, city, state and zip into one field to use for the location. You can group by multiple levels such as country, state and city as long as you use data recognized by Google Maps. OpenStreetMap and OpenCycleMap will also recognize the location if Google Maps does.

* **Google Maps**Using the Google Maps Javascript API, three types of maps can be displayed in Logi JReport: roadmap, satellite and terrain. Logi JReport only supports the Google Maps Javascript API Version 3.

  Users with higher permission level can access more resources about Google Maps. For Google Maps API documentation, it is suggested that you apply for one API key to Google Maps application. If you have one API key, you can add it directly in the configuration file mapConfiguration.xml in `<install_root>\bin` with the following format: `<property name="google.api.key">your key</property>`. If you are a business user with a client ID, you can add it in the configuration file mapConfiguration.xml with the following format: `<property name="google.api.client">your client id</property>`. Then you can access more resources about Google Maps.

  The interactive features of Google maps only work in Page Report Studio, Web Report Studio and JDashboard; however, static Google map images are supported in PDF and HTML formats with some limitations (for details, refer to [Google Static Maps API](https://developers.google.com/maps/documentation/staticmaps/)).
* **OpenStreetMap and OpenCycleMap**Using OpenLayers Javascript API, OpenStreetMap and two types of OpenCycleMap, namely, Cycle Map and Transport Map, can be displayed in Logi JReport.

  OpenStreetMap and OpenCycleMap cannot be displayed in the Designer View mode or be exported or printed in Logi JReport Designer as the Static Maps API is not supported at present. Their interactive features only work in Page Report Studio, Web Report Studio and JDashboard.

Every geographic map component has its own data definition and can be manipulated by report developers. You can create a geographic map with a defined data source and group levels. Each group level has some markers with marker tips which show the defined tip information when you move the mouse over the markers at runtime. For geographic maps in web reports or library components, each group level can even have some areas with area tips, and each area can be shown with a polygon of distinct color.

Pick a task from the following:

> * [Inserting a Geographic Map](https://devnet.logianalytics.com/hc/en-us/articles/1500009584101-Inserting-a-Geographic-Map)
> * [Adding Conditional Formats to Geographic Map Markers](https://devnet.logianalytics.com/hc/en-us/articles/1500009584081-Adding-Conditional-Formats-to-Geographic-Map-Markers)
> * [Example of Using Geographic Map](https://devnet.logianalytics.com/hc/en-us/articles/1500009563482-Example-of-Using-Geographic-Map)

**Notes:**

* To use the geographic map features, you have to make sure your Logi JReport Server and browser have access to the internet. If you are in an intranet, you should specify the proxy for both of them. To specify the proxy for the server, you need to open the batch file JRServer.bat in `<install_root>\bin`, and then add the following parameters in the file::
  + **http.proxyHost**: The host name of the proxy server.
  + **http.proxyPort**: The port number, the default value being 80.
  + **http.nonProxyHosts**: A list of hosts that should be reached directly, bypassing the proxy. This is a list of patterns separated by '|'. The patterns may start or end with a '\*' for wildcards. Any host matching one of these patterns will be reached through a direct connection instead of through a proxy.

  Besides HTTP protocol, HTTPS protocol is also supported by Logi JReport. Loading the Maps API over HTTPS is necessary in SSL applications to avoid security warnings in most browsers, and is recommended for applications that include sensitive user data, such as a user's location, in requests.

  You can specify the required URL in the configuration file mapConfiguration.xml in `<install_root>\bin`.
* The Geographic Map feature cannot work on Internet Explorer 8.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563562-Controlling-Labels-and-Summary-Fields-on-Shape-Map-Areas)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584101-Inserting-a-Geographic-Map)
