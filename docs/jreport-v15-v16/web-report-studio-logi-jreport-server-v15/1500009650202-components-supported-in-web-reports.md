---
title: "Components Supported in Web Reports"
id: 1500009650202
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650202-Components-Supported-in-Web-Reports
updated_at: 2021-07-24T20:53:37Z
---

# Components Supported in Web Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675401-Why-Web-Reports-and-When-to-Choose-Them)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675121-An-Introduction-to-Business-Views)

# Components Supported in Web Reports

Components are the objects that you can place in a report. Logi JReport provides a full set of components that allow you to present and control the report data and presentation in a wide variety of ways.

Web reports support the following report components:

* **Labels**  
   A label is an object that contains a string. It is typically a brief description used to identify a field or other value nearby.
* **Images**  
   An image is a digital representation of a picture. The following image types are supported in web reports: .gif, .jpg, and .png.
* **DBFields**   
   DBFields, or database fields, are fields directly from columns in the database or other data source such as XML or Java objects.
* **Formulas**  
   Formulas are calculated from DBFields, other formulas, summaries, and parameters, so they can present information which is not available directly from the database fields.
* **Summaries**  
   A summary is a special kind of formula. A summary generates a count, average, sum, standard deviation or other transformation of a set of data values. A summary applies to a defined group of data. Summaries are required to provide the data values for charts as well as totals for table reports.
* **Parameters**  
   A parameter in Logi JReport is a variable whose value is determined at runtime. The runtime parameters help you dynamically control your report result such as filtering data.
* **Special fields**  
   Special fields are defined by Logi JReport and allow you to easily obtain system information and report-related data and add it to your report. All special fields are supported to insert into web reports in Logi JReport Designer. However, due to the characteristics of Web Report Studio, only these can be rendered and edited in Web Report Studio: User Name, Modified Date, Modified Time, Fetch Date, Fetch Time, Print Date, and Print Time. For more, see "Special Fields" in the *Logi JReport Designer User's Guide*.
* **Web controls**   
   Web controls are report components designed to be similar to the kinds of controls found on web pages. Currently, the following four web controls are supported in web reports: parameter control, parameter form control, filter control, and navigation control.
* **Multimedia objects**  
   Multimedia objects include Flash, Real Media, and Windows Media objects.
* **Tabular**  
  A tabular is a component designed to lay out other components. There is one and only one tabular in a web report.
* **Geographic maps** A geographic map is a data component that is integrated with Google Maps, OpenStreetMap or OpenCycleMap, which enables analyzing data geographically. Geo Analysis extends traditional data analysis on static maps, where zooming and panning are common, to more dynamic methods of interacting with geographic data. Drill down the hierarchy from country to state to county. Navigate through and analyze the data using a familiar map interface.
* **KPI components**  
   A KPI (Key Performance Indicator) component is a data container used for displaying KPI value together with a chart to help illustrate the value. In a KPI component the following objects can be added:
  + Aggregations and formulas as the KPI values.
  + Labels to describe the values and as the KPI title or description.
  + Images to decorate the KPI component or used as logo.
  + A KPI chart to assist the KPI values, for example, to show the trend of total sales over time. At most one KPI chart can be included in a KPI component. A KPI chart does not have the legend and axes compared to normal Logi JReport charts. It can only be inserted in a KPI component and inherit dataset from the KPI component. The following 2-D chart types are supported in KPI charts: Bar, Bench, Line, Area, Pie, and Bullet.

  A KPI component is bound with a business view so the KPI value and KPI chart in it are both based on this business view. The objects in a KPI component can be freely positioned and resized by dragging inside the KPI component.
* **Tables**  
   A table gives you great control over how to present data, including placing fields, grouping them, and sorting them. It is composed of rows and columns, and each contains several cells. With such a structure a table is a good way to show any two-dimensional dataset.
* **Crosstabs**  
   A crosstab summarizes data and presents the summaries in a compact row and column format.
