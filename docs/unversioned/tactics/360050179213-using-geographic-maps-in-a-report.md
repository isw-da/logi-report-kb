---
title: "Using Geographic Maps in a Report"
id: 360050179213
section: "Tactics"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050179213-Using-Geographic-Maps-in-a-Report
updated_at: 2022-10-31T15:04:55Z
---

# Using Geographic Maps in a Report

Logi Report provides geographic visualization and analysis by overlaying customized areas and markers onto interactive maps in Google Maps, OpenStreetMap and OpenCycleMap. Logi Report also supports Google Maps JavaScript API Version 3. Three types of maps can be displayed in Logi Report: Roadmap, Satellite, and Terrain. Conditional properties such as shape, size, color and label can be adjusted to provide an understanding of the data at a quick glance. Geo Analysis extends traditional data analysis on static maps, where zooming and panning are common, to more dynamic methods of interacting with geographic data. Analyze data using a familiar map interface and drill down hierarchies containing countries, states, counties and cities. This works in Page Report Studio, Web Report Studio as well as JDashboard.

## How to create a map for my report?

We will insert a geographic map in a web report as an example to show the basic procedure:

1. Drag the Geographic Map button ![Geographic Map button](https://devnet.logianalytics.com/hc/article_attachments/9905598996119) from the Visual category of the Components pane to the blank area in the web report.
2. The Create Geographic Map wizard appears. In the Data screen of the wizard, select a business view in the current catalog on which the geographic map will be created. Then click **Next**.
3. In the Display screen, add the group objects Region and then Country from the Resources box to the Drill Path box as the grouping criteria. Use the right arrow button ![Right Arrow button](https://devnet.logianalytics.com/hc/article_attachments/9905589982231) to add them one by one.
4. Click **Finish** to insert the geographic map.

![Create a Map](https://devnet.logianalytics.com/hc/article_attachments/9905590187799)

## How to create a map with dynamic tips (controlled by formula)?

We will create a geographic map in a library component and use three formulas to show advanced customization of the map.

* MarkerTipforCountry

“Country:” + ” ” + @”Customers.Country” + “\n” +  
“Total Cost:” + ” ” + ToText(@”Orders Detail.Total Cost”,”$#,###.00″) + “\n” +  
“Total Sales:” + ” ” + ToText(@”Orders Detail.Total Sales”,”$#,###.00″)

* AreaTipforState

“Country:” + ” ” + @”Customers.Country” + “\n” +  
“State:” + ” ” + @”Customers.State” + “\n” +  
“Total Sales:” + ” ” + ToText(@”Orders Detail.Total Sales”,”$#,###.00″)

* LocationInfoforState

@”Customers.State” + “,” + @”Customers.Country”

![Geo Analysis](https://devnet.logianalytics.com/hc/article_attachments/9905598678295)

## How to perform interactions on a map?

After the library component created above is published to Logi Report Server, we can then add it to a dashboard to perform geo analysis on the map.

![Perform Geo Analysis on Map](https://devnet.logianalytics.com/hc/article_attachments/9905589852951)

## Advanced Geographic Maps Using Page Reports and Google Maps

Using the Google Maps JavaScript API, three types of maps can be displayed in Logi Report: Roadmap, Satellite and Terrain. Logi Report only supports the Google Maps JavaScript API Version 3.

A geographic map integrated with Google Maps in a page report can be viewed in the Logi Report Designer view mode. Its interactive features can work in Page Report Studio. Moreover, static Google Maps images are supported in PDF and HTML formats with some limitations (for details, refer to [Google Static Maps API](https://developers.google.com/maps/documentation/staticmaps/)).

In the following example, we create a geographic map integrated with Google Maps, view it in the Logi Report Designer view mode, run it in Page Report Studio and export it to PDF format.

![Advanced Geographic Maps using Page Reports](https://devnet.logianalytics.com/hc/article_attachments/9906091459351)
