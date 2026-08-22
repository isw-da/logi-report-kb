---
title: "Lesson 2: Creating a Web Report Using the Wizard"
id: 28897700147085
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897700147085-Lesson-2-Creating-a-Web-Report-Using-the-Wizard
updated_at: 2026-02-26T02:10:52Z
source_host: docs-report.zendesk.com
---
# Lesson 2: Creating a Web Report Using the Wizard

In this lesson, we create a web report using the Web Report Wizard, that is, using the traditional method. The report contains these data components: a crosstab, a table, and a banded object. After we create the report, we use the powerful analysis features of Web Report Studio to analyze data in each component. 

This lesson contains the following tasks:

- Task 1: Create a Web Report Using the Wizard

- Task 2: Work with the Crosstab

- Task 3: Work with the Chart

- Task 4: Work with the Table

- Task 5: Work with the Banded Object

- Task 6: Apply a Filter

## 
Task 1: Create a Web Report Using the Wizard

- In the Start Page of the Server Console, select My Profile in the Manage category. 

- In the My Profile > Customize Server Preferences > General tab, select Yes for Use Wizard for Web Report Studio. Select OK to save the setting.
Then in the prompt message box, select OK.

- Select Resources on the system toolbar to switch to the page, then go to the Public Reports > SampleReports  folder.

- Navigate to New > Web Report on the task bar.
    

- In the Page screen of the  Web Report Wizard dialog box, the Blank template is selected by default.  Type Sales Performance in the Label text box, then select Next. You can also select from the other two templates if you want, with which you can customize the company logo and company name.

- In the Layout screen, select the T-Style layout. In the first row, select the Select here to select component link in the left cell and select Crosstab from the drop-down menu. Select Table for the right cell and Banded Object for the bottom row.
    

- Select Next to go to the Bind Data screen to define data for the three components one by one.

- First define the crosstab: from the Data Source drop-down list, select WorldWideSalesBV in Data Source 1. Select Region in the Resources box and select Add to add it to the Columns box, then add Sales Month to the Rows box and Total Sales to the Summaries box.
    

- Select Next to define the table: keep the business view in the Data Source text box unchanged to use the same data source as the crosstab, in the Details tab,  add Product Name, Order Date, and Total as the detail fields of the table one by one, then select the Group tab and add Country as the group-by field.
    

- Select Next to define the banded object: keep the business view in the Data Source text box unchanged to use the same data source as the crosstab, in the Details tab, add these fields: Order ID, Product Name, Quantity, Unit Price, and Total, then select the Group tab and add Country as the group-by field.
    

- Select Next to display the Style screen and select LogiReportDemo as the style. 

- Select Run. The report runs in Web Report Studio. 

- Select Save on the toolbar.

- In the Save As dialog box, type SalesPerformance.wls in the File Name text box, then select OK to save the web report into the Public Reports > SampleReports folder in the server resource tree. Select OK in the message box. 

## 
Task 2: Work with the Crosstab

Using the Switch feature, we can easily change the groups on the crosstab row and column headers, so first let's change the row header to analyze data by quarter. 

- Right-click the row header and navigate to Switch Row > Sales Quarter on the shortcut menu.
    
 
    The row header now displays quarters.    

Next, we use the Go feature to analyze data from different views. Let's try Go-to-by-Value first, which enables to go to another group based on the current value. 

- Right-click 2015-Q1 in the row header, navigate to Go to by Value > Category on the shortcut menu. The crosstab refreshes to show the total sales of each product category in the first quarter of 2015 in different regions.
    

Now we use Go-Up and Go-Down to drill data in higher and lower group levels. To use these two functions, you need to make sure that the business view you use to create the report  has predefined hierarchies, so that you are able to go up and down between the group levels in the hierarchies. 

- Right-click on the row header and navigate to Go Up > Product Type on the shortcut menu.
    

The crosstab changes to：

Next, we want to go down from Product Type to Category. However, it is not simply a reversed process of going up from Category to Product Type. When you go down to a lower group level, Web Report Studio applies the currently selected value as a filter condition to show its data in the lower group level only. 

- Right-click Regular and navigate to Go Down > Category on the shortcut menu.
              The crosstab refreshes to show the total sales of the regular categories in the first quarter of 2015 in different regions.

A crosstab can be converted to a chart, and vice versa. Next, we want to use chart to display the data in the current crosstab. 

- Right-click the blank cell in the intersection of the crosstab row and column headers, then select To Chart from the shortcut menu.
    

- The To Chart dialog box lists the data fields used in the crosstab and we can define the chart based on these fields only. Keep the default chart type Clustered Bar 2-D, add Total Sales to the Bar Length box, Category to the X-Axis box, and Region to the Clustering box. 

- Select OK to generate the chart.

- Drag the bottom border of the chart to enlarge its height. The chart now shows the total sales of the Regular categories in the first quarter of 2015 in different regions.
    

- Select Save on the toolbar to save the report. 

## 
Task 3: Work with the Chart

In this task, we continue to perform on the chart that we converted from the crosstab in the previous task.

First, we want to exchange the fields on the category and series axes.

- Select Swap Chart Groups on the toolbar. The   chart refreshes to display as follows:

Then, we change the chart type to analyze data in line chart.

- Select Chart Type on the toolbar, then navigate to Line > Line 2-D on the drop-down menu.
    

