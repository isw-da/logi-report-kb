---
title: "Lesson 3: Creating and Performing Data Analysis on Page Reports"
id: 45190377472525
section: "Report Tutorial"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190377472525-Lesson-3-Creating-and-Performing-Data-Analysis-on-Page-Reports
updated_at: 2026-04-30T15:10:13Z
source_host: logi-report-v26.insightsoftware.com
---
# Lesson 3: Creating and Performing Data Analysis on Page Reports

Using the Page Report Wizard, you can create a single component page report that you view in Page Report Studio. Page Report Studio provides the user a page mode view of the report very similar to a printed report.

The Page Report Wizard provides several report layouts to collect information for you: Blank (no component), Banded, Crosstab, Table, and Chart. You can add more components to a report after Page Report Studio generates it. In this lesson, we create a page report that contains three report tabs, and then perform data analysis on them one by one.

This lesson contains the following tasks:

- Task 1: Create a Banded Report

- Task 2: Create a Table Report

- Task 3: Create a Crosstab Report

- Task 4: Insert a Chart

- Task 5: Analyze Data of the Banded Object

- Task 6: Analyze Data of the Table

- Task 7: Analyze Data of the Crosstab

- Task 8: Analyze Data of the Chart

## 
Task 1: Create a Banded Report

- In the Start Page of the Server Console, select Page Report in the Create category. Server displays a page.

- Select the SampleReports folder and SampleReports.cat catalog file, then select OK. 

- In the New Page Report dialog box, type Order Details in the Report Title text box, select Banded in the layout box, then select OK.
    

- In the Data screen of the Banded Wizard dialog box, select WorldWideSalesBV in Data Source 1 from the Available Data Resources box.
Select Next.

- In the Display screen, expand the Products category in the Resources box, select Product Name and select Add to add it as a detail field to the right box, then expand the Orders Detail category and add Quantity, Unit Price,  and Total one by one to the right box. Select Next. 
    

- In the Group screen, add Country  in the Customers category as the group-by field, keep Ascend as the sort manner, and then select Next. 

- In the Summary screen, select the Country group in the right box, then add Total Sales to summarize the total sales for each country. Select Next.
    

- Skip the Dataset Filter screen and select Next. 

- In the Style screen, set the style to Classic, then select Finish to create the report in Page Report Studio.
    

- Navigate to Menu > File > Rename Report Tab.

- In the Rename Report Tab dialog box, type OrderDetails as the report tab name and select OK.

- Select Save on the toolbar.

- In the Save As dialog box, type CustomerOrders.cls in the File Name text box, then select OK to save the report into the Public Reports > SampleReports folder in the server resource tree. 

 

## 
Task 2: Create a Table Report

- In the current open report window, select New Report Tab  on the toolbar.

- In the New Report Tab dialog box, type Customer Information in the Report Title text box, select Table (Group Above)  in the layout box, then select OK.

- In the Data screen of the Table Wizard dialog box, select CoffeeSalesUSA in Data Source 1, then select Next.

- In the Display screen, select Customer Name, Phone, Postal Code , and Address 1 in the Resources box and select Add to add them as the detail fields of the table one by one. Select Next.
    

- Skip the Group, Summary, and Dataset Filter screens.

- In the Style screen, set the style to Classic, then select Finish to create the table report.
    

- Navigate to Menu > File > Rename Report Tab to rename the report tab as  CustomerInfo.

- Select Save on the toolbar.

-  In the Save Report Template dialog box, select Yes to save the report.

 

## 
Task 3: Create a Crosstab Report

- In the current open report window, select New Report Tab on the toolbar.

- In the New Report Tab dialog box, type Product Sales in the Report Title text box, select Crosstab in the layout box, then select OK. Page Report Studio displays the Crosstab Wizard dialog box.

- In the Data screen, select WorldWideSalesBV in Data Source 1 and then select Next.

- In the Display screen, add Country as the row field and Category as the column field (keep Ascend as the sort manner for both columns and rows), add Total Sales as the summary field, then select Next.
    

- Skip the Dataset Filter screen. Select Next.

- In the Style screen, set the crosstab style to Classic, then select Finish to create the crosstab report.
    

- Navigate to Menu > File > Rename Report Tab to rename the report tab as ProductSales.

- Select Save on the toolbar.

- In the Save Report Template dialog box, select Yes to save the report.

 

## 
Task 4: Insert a Chart

In this task, we insert a chart below the crosstab that we created in Task 3.

