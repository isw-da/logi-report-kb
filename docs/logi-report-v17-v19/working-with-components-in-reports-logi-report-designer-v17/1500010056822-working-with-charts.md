---
title: "Working with Charts"
id: 1500010056822
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056822-Working-with-Charts
updated_at: 2021-07-23T19:14:36Z
---

# Working with Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094381-Chart-Elements)

# Working with Charts

Chart organizes and graphically presents data in a way that makes it easy for the report users to see comparisons, trends, and patterns in data. It represents the report data in a visually straightforward form. This topic introduces the elements and types of the Logi Report charts, how you can create and modify charts, format the chart elements, as well as other chart features.

A chart is based on a chart platform. On the platform, chart paper, legend, and labels make up the normal chart. You can create a chart that contains only simple DBFields or summaries, or a complicated chart that contains DBFields, groups, summaries, and even formulas. Normally, you can represent the DBFields, summaries, and formulas in a chart using chart data markers, and use groups to produce category names and data series names. You can also use DBFields as category names.

A chart usually displays values in a static way and you cannot change the values on it once you create it. However, Logi Report provides you with options to make the chart interactive and dynamic. For example, if your data source uses data that changes quickly over time such as stock market values, you can create a real time chart, so that the chart updates itself based on a defined interval by using the real time data from the data source. You can make a chart move at runtime based on the value changes of a motion field by creating a motion chart. In a motion chart, the chart is playable. You can start or stop the chart to play the dynamic trend of the motion field, control the moving speed of the chart, and if you create a bubble motion chart, you can even use a trail control to make the chart move showing a bubble or line trail. Logi Report also supports dynamic charts in Excel, that is, you can make data in a chart map to a single cell in Excel, then when you change the data in a cell, the corresponding change also displays in the chart. In addition, you can make your chart scrollable by adding a scrollbar to the chart, which enables you to control the visible value range on the X axis of the chart. You can also use the mouse pointer to select the values you are interested in to have the values zoom in.

The following topics discuss charts in further detail:

* [Chart Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500010094381-Chart-Elements)
* [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500010094681-Chart-Types)
* [How Data Is Represented in a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010056842-How-Data-Is-Represented-in-a-Chart)
* [Inserting Charts in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report)
* [Modifying Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010094661-Modifying-Charts)
* [Formatting Chart Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500010094401-Formatting-Chart-Elements)
* [Applying Conditional Color Fills to Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010094361-Applying-Conditional-Color-Fills-to-Charts)
* [Labeling Time Series Data by Constant Interval](https://devnet.logianalytics.com/hc/en-us/articles/1500010057062-Labeling-Time-Series-Data-by-Constant-Interval)
* [Editing Range Groups on Category Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010057102-Editing-Range-Groups-on-Category-Values)
* [Creating Scrollable Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010057142-Creating-Scrollable-Charts)
* [Creating Real Time Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010057122-Creating-Real-Time-Charts)
* [Creating Motion Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010057082-Creating-Motion-Charts)
* [Creating Dynamic Charts in Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500010056862-Creating-Dynamic-Charts-in-Excel)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how each component type could be used in a report. For the chart component example, open `<install_root>\Demo\Reports\SampleComponents\Chart.cls`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094381-Chart-Elements)
