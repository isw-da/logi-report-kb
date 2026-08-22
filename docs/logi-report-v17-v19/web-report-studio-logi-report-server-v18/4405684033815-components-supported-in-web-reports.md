---
title: "Components Supported in Web Reports"
id: 4405684033815
section: "Web Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405684033815-Components-Supported-in-Web-Reports
updated_at: 2022-01-27T07:59:51Z
---

# Components Supported in Web Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690692503-Major-Benefits-of-Web-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684032791-An-Introduction-to-Business-Views)

# Components Supported in Web Reports

Logi Report provides a full set of components for you to present and control the report data and presentation in a wide variety of ways. This topic describes the components that you can add in web reports.

In Logi Report, you can bind tables, crosstabs, charts, banded objects, KPIs, and geographical maps with a data source. Those components are also data components.

Web reports support the following report components:

* **Label**  
   A label is an object that contains a string. It is typically a brief description to identify a field or other value nearby.
* **Image**  
   An image is a digital representation of a picture. You can use the following image types in web reports: GIF, JPG, and PNG.
* **DBField**  
   DBFields, or database fields, are fields directly from columns in the database or other data sources such as XML or Java objects.
* **Formula**  
  Logi Report calculates formulas from DBFields, summaries, parameters, and other formulas, so formulas can present information which is not available directly from database fields.
* **Summary**  
   A summary is a special kind of formula. A summary generates a count, average, sum, standard deviation, or other transformation of a set of data values. A summary applies to a group of data or to the entire business view.
* **Parameter**  
  A parameter in Logi Report is a variable whose value is determined at runtime. Runtime parameters help you dynamically control your report data such as filtering data.
* **Special Field**  
  Logi Report defines special fields for you to easily obtain system information and report-related data and add it to your report. You can use the following special fields in your reports in Web Report Studio: Modified Date, Modified Time, Print Date, Print Time, Fetch Date, Fetch Time, Record Number, Total Records, Group Number, Total Group Number, User Name, Report Path on Server, Report Path on Disk, Catalog Path on Server, Catalog Path on Disk, Query Filter, Filter, On-screen Filter, and Go To Filter.

  For more information, see Special Fields in the *Logi Report Designer Guide*.
* **Web Control**  
  Web controls are report components similar to the controls you see on web pages. You can use the following four web controls in web reports: parameter control, parameter form control, filter control, and navigation control.
* **Multimedia Object**  
  Multimedia objects include RealMedia and Windows Media objects, which you also call OLE Objects.
* **Line Object**  
  You can add horizontal and vertical lines to banded objects in Web Report Studio.
* **Page Break**  
  A page break creates a page mark to separate components in the report body and place the components that follow the page break in a new page in the report output that supports page layout such as PDF and RTF.
* **Tabular**  
  A tabular is a component designed to lay out other components. A web report can contain at most one tabular.
* **Geographic Map**  
  A geographic map is a data component that is integrated with Google Maps, OpenStreetMap, or OpenCycleMap, which enables analyzing data geographically. Geo Analysis extends traditional data analysis on static maps, where zooming and panning are common, to more dynamic methods of interacting with geographic data. Drill down the hierarchy from country to state to county. Navigate through and analyze the data using a familiar map interface.
* **KPI**  
  KPIs (Key Performance Indicators) help manage business performance. A KPI in Logi Report is a data container that displays KPI value together with a chart to help illustrate the value. You can add the following objects in a KPI:
  + Aggregations and formulas as the KPI values.
  + Labels to describe the values and as the KPI title or description.
  + Images to decorate the KPI or used as logo.
  + A KPI chart to assist the KPI values, for example, to show the trend of total sales over time. You can include at most one KPI chart in a KPI. A KPI chart does not have the legend and axes compared to normal Logi Report charts. You can only insert it in a KPI and use the same business view as the KPI. You can use the following 2D chart types in KPI charts: Bar, Bench, Line, Area, Pie, and Bullet.

  A KPI is bound with a business view so the KPI value and KPI chart in it are both based on the business view. You can freely position and resize the objects in a KPI by dragging them inside the KPI.
* **Table**  
  A table gives you great control over how to present data, including placing, grouping, and sorting fields.
* **Crosstab**  
  A crosstab summarizes data and presents the summaries in a compact row and column format.
* **Banded Object**  
  A banded object is a type of component that presents grouped data and detail data. A banded object is composed of several banded panels in which you can easily organize data fields and other components with absolute layout for precise design.