- Drag Chart from the Toolbox panel to place it under the last row of the crosstab. 
    

-  In the Data screen the Chart Wizard dialog box, select WorldWideSalesBV in Data Source 1, then select Next.  

- In the Type screen, keep the default chart type Clustered Bar 2-D and select Next.

- In the Display screen, select Sales Quarter in the Resources box and select Add beside the Category box to add it as the category field of the chart, then add Product Type to the Series box and Total Sales to the Show Values box.
    

- Select Finish to create the chart. 

- Select Save on the toolbar.

- In the Save Report Template dialog box, select Yes to save the report.

 

## 
Task 5: Analyze Data of the Banded Object

- In the current report window, select OrderDetails from the Go To drop-down list on the toolbar to switch to this report tab.
    

We want to make the orders in each country further grouped by order ID, so first we need to add another group into the banded object.

- Close the Toolbox panel on the left.

- Expand the Orders Detail category in the Resource View panel, drag Order ID below the Australia group header and release the mouse button when Page Report Studio displays a blue line and a tip "Group Header".
    

Next, we want to add a column about the discount of each product. 

-  Drag Discount from the Resource View panel to the detail panel of the banded object.

The new group and detail column display in the banded object as follows:

Now let's do some adjustments to improve the appearance of the banded object.

- Right-click the Discount label in the banded header and select Properties from the shortcut menu. Page Report Studio displays the Label Properties dialog box.

- In the General tab, edit the Width property to 1.04, then select the Font tab and change Horizontal Alignment to right. Select  OK to apply the property settings. The Discount label now aligns with the values in the same column.
    

There are two group levels in the banded object, to easily distinguish them, we want to change the background color of the Order ID group.

- Right-click any of the Order ID group header panel, the panel of 3033 for example, then select Properties on the shortcut menu.

- In the General tab of the Banded Panel Properties dialog box, set the Background property to #668cb2, then select OK to confirm.

 There is a blank panel before each new order ID begins. This is the group footer panel of the Order ID group. Since the panel does not contain any data, we can hide it.

- Right-click any of the Order ID group footer panel, the blank footer of 3033 for example, then select Hide from the shortcut menu.
    

After we made the appearance adjustments, the banded object looks as follows:

Next, we want to sort and filter the banded object. We sort the totals in descending order for each group, and filter the records by discount to show orders in which the discount is 10 point only.

- Select Sort on the toolbar.

- In the Sort dialog box, choose Total from the field drop-down list, select the sorting manner as Descend, and then select OK to apply the settings.
    

- Right-click any value in the Discount column, then on the shortcut menu, navigate to Filter > 10.00.
    

The banded object finally turns out as follows:

- Select Save on the toolbar.

- In the Save Report Template dialog box, select Yes to save the report.

In this task, we used two ways to sort and filter the report: one by dialog box and the other by right-click menu command. In fact, you can achieve both operations by either way.

 

## 
Task 6: Analyze Data of the Table

- Select CustomerInfo from the Go To drop-down list on the toolbar to switch to this report tab.

First, we want to add more columns to the table. We can do this either by dragging fields from the Resource View panel or using dialog box.

- In the Resource View panel, expand the Customers category, then drag Customer ID to the top left boundary of the Customer Name column and release the mouse button when Page Report Studio displays a vertical blue line on the left of Customer Name. Select OK in the prompt message to use the group object as a detail object.
    

- Right-click any label in the table header, Customer ID for example, and navigate to Insert > Group Column on the shortcut menu.
    

- In the Insert Group Column dialog box, select State in the Resources box as the group-by field and add it to the right box, select the group position as Group Above, keep the default sort order, then select OK to insert the column. 
    

Page Report Studio now groups the table by state as follows: 

We consider the postal code information is not very useful. We want to replace the column with City. 

- Drag City from the Resource View panel to the Postal Code column label and release the mouse button when it covers the label. 

The table changes to:

Lastly, we want to make some adjustments to improve the table appearance. We resize the Address 1 columns to display values in the column entirely and hide the blank group footer. 

- Point to the right boundary of the City column header, when Page Report Studio displays a double headed arrow, drag the boundary to the left.
    

- Select in the blank group footer row. When Page Report Studio displays the icon  at the top left of the table, right-click the icon, then navigate to Show > Table Group Footer on the shortcut menu.
    

The table finally changes to:

- Select Save on the toolbar.

- In the Save Report Template dialog box, select Yes to save the report.

 

## 
Task 7: Analyze Data of the Crosstab

