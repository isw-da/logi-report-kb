---
title: "Working with Charts"
id: 5735563831831
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735563831831-Working-with-Charts
updated_at: 2022-11-02T04:12:42Z
---

# Working with Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520547607-Chart-Elements)

# Working with Charts

Chart organizes and graphically presents data in a way that makes it easy for users to see comparisons, trends, and patterns in data. It represents the report data in a visually straightforward form. This topic introduces the elements and types of the Logi Report charts, how you can create and modify charts, format the chart elements, and other chart features.

A chart is based on a chart platform. On the platform, chart paper, legend, and labels make up the normal chart. You can create a chart that contains only simple DBFields or summaries, or a complicated chart that contains DBFields, groups, summaries, and even formulas. Normally, you can represent the DBFields, summaries, and formulas in a chart using chart data markers, and use groups to produce category names and data series names. You can also use DBFields as category names.

A chart usually displays values in a static way and you cannot change the values on it once you create it. However, Logi Report provides you with options to make the chart interactive and dynamic. For example, if your data source uses data that changes quickly over time such as stock market values, you can create a real time chart, so that the chart updates itself based on a defined interval by using the real time data from the data source. You can make a chart move at runtime based on the value changes of a motion field by creating a motion chart. In a motion chart, the chart is playable. You can start or stop the chart to play the dynamic trend of the motion field, control the moving speed of the chart, and if you create a bubble motion chart, you can even use a trail control to make the chart move showing a bubble or line trail. Logi Report also supports dynamic charts in Excel, that is, you can make data in a chart map to a single cell in Excel, then when you change the data in a cell, the corresponding change also displays in the chart. In addition, you can make your chart scrollable by adding a scroll bar to the chart, which enables you to control the visible value range on the X axis of the chart. You can also select the values you are interested in to zoom them in.

The following topics discuss charts in further detail:

* [Chart Elements](https://devnet.logianalytics.com/hc/en-us/articles/5735520547607-Chart-Elements)
* [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/5735527491351-Chart-Types)
* [How Data Is Represented in a Chart](https://devnet.logianalytics.com/hc/en-us/articles/5735511926551-How-Data-Is-Represented-in-a-Chart)
* [Inserting Charts in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735512245143-Inserting-Charts-in-a-Report)
* [Modifying Charts](https://devnet.logianalytics.com/hc/en-us/articles/5735498861207-Modifying-Charts)
* [Formatting Chart Elements](https://devnet.logianalytics.com/hc/en-us/articles/5735520553751-Formatting-Chart-Elements)
* [Applying Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/5735511924119-Applying-Conditional-Color-Fills-to-Charts)
* [Labeling Time Series Data by Constant Interval](https://devnet.logianalytics.com/hc/en-us/articles/5735512266391-Labeling-Time-Series-Data-by-Constant-Interval)
* [Editing Range Groups on Chart Categories](https://devnet.logianalytics.com/hc/en-us/articles/5735520916503-Editing-Range-Groups-on-Category-Values)
* [Creating Scrollable Charts](https://devnet.logianalytics.com/hc/en-us/articles/5735498899351-Creating-Scrollable-Charts)
* [Creating Real Time Charts](https://devnet.logianalytics.com/hc/en-us/articles/5735564230679-Creating-Real-Time-Charts)
* [Creating Motion Charts](https://devnet.logianalytics.com/hc/en-us/articles/5735527456279-Creating-Motion-Charts)
* [Creating Dynamic Charts in Excel](https://devnet.logianalytics.com/hc/en-us/articles/5735511933463-Creating-Dynamic-Charts-in-Excel)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how each component type could be used in a report. For the chart component example, open `<install_root>\Demo\Reports\SampleComponents\Chart.cls`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520547607-Chart-Elements)