* **2D Chart**  
  A chart organizes and graphically presents data in a way that makes it easy for you to see comparisons, trends, and patterns in data. It represents the report data in a visually straightforward form. A chart is based on the chart platform. On the platform, the chart paper, the legend, and labels make up the chart. You can create a chart that contains only simple DBFields or summaries, or a complicated chart that contains DBFields, groups, summaries, and even formulas. Normally, Logi Report displays DBFields, summaries, and formulas in a chart using chart data markers, and uses groups to produce category names and data series names. You can also use DBFields as category names.

  The following table lists the chart types Web Report Studio supports.

  |  |  |  |
  | --- | --- | --- |
  | Bar | | |
  | Clustered Bar 2-D | Clustered Bar 2-D | Clustered Bar displays and compares data values across categories. |
  | Stacked Bar 2-D | Stacked Bar 2-D | Stacked Bar displays and compares the contribution of each data value to a total across categories. |
  | 100% Stacked Bar 2-D | 100% Stacked Bar 2-D | 100% Stacked Bar displays and compares the percentage that each data value contributes to a total across categories. |
  | Bench | | |
  | Clustered Bench 2-D | Clustered Bench 2-D | Clustered Bench displays and compares data values across categories. |
  | Stacked Bench 2-D | Stacked Bench 2-D | Stacked Bench displays and compares the contribution of each data value to a total across categories. |
  | 100% Stacked Bench 2-D | 100% Stacked Bench 2-D | 100% Stacked Bench displays and compares the percentage that each data value contributes to a total across categories. |
  | Line | | |
  | Line 2-D | Line 2-D | Line displays trend over categories. |
  | Stacked Line 2-D | Stacked Line 2-D | Stacked Line displays the trend of the contribution of each data value over categories. |
  | 100% Stacked Line 2-D | 100% Stacked Line 2-D | 100% Stacked Line displays the trend of the percentage each data value contributes over categories. |
  | Area | | |
  | Area 2-D | Area 2-D | Area displays the trend of the values over time or categories. |
  | Stacked Area 2-D | Stacked Area 2-D | Stacked Area displays the trend of the contribution of each data value over categories. |
  | 100% Stacked Area 2-D | 100% Stacked Area 2-D | 100% Stacked Area displays the trend of the percentage each data value contributes over categories. |
  | Pie | | |
  | Clustered Pie | Clustered Pie | Pie displays the contribution of each data value to a total over time or categories. |
  | Clustered Donut | Clustered Donut | Donut displays the contribution of each data value to the Category total. The size of each piece is proportional to the sum of the items. Each Series value creates a new instance of the chart. |
  | Organization (Org) | | |
  | Org 2-D | Org 2-D | It displays the structure of an organization and the relationships and relative ranks of its parts, or the similar structures. |
  | Indicator | | |
  | Indicator 2-D | Indicator 2-D | It displays each data value with a colored indicator. |
  | Gauge | | |
  | Gauge Solid 2-D | Gauge Solid 2-D | It displays each data value with an arc. |
  | Gauge Dial 2-D | Gauge Dial 2-D | It usually displays the performance of each member in a group, using three colors, green, yellow, and red (by default) to represent three levels: normal, alert, and error. This type displays each data value by a dial. |
  | Gauge Activity 2-D | Gauge Activity 2-D | It displays each data value with a circle (and pointer). |
  | Gauge Bar 2-D | Gauge Bar 2-D | It displays each data value with a bar. |
  | Gauge Bubble 2-D | Gauge Bubble 2-D | It displays each data value with a colored bubble. |
  | Bubble | | |
  | Bubble 2-D | Bubble 2-D | It compares sets of three values. It is similar to a scatter chart with the third value displayed as the size of the bubble marker. |
  | Bullet | | |
  | Bullet 2-D | Bullet 2-D | It replaces the meters and gauges that are often used on dashboards. Its linear design not only gives it a small footprint, but also supports more efficient reading than radial meters. |
  | Heat Map | | |
  | Heat Map | Heat Map | It displays values by colors and sizes in a matrix. |
  | Combo | | |
  | Combo | Combo | Combination of bar and line charts. |
  | Combo | Combo | Combination of area and line charts. |

  For more information, see How Data Is Represented in a Chart and Chart Elements in the *Logi Report Designer Guide*.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690692503-Major-Benefits-of-Web-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684032791-An-Introduction-to-Business-Views)