In this task, we demonstrate the Drill feature of Page Report Studio based on the crosstab in the ProductSales report tab. Page Report Studio supports four types of drill actions: drill-up, drill-down, drill-to, and drill-to-by-value. You can apply them on crosstabs, charts, grouped tables, and banded objects. However, to perform the drill-up and drill-down actions on a data component, the business view that the component uses should contain predefined hierarchies, so that you are able to drill from one group level up or down to another within a hierarchy.

- Select ProductSales from the Go To drop-down list on the toolbar to switch to the report tab, which contains a crosstab and a chart.

Since Country is a middle level predefined in the hierarchy Geography of WorldWideSalesBV, we can drill it up or down to the adjacent level.

- Right-click any country in the row header, then navigate to Drill Up > Region on the shortcut menu. 
    

The crosstab refreshes to show as follows:

Next, we want to drill down from Region to Country. However, it is not simply a reversed process of drilling up from Country to Region. When you drill down to a lower group level, Page Report Studio applies the currently selected value as a filter condition to show its data in the lower group level only. Therefore, after drill-down you cannot use drill-up to go back to the previous state, instead you can simply perform an Undo action.

- Right-click Asia-Pacific in the row header and navigate to Drill Down > Country on the shortcut menu. The crosstab now displays only countries in the Asia-Pacific region in the row header. 

We can further drill Country down to State and then to City in this way. Here let's leave the crosstab as it is and try the other two drill actions.

- Right-click any product category in the column header, then navigate to Drill To > Sales Year on the shortcut menu.
    

The crosstab now shows sales in the Asia-Pacific countries in 2015 and 2016.

- Right-click 2016 in the column header and navigate to Drill to by Value > Product Name on the shortcut menu. The crosstab now shows each product's sales in the Asia-Pacific countries in 2016. 

Lastly, we want to rotate the crosstab, that is, to switch its column and row headers so that the crosstab is not split into two.

- Select any aggregation cell in the crosstab to select the crosstab, then select Rotate on the toolbar.

- Resize the crosstab row header by dragging its right boundary to the right to display values in the row header completely.
    

- Select Save on the toolbar.

- In the Save Report Template dialog box, select Yes to save the report.

 

## 
Task 8: Analyze Data of the Chart

In this task, we focus on the chart below the crosstab in the ProductSales report tab. Page Report Studio supports converting a chart to a crosstab, and vice versa. Let's convert the chart to a crosstab first.

- Right-click on the chart and select To Crosstab from the shortcut menu. Page Report Studio displays the To Crosstab dialog box. 

- The Resources box in the Display tab lists the fields used in the crosstab. Add Product Type to the Columns box, Sales Quarter to the Rows box, and Total Sales to the Summaries box. Select OK to generate the crosstab. 
    

Page Report Studio converts the chart to a crosstab.

Next, we want to return the crosstab to chart to go on analyzing with chart. We want to change the chart type to line chart. 

- Select Undo on the toolbar to cancel the operation of converting chart to crosstab.

- Right-click on the chart and  navigate to Chart Type > Line > Line 2-D on the shortcut menu. 

In Page Report Studio, you can change the definition of a chart  at any time. Next, we want to use different type and fields to redefine the chart. 

- Right-click anywhere in the chart except the legend and select Chart Wizard on the shortcut menu. Page Report Studio displays the Chart Definition dialog box. 

- In the Type tab, select the Bench chart type, keep the default subtype Clustered Bench 2-D. 

- Select the Display tab, remove the fields in the Category and Series boxes respectively.

- Select Category in the Resources box and select Add  beside the Category box to add it as the category field of the chart, then add RegionAbbr to the Series box and Total Quantity to the Show Values box. Select OK to create the chart.
    

The new bench chart displays as follows:

You can format properties of the elements in a chart, such as the platform, paper, legend, and axes using the corresponding format dialog boxes to suit your requirements. Next, we edit some properties of the tick marks on the Y axis to briefly introduce the Chart Format feature. 

- Right-click anywhere in the chart except the legend and navigate to Format Axis > Format Value (Y) Axis on the shortcut menu.

- In the Format Value (Y) Axis dialog box, switch to the Tick Mark tab, in the Major Tick Mark subtab, select Cross, clear Correlate with Axis and type #ff3333 in the Color text box, specify to show data labels every 2 tick marks. Select OK to apply the properties.
    

The tick marks and data labels on the Y axis apply the new properties.

- Select Save on the toolbar.

- In the Save Report Template dialog box, select Yes to save the report.