* **2-D Charts**  
   A chart organizes and graphically presents data in a way that makes it easy for end users to see comparisons, trends, and patterns in data. It represents the report data in a visually straightforward form. A chart is based on the chart platform. On the platform, the chart paper, the legend, and labels make up the chart. You can create a chart that contains only simple DBFields or summaries, or a complicated chart that contains DBFields, groups, summaries, and even formulas. Normally, DBFields, summaries, and formulas in a report are represented in a chart using chart data markers, and groups are used to produce category names and data series names. DBFields can also be used as category names.

  The following table lists the chart types supported in Web Report Studio.

  |  |  |  |
  | --- | --- | --- |
  | Bar | | |
  |  | Clustered Bar 2-D | Clustered Bar. Displays and compares data values across categories. |
  |  | Stacked Bar 2-D | Stacked Bar. Displays and compares the contribution of each data value to a total across categories. |
  |  | 100% Stacked Bar 2-D | 100% Stacked Bar. Displays and compares the percentage that each data value contributes to a total across categories. |
  | **Bench** | | |
  |  | Clustered Bench 2-D | Clustered Bench. Displays and compares data values across categories. |
  |  | Stacked Bench 2-D | Stacked Bench. Displays and compares the contribution of each data value to a total across categories. |
  |  | 100% Stacked Bench 2-D | 100% Stacked Bench. Displays and compares the percentage that each data value contributes to a total across categories. |
  | Line | | |
  |  | Line 2-D | Line. Displays trend over categories. |
  |  | Stacked Line 2-D | Stacked Line. Displays the trend of the contribution of each data value over categories. |
  |  | 100% Stacked Line 2-D | 100% Stacked Line. Displays the trend of the percentage each data value contributes over categories. |
  | Area | | |
  |  | Area 2-D | Displays the trend of the values over time or categories. |
  |  | Stacked Area 2-D | Stacked Area. Displays the trend of the contribution of each data value over categories. |
  |  | 100% Stacked Area 2-D | 100% Stacked Area. Displays the trend of the percentage each data value contributes over categories. |
  | Pie | | |
  |  | Clustered Pie | Pie. Displays the contribution of each data value to a total over time or categories. |
  |  | Clustered Donut | Donut. Displays the contribution of each data value to the Category total. The size of each piece is proportional to the sum of the items. Each Series value will create a new instance of the chart. |
  | Organization (Org) | | |
  |  | Org 2-D | Displays the structure of an organization and the relationships and relative ranks of its parts, or the similar structures. |
  | Indicator | | |
  |  | Indicator 2-D | Displays each data value with a colored indicator. |
  | Gauge | | |
  |  | Gauge Dial 2-D | Usually displays the performance of each member in a group, using three colors, green, yellow, and red (by default) to represent three levels: normal, alert, and error. This type, displays each data value by a dial. |
  |  | Gauge Bar 2-D | Displays each data value with a bar. |
  |  | Gauge Bubble 2-D | Displays each data value with a colored bubble. |
  | Bubble | | |
  |  | Bubble 2-D | Compares sets of 3 values. Similar to a scatter chart with the third value displayed as the size of the bubble marker. |
  | Bullet | | |
  |  | Bullet 2-D | Bullet. Replaces the meters and gauges that are often used on dashboards. Its linear design not only gives it a small footprint, but also supports more efficient reading than radial meters. |
  | Heat Map | | |
  |  | Heat Map | Displays values by colors and sizes in a matrix. |
  | Combo | | |
  |  | Combo | Combination of bar and line charts. |
  |  | Combo | Combination of are and line charts. |

  For how charts present data, see "How Data Is Represented in a Chart" in the *Logi JReport Designer User's Guide*.

  For the elements that compose a chart, see "Chart Elements" in the *Logi JReport Designer User's Guide*.

**Tip:** In Logi JReport, the components that can be bound with a data source are also referred to as data components. These components include tables, crosstabs, charts, KPI components, and geographical maps.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675401-Why-Web-Reports-and-When-to-Choose-Them)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675121-An-Introduction-to-Business-Views)
