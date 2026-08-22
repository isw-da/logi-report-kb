---
title: "Creating Real Time Charts"
id: 12479956403853
section: "Working with Components in Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12479956403853-Creating-Real-Time-Charts
updated_at: 2026-02-25T23:50:31Z
source_host: docs-report.zendesk.com
---
# Creating Real Time Charts

This topic introduces the characteristics of real time charts and how you can create a real time chart.

This topic contains the following sections:

- What Are Real Time Charts?

- Creating a Real Time Chart

## 
What Are Real Time Charts?

A real time chart can update automatically at runtime by using data that changes rapidly with time such as stock market quotes. When the data in the data source that a real time chart applies is updated in real time, the chart automatically fetches data from the data source to update itself with the specified interval. Users can then conveniently see the real time data information without updating the chart by themselves and without having to refetch all of the data. Report only selects the new data since the last interval from the data source.

Before you create a real time chart, you have to make sure the data source you use contains real time data which can be updated periodically; otherwise, the chart loses its real time functionality. 

Real time charts can only be of the Bar, Bench, Line, and Area types, and you can use them in web reports and library components only.

## 
Creating a Real Time Chart

- Position the mouse pointer at the destination in the web report or a library component where you want to insert the chart. 

- Do either of the following:
    
- From the Components panel, drag a chart icon in the Visual category  to the destination.

- Navigate to Insert > Chart or Home > Insert > Chart.

Designer displays the Create Chart dialog box.

- In the Data screen, specify the dataset you want to use to create the
     chart. 

- In the Type screen, specify the type of the chart which can only be single chart of the Bar, Bench, Line, or Area type.
    

- In the Display screen, specify a title for the chart in the Title text box. Select Real Time.
    

- By default, Designer selects Use System Time for Category and you can see the text Use System Refresh Time in the Category box, which means Designer usea the time at which the chart refreshes itself as the category value. You can clear Use System Time for Category and choose a group object  or detail object  in the specified business view, or a dynamic formula used as Group  or dynamic formula used as Detail   that you have created for the business view in the current report to display on the category axis, and define the Order/Select N condition on it.

- In the Show Values box, add the group objects and detail objects that are Numeric data type to display on the value axis.    You can only use Numeric group objects and details objects on the value axis of a real time chart. If you add objects of other data types to the Show Values box, Designer automatically clears the Real Time checkbox.

- Specify the time interval at which the chart gets data and refreshes itself automatically in the Refresh Interval text box.

- Specify the most recent N records you want to keep for the real time data  in the Show Most Recent text box.

- Select Incremental Fetch to add the fields as the unique key of the real time chart in the Unique Key dialog box, which guarantees there are no two records with the same unique key value in the chart. Once you define a unique key, each time when the chart automatically updates itself at runtime, Report Engine filters the data that has the same unique key value as the previously loaded records and only adds data with different unique key value to the chart. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when a record with the product ID 1 in USA has already been loaded into the chart, Report Engine adds no more records of this product ID in USA to the real time chart because they have the same unique key value. The most common usage is with a time field, so that when a time is part of the unique key, you can find the chart updated each time new records are added to the database with more recent times.    

- In the Dataset Filter screen, filter the dataset the chart applies. If you have added filter conditions to the dataset somewhere else, Designer displays the conditions in the screen. You can further edit the conditions. Be aware that a filter on a dataset applies to all data components in the same report that use this dataset.  

- In the Layout screen, specify the layout of the chart.
    

- In the Style screen, select a style for the chart.
    

- Select Finish to create the chart.