From the line trend, you can easily figure out the change of the category total sales across the regions. You can also point to any line node to get the detailed data it represents in the chart.

Web Report Studio supports  linking a summary in a report to a specific detail table. Next, we use this feature to view the detailed information of each chart value.

- Right-click the highest node and select Go to Detail from the shortcut menu.
    

The detail table shows the Bold category's total sales in Europe, Middle East, Africa.

The default detail table contains all the group and detail fields in the same business view category as the aggregate field, from which you specify to create the summary of a report. In our case, the default detail table does not satisfy our requirements, so next we edit the detail table manually. 

- Select Back on the toolbar to return to the main report.

- Right-click any node in the line chart and select Edit Detail Table from the shortcut menu. 

- The Edit Detail Table dialog box lists all the group and detail fields in the business view  the chart uses. Add these fields to the right box to display in the detail table one by one: Customer Name, Discount, Quantity, Unit Price, and Total. Select OK to finish editing the detail table.
    

- Right-click the highest node again and select Go to Detail from the shortcut menu. The detail table now displays data of the fields we selected.
    

- Select Back on the toolbar to return to the main report.

- Select Save on the toolbar to save the report.

## 
Task 4: Work with the Table

We want to add some fields into the table to get more order information. We add a detail column to show order quantity and add another group to group the table by sales year first and then country.

- Select the table.

- From the Resources panel on the left, drag Quantity to the right border of the Order Date column and release the mouse button when Web Report Studio displays an orange line.
    

The table now displays as follows:

Next, we want to sort the table by the order dates in descending order. 

- Point to the Order Date column header. Web Report Studio displays the sort icon.
    

- Select the down arrow to sort the dates in descending order.
    

Now we summarize the order total in each group. 

- Right-click any value in the Total column, then select Aggregate On from the shortcut menu.

- In the Aggregate On dialog box, set the function to Sum and select OK.
    We can see the order total in each country is added in the group header.

This operation also creates a dynamic aggregation, which Web Report Studio names as Sum_Total by default. You can find it in the Dynamic Resources > Aggregations list in the Resources panel and use it in the report as you want.

Lastly, we use the Conditional Formatting feature to highlight the orders the quantity of which are equal to and larger than 1500.

- Right-click any value in the Quantity column and select Conditional Formatting from the shortcut menu.

- In the Conditional Formatting dialog box, select  Add above the Condition box.

- In the Edit Conditions dialog box, select Current Field from the field drop-down list, >= from the operator drop-down list, then in the value text box,  type 1500. Select OK to finish editing the condition and return to the Conditional Formatting dialog box.

- Select the color image ahead of the Background Color text box and select the yellow color #FFCC00 from the color palette. Select OK to apply the conditional formatting.
    

The table refreshes to display as follows:

- From the Resources panel on the left, drag Sales Year above the Australia group and release the mouse button when Web Report Studio displays an orange line.
    

The table refreshes as follows:

- Select Save on the toolbar to save the report.

## 
Task 5: Work with the Banded Object

We add a detail column to show product cost, add one more group to group the banded object by region first and then country, and add a chart in the region group. We can use the banded object template editor to perform these operations. 

- Select in the banded object, then select Edit Template on the visualization toolbar to access the template editor.
	

- Drag the detail object Cost from the Resources panel to the detail panel on the right of the Total column in the banded object.
    

Web Report Studio displays the result as follows:

- Drag Region from the Resources panel to the GH panel in the template editor and release the mouse button until Web Report Studio displays an orange line above GH.
    

Web Report Studio adds the Region group above the Country group.

Next, we insert a chart in the Region group header. We make the chart inherit data from the banded object and filter it by the region value. 

- Drag Convert or drag to add Bar from the visualization toolbar to the GH panel of the Region group.
    

- In the Insert Chart dialog box, add Total Sales to the Bar Length box and Category to the X-Axis box.
    

- Select OK to insert the chart.

- Resize the chart smaller: select in the chart to select it, then drag the bottom right corner of the chart to resize. You can also drag the chart to change its position.
    

- Select the GH panel that contains the chart to select the panel, then drag the bottom border of the panel to be closer to the chart. 
    

- Select Return on the visualization toolbar to exit the template editor. The banded object looks as follows:

Next, we switch from the Region group to Sales Year to see how the chart responds to the change of the group value. 

- Right-click Asia-Pacific and navigate to Switch Group > Sales Year on the shortcut menu.
    

The banded object now shows as follows:

## 
Task 6: Apply a Filter

In Web Report Studio, you can apply a filter to each data component in a report individually, or use the Filter panel and filter controls to filter multiple data components at a time. For the usage of filter controls, you can learn from Creating Web Reports in the Advanced Part. Here we focus on using the Filter panel to filter report data.

- Select Add on the title bar of the Filter panel on the left. Web Report Studio displays the Select Field dialog box.

- Select Country and Region, keep the default Apply To setting, then select OK.
    

Web Report Studio adds a filter box which contains all values of the selected fields in the Filter panel, and labels the box by the name of the first selected field in the Select Fields dialog box.

- Select North America  in the value list. The report comes out as follows:

At the meantime, Web Report Studio processes values in the filter box to put the countries in the selected region on the top of the value list. You can select a country in the region or other value to go on filtering the report.

- Select Mexico. Web Report Studio filters the report to show the following data:
    

- Select Clear in the Filter panel to remove all filters applied to the report via the panel.

- Select Save on the toolbar to save the report.
